from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
from wtforms.widgets import TextArea

class GenerateDataForm(FlaskForm):
	submit = SubmitField('Generate New Data!')

class InputForm(FlaskForm):
	user_review = StringField('Write your review here', 
								widget=TextArea(),
								validators=[DataRequired(), 
								Length(min=10)])
	submit = SubmitField('Check Your Review!')

	
