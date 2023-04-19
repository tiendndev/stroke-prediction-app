from flask import request, jsonify, flash, redirect, url_for
from sqlalchemy import func

from strokeprediction.extension import db
from strokeprediction.library_ma import SymptomSchema
from strokeprediction.models import Note, User

symptom_schema = SymptomSchema()
symptoms_schema = SymptomSchema(many=True)


def add_symptom_service():
    data = request.json
    if (data and ("user_id" in data) and ("gender" in data) and ("age" in data) and ("hypertension" in data)
        and ("heart_desease" in data) and ("ever_married" in data) and ("work_type" in data) and ("resident_type") and
            ("avg_glucose_level" in data) and ("bmi" in data) and ("smoking_status" in data)):

        id = data["id"]
        fullname = data["fullname"]

        user_id = data["user_id"]
        age = data["age"]
        gender = data["gender"]
        hypertension = data["hypertension"]
        heart_desease = data["heart_desease"]
        ever_married = data["ever_married"]
        work_type = data["work_type"]
        resident_type = data["resident_type"]
        avg_glucose_level = data["avg_glucose_level"]
        bmi = data["bmi"]
        smoking_status = data["smoking_status"]
        try:
            new_book = Note(id, fullname, user_id, gender, age, hypertension, heart_desease, ever_married,
                            work_type, resident_type, avg_glucose_level, bmi, smoking_status)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add symptom!"}), 400
    else:
        return jsonify({"message": "Request error!"}), 400


# Get symptom by id
def get_symptom_by_id_service(id):
    symptom = Note.query.get(id)
    if symptom:
        # Mapping cac field cua book vao cac field cua schema
        return symptom_schema.jsonify(symptom)
    else:
        return jsonify({"message": "Not found symptom!"}), 400


# Get all symptoms
def get_all_symptoms_service():
    symptoms = Note.query.all()
    if symptoms:
        return symptoms_schema.jsonify(symptoms)
    else:
        return jsonify({"message": "Not found symptom!"}), 400


# Delete symptom
def delete_symptom_by_id_service():
    symptom = Note.query.get(1)
    if symptom:
        try:
            db.session.delete(symptom)
            db.session.commit()
            return "symptom is deleted"
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete symptom!"}), 400
    else:
        return jsonify({"message": "Not found symptom!"}), 400
