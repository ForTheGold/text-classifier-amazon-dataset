from flask import render_template, url_for, flash, redirect, Markup
from dash.forms import ClassifyUserInputForm, GenerateDataForm, ScrapeAmazonForm, ScrapeRedditForm
from dash import app
from dash.models import *

messages = []

@app.route('/')
@app.route('/project')
def project():
	return render_template('project.html', title='Project')

@app.route('/database')
def database():
	return render_template('database.html', title='Database')

@app.route('/model', methods=['GET', 'POST'])
def model():
	messages2 = []
	form = GenerateDataForm()

	output_string_to_list = output_string[26:].split()

	if form.submit.data and form.validate():
		if form.validate_on_submit():
			classification = create_new_feature_set()
			messages2 = ["A new dataset has been successfully generated."]
			return redirect(url_for('model'))



	return render_template('model.html', form=form, 
												messages=messages2,
												accuracy=accuracy, 
												features=features, 
												output_string_to_list=output_string_to_list, 
												title='Model and Preprocessing')

@app.route('/verification', methods=['GET', 'POST'])
def verification():
	form = ScrapeAmazonForm()
	if form.validate_on_submit():
		# headers = {'User-Agent':"""Mozilla/5.0 (X11; Linux x86_64) 
  #              				 AppleWebKit/537.36 (KHTML, like Gecko) 
  #                  			 Chrome/44.0.2403.157 Safari/537.36""",
  #                          'Accept-Language': 'en-US, en;q=0.5'}
		headers = {
						"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0", 
			           "Accept-Encoding":"gzip, deflate", 
			           "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
			           "DNT":"1","Connection":"close", 
			           "Upgrade-Insecure-Requests":"1"
			      }

		amazon_reviews = scrape_amazon(form.user_url_input.data, headers)
		write_reviews_to_db(amazon_reviews)
		return redirect(url_for('verification'))
	try: 
		conn = sqlite3.connect("dash/static/data/reviewdb.db")
		c = conn.cursor()
		c.execute("SELECT reviewer_username, review_date, review_rating, review_text FROM scraped_reviews")
		amazon_data = c.fetchall()

		our_classifications = [classify_text(review[3]) for review in amazon_data]

		c2 = conn.cursor()
		c2.execute("SELECT DISTINCT(brand_name) FROM scraped_reviews")
		brand_names = c2.fetchall()

		brand_name_values = [brand_name[0].replace(" ", "-") for brand_name in brand_names]

		c3 = conn.cursor()
		c3.execute("SELECT DISTINCT(product_name), brand_name, asin, price, overall_rating FROM scraped_reviews WHERE brand_name=?", (brand_names[0]))
		brand_header = c3.fetchall()
		conn.close()

	except:
		brand_names = ""
		brand_name_values = ""
		brand_header = ""
		amazon_data = ""
		our_classifications = ""
	
	return render_template('verification.html', 
							form=form,
							brand_names=brand_names,
							brand_name_values=brand_name_values,
							brand_header=brand_header, 
							amazon_data=amazon_data,
							our_classifications=our_classifications, 
							title='Verification')

@app.route('/predictions', methods=['GET', 'POST'])
def predictions():
	form = ScrapeRedditForm()

	if form.validate_on_submit():
		headers = {'User-Agent': 'Mozilla/5.0'}
		(title, clean_comments) = scrape_reddit(form.user_url_input.data, headers)
		write_to_reddit_thread_db(title, clean_comments)
		return redirect(url_for('predictions'))

	try:
		conn = sqlite3.connect("dash/static/data/reviewdb.db")
		c = conn.cursor()
		c.execute("SELECT * FROM reddit_thread")
		reddit_data = c.fetchall()

		our_classifications = [classify_text(review[1]) for review in reddit_data]
		total_comment_count = len(our_classifications)
		positive_comment_count = len([classification for classification in our_classifications if classification == "pos"])
		negative_comment_count = len([classification for classification in our_classifications if classification == "neg"])
	except:
		reddit_data = ""
		our_classifications = ""

	return render_template('predictions.html', form=form, 
												reddit_data=reddit_data, 
												our_classifications=our_classifications,
												total_comment_count=total_comment_count,
												positive_comment_count=positive_comment_count,
												negative_comment_count=negative_comment_count,
												title='Predictions')


@app.route('/demo', methods=['GET', 'POST'])
def demo():
	form = ClassifyUserInputForm()

	if form.validate_on_submit():
		classification = classify_text(form.user_review.data)
		if classification == "pos":
			classification = "positive"
		else:
			classification = "negative"
		messages.append((form.user_review.data, classification))
		return redirect(url_for('demo'))

	return render_template('demo.html', title='Demonstration', form=form, messages=messages)

@app.route('/visualizations')
def visualizations():
	return render_template('visualizations.html', title='Visualizations')

@app.route('/presentation')
def presentation():
	return render_template('presentation.html', title='Presentation')