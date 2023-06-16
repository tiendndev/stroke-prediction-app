from flask import request, jsonify, flash, redirect, url_for
from flask_login import current_user
from sqlalchemy import func

from strokeprediction.extension import db
from strokeprediction.library_ma import SymptomSchema
from strokeprediction.models import Note, User

symptom_schema = SymptomSchema()
symptoms_schema = SymptomSchema(many=True)


def add_symptom_service():
    data = request.json
    if (data and ("user_id" in data) and ("gender" in data) and ("age" in data) and ("hypertension" in data)
        and ("heart_desease" in data) and ("ever_married" in data) and ("work_type" in data) and ("residence_type") and
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
        residence_type = data["residence_type"]
        avg_glucose_level = data["avg_glucose_level"]
        bmi = data["bmi"]
        smoking_status = data["smoking_status"]
        try:
            new_book = Note(id, fullname, user_id, gender, age, hypertension, heart_desease, ever_married,
                            work_type, residence_type, avg_glucose_level, bmi, smoking_status)
            db.session.add(new_book)
            db.session.commit()
            return jsonify({"message": "Add success!"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not add symptom!"}), 400
    else:
        return jsonify({"message": "Request error!"}), 400


# Get symptom
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
            return jsonify({"message": "symptom is deleted"}), 200
        except IndentationError:
            db.session.rollback()
            return jsonify({"message": "Can not delete symptom!"}), 400
    else:
        return jsonify({"message": "Not found symptom!"}), 400


# Get symptoms by user_email
def get_symptoms_by_patient_service(user_email):
    symptom = Note.query.join(User).filter(
        func.lower(User.email) == user_email.lower()
    ).all()
    if symptom:
        return symptoms_schema.jsonify(symptom)
    else:
        return jsonify({"message": f"Not found symptoms by patient {user_email}"}), 404
    

def get_user_email_by_id_service(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    
    return jsonify({'email': user.email})


def get_patient_medical_records():
    patient = current_user

    if patient.notes:
        medical_records_data = {
            'id': patient.notes.id,
            'fullname': patient.notes.fullname,
            'gender': patient.notes.gender,
            'age': patient.notes.age,
            'hypertension': patient.notes.hypertension,
            'heart_disease': patient.notes.heart_disease,
            'ever_married': patient.notes.ever_married,
            'residence_type': patient.notes.residence_type,
            'avg_glucose_level': patient.notes.avg_glucose_level,
            'bmi': patient.notes.bmi,
            'work_type': patient.notes.work_type,
            'smoking_status': patient.notes.smoking_status,
            'stroke': patient.notes.stroke,
            'percentageStroke': patient.notes.percentageStroke,
        }
    else:
        medical_records_data = None

    return jsonify({
        'patient': patient.user_name,
        'medical_records': medical_records_data
    })