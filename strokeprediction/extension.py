from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

# Khai bao doi tuong db
db = SQLAlchemy()

# Marshmallow giup validate du lieu tra ve dang json cho frontend
ma = Marshmallow()