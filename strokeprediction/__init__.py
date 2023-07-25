from flask import Flask
import os
from dotenv import load_dotenv
from flask_login import LoginManager
from datetime import timedelta

from .extension import ma, db
from .user_info.controller import symptoms

load_dotenv()
SECRET_KEY = os.environ.get("KEY")
SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_database(app):
        with app.app_context():
             db.create_all()
        print("Created Database")

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    # Khai bao duong dan chua database va khoi tao db
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql://root:qMsNy6GDgOjLCg7p7a5v@containers-us-west-92.railway.app:5494/railway"
    db.init_app(app)

    """ Khoi tao api """
    ma.init_app(app)

    # import and setup database
    from .models import Note, User
    create_database(app)

    # Khoi tao user (phai de sau create_database)
    from strokeprediction.user import user
    from strokeprediction.views import views

    # Lien ket user va views
    app.register_blueprint(user)
    app.register_blueprint(views)

    """ Lien ket voi controller """
    app.register_blueprint(symptoms)

    login_manager = LoginManager()
    login_manager.login_view = "user.login"
    login_manager.init_app(app)

    # Set life time cua user (sau 1p se logout)
    app.permanent_session_lifetime = timedelta(minutes=1)

    @login_manager.user_loader
    # Tra ve Id cua nguoi dung dang su dung
    def load_user(id):
        return User.query.get(int(id))
    return app