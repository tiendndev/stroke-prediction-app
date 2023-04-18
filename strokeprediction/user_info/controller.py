from flask import Blueprint

from .services import add_symptom_service, get_all_symptoms_service, delete_symptom_by_id_service

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
