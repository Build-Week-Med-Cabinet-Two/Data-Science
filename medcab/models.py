from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy()

class Strain(DB.Model):
    '''cannabis strains'''

    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(30), nullable=False)
    kind = DB.Column(DB.String(6), nullable=False)
    rating = DB.Column(DB.Float, nullable=False)
    effects = DB.Column(DB.Text, nullable=False)
    flavor = DB.Column(DB.Text, nullable=False)
    description = DB.Column(DB.Text, nullable=False)
    symptoms_diseases = DB.Column(DB.Text)
    all_text_search = DB.Column(DB.Text, nullable=False)
