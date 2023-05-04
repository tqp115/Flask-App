from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from app import db

db = SQLAlchemy()

class User(db.Model):
    """Model for user acccounts."""
    __tablename__ = 'users'


    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(20), nullable=False)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class DataSet(db.Model):
    """Model for data sets."""
    __tablename__ = 'datasets'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    file = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"DataSet('{self.name}', '{self.file}')"
