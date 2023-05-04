import os
from dotenv import load_dotenv
load_dotenv()
DEBUG = True

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY")