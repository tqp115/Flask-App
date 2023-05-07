from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_admin = db.Column(db.Boolean, default = False)
    username = db.Column(db.String(64), unique=True, index = True)
    email = db.Column(db.String(120), unique=True, index = True)
    password = db.Column(db.String(128))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    last_login = db.Column(db.DateTime)
    uploads = db.relationship('DataSet', backref = 'author', lazy = 'dynamic', cascade='all, delete')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    def set_password(self, password):
        self.password = generate_password_hash(str(password))
    def check_password(self, password):
        return check_password_hash(self.password, password)

class DataSet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    file = db.Column(db.LargeBinary)
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f"DataSet('{self.name}', '{self.file}')"