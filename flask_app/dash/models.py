import re
import csv
import random
import sqlite3
import requests
from bs4 import BeautifulSoup
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

	conn2 = sqlite3.connect("dash/static/data/review.db")
	c2 = conn2.cursor()
	
	c2.execute("DROP TABLE labeled_reviews")
	c2.execute("CREATE TABLE labeled_reviews('review', 'label')")

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

# VERIFICATION PAGE

def scrape_amazon(main_page_url, headers):
    main_page = requests.get(main_page_url, headers=headers)
    main_page_soup = BeautifulSoup(main_page.content, 'html.parser')
    print(main_page_soup.prettify())
    data = []
    
    product_name = main_page_soup.find('span', {'id': 'productTitle'}).get_text().strip()
    brand_name = main_page_soup.find('a', {'id': 'bylineInfo'}).get_text().strip()[7:]
    price = main_page_soup.find('span', {'id': 'priceblock_ourprice'}).get_text().strip()[1:]
    asin = main_page_soup.find('ul', {'class': 'detail-bullet-list'}).findAll('li')[4].findAll('span')[2].get_text()
    overall_rating = main_page_soup.find('span', {'data-hook': 'rating-out-of-text'}).get_text()[:3]
    
    review_url_base = url[:-1].replace("dp", "product-reviews") + "?ie=UTF8&reviewerType=all_reviews&sortBy=recent&pageNumber="
    review_urls = [review_url_base + str(i) for i in range(1, 10)]
    
    for review_url in review_urls:
        review_page = requests.get(review_url, headers=headers)
        review_page_soup = BeautifulSoup(review_page.content, 'html.parser')
        username = review_page_soup.findAll('span', {'class': 'a-profile-name'})
        date = review_page_soup.findAll('span', {'data-hook': 'review-date'})
        rating = soup.find_all('i', {'data-hook': 'review-star-rating'})
        review = soup.find_all('span', {'data-hook': 'review-body'})
        
        for i in range(2, 8):
            try:
                reviewer_username = username[i].get_text()
                review_date = date[i].get_text()[33:]
                review_rating = rating[i].span.get_text()[:3]
                review_text = review[i].get_text()[:-9].strip()

                data.append([brand_name, product_name, asin, price, overall_rating, reviewer_username, review_date, review_rating, review_text])
                
            except:
                continue
    return data

def write_reviews_to_db(data):
    conn = sqlite3.connect("reviewdb.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS scraped_reviews ('brand_name', 'product_name', 'asin', 'price', 'overall_rating', 'reviewer_username', 'review_date', 'review_rating', 'review_text')""")
    
    for entry in data:
        c.execute("INSERT INTO scraped_reviews ('brand_name', 'product_name', 'asin', 'price', 'overall_rating', 'reviewer_username', 'review_date', 'review_rating', 'review_text') VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", 
                  (entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], entry[6], entry[7], entry[8]))
        
    conn.commit()
    conn.close()