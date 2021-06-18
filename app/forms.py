from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class InputForm(FlaskForm):
	user_review = StringField('Write your review here', 
								validators=[DataRequired(), 
								Length(min=10)])
	submit = SubmitField('Check Your Review!')

	
