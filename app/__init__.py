from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#initialize app

app = Flask(__name__, instance_relative_config=True)
app.config.from_object(Config)
db = SQLAlchemy
migrate = Migrate(app, db)

from app import views

#load config file

app.config.from_object('config.Config')