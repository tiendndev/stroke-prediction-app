from flask import Blueprint, jsonify, render_template, request, redirect, url_for
from flask_login import login_required, current_user

from .services import (
    add_symptom_service, 
    get_all_symptoms_service, 
    delete_symptom_by_id_service, 
    get_symptoms_by_patient_service, 
    get_patient_medical_records, 
    delete_current_patient, 
    update_patient_email_service, 
    update_patient_password_service,
    event_index_service,
    event_insert_service,
    event_update_service,
    event_ajax_delete_service,
)

symptoms = Blueprint("symptoms", __name__)


# Add new symptoms
@symptoms.route("/patient-management/patient", methods=["POST"])
def add_symptom():
    return add_symptom_service()


# Get all symptoms of all patients
@symptoms.route("/patient-management/views", methods=["GET"])
def get_all_symptoms():
    return get_all_symptoms_service()


# Delete symptom of patient
@symptoms.route("/patient-management/views/delete", methods=["DELETE"])
@login_required
def delete_symptom_by_id():
    return delete_symptom_by_id_service()


# Get symptom by User_Email
@symptoms.route("/patient-management/views/<string:user_email>", methods=["GET"])
def get_symptoms_by_patient(user_email):
    return get_symptoms_by_patient_service(user_email)


# Get symptoms of patient
@symptoms.route('/patient/medical_records', methods=['GET'])
@login_required
def get_patient_medical_records_controller():
        return get_patient_medical_records()
        

@symptoms.route('/patient/delete', methods=['POST'])
@login_required
def delete_patient_controller():
    email = request.form.get('email')

    if delete_current_patient(email):
        return render_template("login.html", user=None)
    else:
        return jsonify({'message': 'Không tìm thấy người dùng'})
    

# Update patient_email 
@symptoms.route('/patient/update-email', methods=['POST'])
@login_required
def update_patient_email_controller():
    update_patient_email_service()
    return render_template('setting.html', user=current_user)


# Update patient_password
@symptoms.route('/patient/update-password', methods=['POST'])
@login_required
def update_patient_password_controller():
     update_patient_password_service()
     return render_template('setting.html', user=current_user)


@symptoms.route('/calendar')
@login_required
def event_index():
    return event_index_service()


@symptoms.route('/calendar/insert', methods=["POST"])
@login_required
def event_insert():
    return event_insert_service()


@symptoms.route("/calendar/update", methods=["POST"])
@login_required
def event_update():
    return event_update_service()


@symptoms.route("/calendar/ajax_delete", methods=["POST"])
@login_required
def event_ajax_delete():
    event_ajax_delete_service()
    return render_template('login.html')
