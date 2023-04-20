from flask_login import UserMixin
from datetime import timezone
from sqlalchemy.sql import func

from strokeprediction import db


class Note(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    fullname = db.Column(db.String(30))

    # New data
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(10))
    age = db.Column(db.Integer)
    hypertension = db.Column(db.Integer)
    heart_desease = db.Column(db.String(10))
    ever_married = db.Column(db.String(10))
    residence_type = db.Column(db.String(10))
    avg_glucose_level = db.Column(db.Float)
    bmi = db.Column(db.Float)
    work_type = db.Column(db.String(20))
    smoking_status = db.Column(db.String(20))

    stroke = db.Column(db.Integer)

    def __init__(self, fullname, user_id, gender, age, hypertension,
                 heart_desease, ever_married, work_type, residence_type,
                 avg_glucose_level, bmi, smoking_status, stroke):
        self.fullname = fullname
        self.user_id = user_id
        self.gender = gender
        self.age = age
        self.hypertension = hypertension
        self.heart_desease = heart_desease
        self.ever_married = ever_married
        self.work_type = work_type
        self.residence_type = residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.smoking_status = smoking_status
        self.stroke = stroke


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    # Cac quan he trong database (1-1, 1-n, n-n)
    # O day su dung quan he 1-n
    notes = db.relationship("Note")

    def __init__(self, email, password, user_name):
        self.email = email
        self.password = password
        self.user_name = user_name
