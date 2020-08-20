from os import getenv
from flask import Flask, request, render_template
from dotenv import load_dotenv

load_dotenv

def create_app():
    '''Create and configure an instance of the Flask application'''

    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URL')  # <---- work on getting the URL corrected
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    @app.route('/')
    def root():
        return #(either a template or some other front page)

    @app.route('/_____', methods=['']) # Next route