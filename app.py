from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


@app.route("/")
@app.route("/home")
def home():
    return 'The API is up and Running! '

@app.route('/api', methods=['GET', 'POST'])
def results():
    