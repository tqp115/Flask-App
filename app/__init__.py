from flask import Flask

#initialize app

app = Flask(__name__, instance_relative_config=True)

from app import views

#load config file

app.config.from_object('config')

# use .env to hide hardcoded key
import os
from dotenv import load_dotenv
load_dotenv()
app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY")