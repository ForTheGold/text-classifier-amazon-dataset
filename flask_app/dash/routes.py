from flask import render_template, url_for, flash, redirect, Markup
from dash.forms import InputForm, GenerateDataForm
from dash import app
from dash.models import *

messages = []

@app.route('/')
@app.route('/project')
def project():
	return render_template('project.html', title='Project')

@app.route('/data')
def data():
	return render_template('data.html', title='Data')

@app.route('/database')
def database():
	return render_template('database.html', title='Database')

@app.route('/preprocessing', methods=['GET', 'POST'])
def preprocessing():
	messages = []
	form = GenerateDataForm()
	if form.validate_on_submit():
		classification = create_new_feature_set()
		messages = ["A new dataset has been successfully generated."]
		return redirect(url_for('preprocessing'))
	return render_template('preprocessing.html', form=form, messages=messages, title='Preprocessing')

@app.route('/model')
def model():
	return render_template('model.html', title='Model')

@app.route('/verification')
def verification():
	return render_template('verification.html', title='Verification')

@app.route('/predictions')
def predictions():
	return render_template('predictions.html', title='Predictions')

@app.route('/demo', methods=['GET', 'POST'])
def demo():
	form = InputForm()
	if form.validate_on_submit():
		classification = classify_text(form.user_review.data)
		if classification == "pos":
			classification = "positive"
		else:
			classification = "negative"
		messages.append((form.user_review.data, classification))
		#message = Markup(f"<h3>You typed: { form.user_review.data }! <br /> This was classified as a <strong>{ classification }</strong> review.</h3>")
		#flash(message, "CLASS_NAME")
		return redirect(url_for('demo'))
	return render_template('demo.html', form=form, messages=messages, title='Demo')

@app.route('/visualizations')
def visualizations():
	return render_template('visualizations.html', title='Visualizations')

@app.route('/presentation')
def presentation():
	return render_template('presentation.html', title='Presentation')