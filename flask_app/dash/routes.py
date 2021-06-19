from flask import render_template, url_for, flash, redirect
from dash.forms import InputForm
from dash import app

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
	form = InputForm()
	if form.validate_on_submit():
		flash(f'You typed: { form.user_review.data } !', "CLASS_NAME")
		return redirect(url_for('home'))
	return render_template('home.html', title='Home', form=form)