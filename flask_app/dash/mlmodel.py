import csv
import random
import nltk
from nltk.tokenize import RegexpTokenizer

def make_training_feature_set():
	data = []
	with open('../2000reviews.csv') as f:
	    reader = csv.reader(f, delimiter=',')
	    for i in reader:
	        data.append(i)

	f.close()

	tokenizer = RegexpTokenizer(r'\w+')

	labeled_reviews = []

	for i in data:
	    if i[1] == 'pos':
	        tokens = tokenizer.tokenize(i[0])
	        labeled_reviews.append((tokens, 'pos'))
	        
	    else:
	        tokens = tokenizer.tokenize(i[0])
	        labeled_reviews.append((tokens, 'neg'))

	return labeled_reviews

def find_features(document, word_features):
	features = {}
	for w in word_features:
		features[w] = (w in document[0])
	return features

def train_classifier(labeled_reviews):

	all_words = []
	for review in labeled_reviews:
	    for word in review[0]:
	        all_words.append(word)

	all_words = nltk.FreqDist(all_words)
	word_features = list(all_words.keys())[:3000]

	featuresets = [(find_features(reviews, word_features), category) for (reviews, category) in labeled_reviews]

	training_percent = int(len(featuresets)*.7)
	training_set = featuresets[:training_percent]

	classifier = nltk.NaiveBayesClassifier.train(featuresets)

	return (classifier, word_features)



def text_to_feature_set(review, word_features):
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(review.lower())
	features = {}
	for word in word_features:
		features[word] = (word in tokens)
	return features

def classify_text(user_input):
	labeled_reviews = make_training_feature_set()
	(classifier, word_features) = train_classifier(labeled_reviews)

	
	return classifier.classify(text_to_feature_set(user_input, word_features))

