#Using SQLAlchemy to store data in local system
from flask_sqlalchemy import SQLAlchemy

#database object
db = SQLAlchemy()

class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20))
    last_name=db.Column(db.String(20))

class SameNames(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    same_name = db.Column(db.String(20))
