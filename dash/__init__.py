from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretnumbers12345'

from dash import routes