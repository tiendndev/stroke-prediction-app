import uuid
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
    heart_disease = db.Column(db.String(10))
    ever_married = db.Column(db.String(10))
    residence_type = db.Column(db.String(10))
    avg_glucose_level = db.Column(db.Float)
    bmi = db.Column(db.Float)
    work_type = db.Column(db.String(20))
    smoking_status = db.Column(db.String(20))

    stroke = db.Column(db.Integer)
    percentageStroke = db.Column(db.Float)

    def __init__(self, fullname, user_id, gender, age, hypertension,
                 heart_disease, ever_married, work_type, residence_type,
                 avg_glucose_level, bmi, smoking_status, stroke, percentageStroke):
        self.fullname = fullname
        self.user_id = user_id
        self.gender = gender
        self.age = age
        self.hypertension = hypertension
        self.heart_disease = heart_disease
        self.ever_married = ever_married
        self.work_type = work_type
        self.residence_type = residence_type
        self.avg_glucose_level = avg_glucose_level
        self.bmi = bmi
        self.smoking_status = smoking_status
        self.stroke = stroke
        self.percentageStroke = percentageStroke


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    user_name = db.Column(db.String(150))
    # Cac quan he trong database (1-1, 1-n, n-n)
    # 1-1 Relationship
    notes = db.relationship("Note", backref='user', uselist=False)
    events = db.relationship("Event", backref='user', uselist=False)

    def __init__(self, email, password, user_name):
        self.email = email
        self.password = password
        self.user_name = user_name

class Event(db.Model, UserMixin):
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    start_event = db.Column(db.DateTime)
    end_event = db.Column(db.DateTime)

    def __init__(self, user_id, title, start_event, end_event):
        self.user_id = user_id
        self.title = title
        self.start_event = start_event
        self.end_event = end_event