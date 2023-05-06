from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    account_type = db.Column(db.String(20))
    username = db.Column(db.String(64), unique=True, index = True)
    email = db.Column(db.String(120), unique=True, index = True)
    password = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    uploads = db.relationship('DataSet', backref = 'author', lazy = 'dynamic')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    def 

class DataSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    file = db.Column(db.LargeBinary)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"DataSet('{self.name}', '{self.file}')"