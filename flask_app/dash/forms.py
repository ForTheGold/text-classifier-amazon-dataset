from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea

class GenerateDataForm(FlaskForm):
	submit = SubmitField('Generate New Data!')

class ClassifyUserInputForm(FlaskForm):
	user_review = StringField('Write your review here', 
								widget=TextArea(),
								validators=[DataRequired()])
	submit = SubmitField('Check Your Review!')

class ScrapeAmazonForm(FlaskForm):
	user_url_input = StringField('Enter an Amazon Product URL to Scrape')
	submit = SubmitField('Scrape Amazon!')

class ScrapeRedditForm(FlaskForm):
	user_url_input = StringField('Enter an Reddit Thread URL to Scrape')
	submit = SubmitField('Scrape Reddit!')

	
