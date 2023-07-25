import os
from dotenv import load_dotenv

# load .env de nhan KEY & DB_URL
load_dotenv()

SECRET_KEY = os.environ.get("KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("DB_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False


class Config(object):
    DEBUG = True
    TESTING = False


class DevelopmentConfig(Config):
    # SECRET_KEY = "this-is-a-super-secret-key"
    OPENAI_KEY = os.environ.get("OPENAI_KEY")


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
