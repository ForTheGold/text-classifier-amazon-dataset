import re
import csv
import random
import sqlite3
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

# FEATURE SET

def create_new_feature_set():
	data = []

	with open("dash/static/data/groceries_trimmed.csv") as f:
	    reader = csv.reader(f, delimiter=',')
	    for i in reader:
	        data.append(i)
	f.close()

	data = data[1:]

	tokenizer = RegexpTokenizer(r'\w+')
	stop_words = set(stopwords.words('english'))

	positive = []
	negative = []

	regex = re.compile('[^a-zA-Z0-9]')
	lemmatizer = WordNetLemmatizer()

	for i in data:
	    if i[0] == '5':
	        filtered = []
	        tokens = tokenizer.tokenize(i[1].lower())
	        for j in tokens:
	            j = regex.sub('', j)
	            if len(j) > 2 and j not in stop_words:
	                lemma = lemmatizer.lemmatize(j)
	                filtered.append(lemma)

	        if len(filtered) > 0:
	            positive.append((filtered, 'pos'))
	    else:
	        filtered = []
	        tokens = tokenizer.tokenize(i[1].lower())
	        for j in tokens:
	            j = regex.sub('', j)
	            if len(j) > 2 and j not in stop_words:
	                lemma = lemmatizer.lemmatize(j)
	                filtered.append(lemma)
	                
	        if len(filtered) > 0:
	            negative.append((filtered, 'neg'))

	random.shuffle(positive)
	random.shuffle(negative)
	labeled_reviews = positive[:1000] + negative[:1000]
	random.shuffle(labeled_reviews)

	labeled_reviews_joined = []
	for i in labeled_reviews:
		labeled_reviews_joined.append((" ".join(i[0]), i[1]))

	conn2 = sqlite3.connect("dash/static/data/review1.db")
	c2 = conn2.cursor()

	c2.execute("""CREATE TABLE labeled_reviews('review', 'label')""")

	for entry in labeled_reviews_joined:
	    c2.execute("INSERT INTO labeled_reviews('review', 'label') VALUES(?, ?)", (entry[0], entry[1]))
	conn2.commit()

	conn2.close()


# DEMO PAGE

def make_training_feature_set():

	conn = sqlite3.connect("dash/static/data/review.db")
	c = conn.cursor()

	c.execute("SELECT * FROM labeled_reviews")
	data = c.fetchall()

	labeled_reviews = []

	tokenizer = RegexpTokenizer(r'\w+')
	
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
	return classifier.classify(text_to_feature_set(user_input, word_features))


labeled_reviews = make_training_feature_set()
(classifier, word_features) = train_classifier(labeled_reviews)