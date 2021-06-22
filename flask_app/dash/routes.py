from flask import render_template, url_for, flash, redirect, Markup
from dash.forms import InputForm
from dash import app
from dash.mlmodel import make_training_feature_set, find_features, train_classifier, text_to_feature_set, classify_text

@app.route('/')
@app.route('/project')
def project():
	return render_template('project.html', title='Project')

@app.route('/data')
def data():
	return render_template('data.html', title='data')

@app.route('/database')
def database():
	return render_template('database.html', title='database')

@app.route('/preprocessing')
def preprocessing():
	return render_template('preprocessing.html', title='preprocessing')

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
		message = Markup(f"<h3>You typed: { form.user_review.data }! <br /> This was classified as a <strong>{ classification }</strong> review.</h3>")
		flash(message, "CLASS_NAME")
		return redirect(url_for('demo'))
	return render_template('demo.html', title='Demo', form=form)

@app.route('/visualizations')
def visualizations():
	return render_template('visualizations.html', title='Visualizations')