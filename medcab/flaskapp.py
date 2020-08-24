from os import getenv
from flask import Flask, request, render_template, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from .model import db



def create_app():
    '''Create and configure an instance of the Flask application'''
    app = Flask(__name__)
    load_dotenv()
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    app.config['DEBUG'] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = getenv('DATABASE_URL')  # <---- work on getting the URL corrected
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db = SQLAlchemy(app)
    db.init_app(app)

    @app.route('/')
    def root():
        return 'WELCOME TO MY FLASK APP!!'


    @app.route('/test', methods=['POST', 'GET'])
    def predict_strain():
        text = request.get_json(force=True)
        # Once we know the name of dspt5 name of model, replace predict on line 32 and import from their file
        predictions = predict(text)
        return jsonify(predictions)

    #@app.route('/user/<name>', methods=['GET'])
    #def user(name=None, message=''):
    #    name = name or request.values['user_name']
    #    try:
    #        if request.method == 'POST':
    #            db.session.add(name)
    #            db.session.commit
    #            message = "User {} successfully added!".format(name)
    #    except Exception as e:
    #        message = "Error adding {}: {}".format(name, e)
    #    return

    return app