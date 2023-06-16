from flask import Blueprint
from flask_login import login_required

from .services import add_symptom_service, get_all_symptoms_service, delete_symptom_by_id_service, get_symptoms_by_patient_service, get_user_email_by_id_service, get_patient_medical_records

symptoms = Blueprint("symptoms", __name__)


# Add new parameter
@symptoms.route("/patient-management/patient", methods=["POST"])
def add_symptom():
    return add_symptom_service()


# Get all parammeters
@symptoms.route("/patient-management/views", methods=["GET"])
def get_all_symptoms():
    return get_all_symptoms_service()


# Delete parameter
@symptoms.route("/patient-management/delete", methods=["DELETE"])
def delete_symptom_by_id():
    return delete_symptom_by_id_service()


# Get symptom by User_Email
@symptoms.route("/patient-management/views/<string:user_email>", methods=["GET"])
def get_symptoms_by_patient(user_email):
    return get_symptoms_by_patient_service(user_email)


@symptoms.route('/users/<int:user_id>', methods=['GET'])
def get_user_email(user_id):
    return get_user_email_by_id_service(user_id)


@symptoms.route('/patient/medical_records', methods=['GET'])
@login_required
def get_patient_medical_records_controller():
        return get_patient_medical_records()
        