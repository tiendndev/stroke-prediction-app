import os
from dotenv import load_dotenv

# load .env de nhan KEY & DB_URL
load_dotenv()

SECRET_KEY = os.environ.get("KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
