from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Strain(db.Model):
    '''cannabis strains'''

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    kind = db.Column(db.String(6), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    effects = db.Column(db.Text, nullable=False)
    flavor = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    symptoms_diseases = db.Column(db.Text)
    all_text_search = db.Column(db.Text, nullable=False)