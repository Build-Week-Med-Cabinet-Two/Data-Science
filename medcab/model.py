'''SQLAlchemy model for medcab'''
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# Should we use the column names etc from the kaggle db?
# Also, should these be split into 2 like it was in Twitoff, or should it be just one class?

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    strain = db.Column(db.String(80), unique=True, nullable=False)
    planttype = db.Column(db.String(80), unique=True, nullable=False)
    rating = db.Column(db.Float, unique=True, nullable=False)
    effects = db.Column(db.Unicode(300), unique=True, nullable=False)
    flavor = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Unicode(300), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.strain

#class PlantRatingDesc(db.Model):
    #id = db.Column(db.Integer, primary_key=True)
    #rating = db.Column(db.Float, unique=True, nullable=False)
    #effects = db.Column(db.Unicode(300), unique=True, nullable=False)
    #flavor = db.Column(db.String(80), unique=True, nullable=False)
    #description = db.Column(db.Unicode(300), unique=True, nullable=False)

    #def __repr__(self):
    #    return '<PlantRatingDesc %r>' % self.rating


