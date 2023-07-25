import uuid
from flask import render_template, request, jsonify, flash
from flask_login import current_user
from sqlalchemy import func
from werkzeug.security import generate_password_hash
from strokeprediction import aiapi

from strokeprediction.extension import db
from strokeprediction.library_ma import SymptomSchema
from strokeprediction.models import Note, User, Event

symptom_schema = SymptomSchema()
symptoms_schema = SymptomSchema(many=True)


# Add symptoms
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


# Get all symptoms of all patients
def get_all_symptoms_service():
    symptoms = Note.query.all()
    if symptoms:
        return symptoms_schema.jsonify(symptoms)
    else:
        return jsonify({"message": "Not found symptom!"}), 400


# Delete symptom of patient
def delete_symptom_by_id_service():
    patient = current_user

    if patient.notes:
        # Delete all the notes for the patient
        db.session.delete(patient.notes)
        db.session.commit()
        return jsonify({'message': 'Medical records deleted successfully'})
    else:
        return jsonify({'error': 'No medical records found for the patient'}), 404


# Get symptoms by user_email
def get_symptoms_by_patient_service(user_email):
    symptom = Note.query.join(User).filter(
        func.lower(User.email) == user_email.lower()
    ).all()
    if symptom:
        return symptoms_schema.jsonify(symptom)
    else:
        return jsonify({"message": f"Not found symptoms by patient {user_email}"}), 404


# Get symptoms of patient
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
        'email': patient.email,
        'medical_records': medical_records_data
    })


#  Delete patient account
def delete_current_patient(email):
    patient = User.query.filter_by(email=email).first()

    if patient:
        Event.query.filter_by(user_id=patient.id).delete()
        db.session.delete(patient)
        db.session.commit()
        return True
    else:
        return False
    

#  Update patient_email
def update_patient_email_service():
    new_email = request.form.get('new_email')

    if not new_email:
        return jsonify({'message': 'Yêu cầu email mới'}), 400

    current_patient = User.query.get(current_user.id)
    if not current_patient:
        return jsonify({'message': 'Người dùng không tìm thấy'}), 404

    current_patient.email = new_email
    db.session.commit()

    return jsonify({'message': 'Cập nhật email thành công'})


#  Update patient_password
def update_patient_password_service():
    new_password = request.form.get('new_password')

    if not new_password:
        flash('Yêu cầu mật khẩu mới')
        return jsonify({'message': 'Yêu cầu mật khẩu mới'}), 400

    current_patient = User.query.get(current_user.id)
    if not current_patient:
        flash('Không tìm thấy người dùng')
        return jsonify({'message': 'Không tìm thấy người dùng'}), 404

    current_patient.password = generate_password_hash(new_password, method="sha256")
    db.session.commit()

    flash('Mật khẩu cập nhật thành công')
    return jsonify({'message': 'Mật khẩu cập nhật thành công'})



def event_index_service():
    user_id = current_user.id
    calendar = Event.query.filter_by(user_id=user_id).order_by(Event.id).all()
    return render_template('calendar.html', calendar=calendar, user=current_user)


def event_insert_service():
    if request.method == 'POST':
        user_id = User.query.get(current_user.id).id
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        event = Event(user_id=user_id, title=title, start_event=start, end_event=end)
        db.session.add(event)
        db.session.commit()
        msg = 'success'
        return jsonify(msg)
    

def event_update_service():
    if request.method == 'POST':
        id = request.form['id']
        title = request.form['title']
        start = request.form['start']
        end = request.form['end']
        event = Event.query.get(id)
        if event:
            event.title = title
            event.start_event = start
            event.end_event = end
            db.session.commit()
            msg = 'success'
        else:
            msg = 'error'
        return jsonify(msg)
    

def event_ajax_delete_service():
    if request.method == 'POST':
        id = request.form['id']
        event = Event.query.get(id)
        if event:
            db.session.delete(event)
            db.session.commit()
            msg = 'Record deleted successfully'
        else:
            msg = 'Record not found'
        return jsonify(msg)
    