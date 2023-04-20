from flask import Blueprint, jsonify, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user

from .models import Note, User
from . import db
from strokeprediction.predict import prediction_model

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@views.route("/form", methods=["GET", "POST"])
# @views.route("/", methods=["GET", "POST"])
# Login roi moi duoc vao Form Page
@login_required
def form():
    if request.method == "POST":
        if (db.session.query(Note.id).filter_by(id=1).first()):
            flash("You submitted data!", category="error")
            return redirect(url_for("views.RetrivePatient"))
        # Lay noi dung tu input[name="fullname"],...
        fullname = request.form.get("fullname")
        age = request.form.get("age")
        gender = request.form.get("gender")
        hypertension = request.form.get("hypertension")
        heart_desease = request.form.get("heart_desease")
        ever_married = request.form.get("ever_married")
        resident_type = request.form.get("resident_type")
        work_type = request.form.get("work_type")
        avg_glucose_level = request.form.get("avg_glucose_level")
        bmi = request.form.get("bmi")
        smoking_status = request.form.get("smoking_status")

        # Lay data va user_id cua user (xem trong models.py - class user)
        new_note = Note(
            fullname=fullname,
            user_id=current_user.id,
            age=age,
            gender=gender,
            hypertension=hypertension,
            heart_desease=heart_desease,
            ever_married=ever_married,
            resident_type=resident_type,
            work_type=work_type,
            avg_glucose_level=avg_glucose_level,
            bmi=bmi,
            smoking_status=smoking_status
        )
        # Them vao databse
        db.session.add(new_note)
        db.session.commit()
        flash("Note added!", category="success")

    return render_template("form.html", user=current_user)


@views.route("/data", methods=["GET", "DELETE", "POST"])
def RetrivePatient():
    if request.method == "POST":
        fullname = request.form.get("fullname")
        age = request.form.get("age")
        gender = request.form.get("gender")
        hypertension = request.form.get("hypertension")
        heart_desease = request.form.get("heart_desease")
        ever_married = request.form.get("ever_married")
        work_type = request.form.get("work_type")
        resident_type = request.form.get("resident_type")
        avg_glucose_level = request.form.get("avg_glucose_level")
        bmi = request.form.get("bmi")
        smoking_status = request.form.get("smoking_status")
        symptom = Note.query.get(1)
        if symptom:
            try:
                if fullname:
                    symptom.fullname = fullname
                elif age:
                    symptom.age = age
                elif gender:
                    symptom.gender = gender
                elif hypertension:
                    symptom.hypertension = hypertension
                elif heart_desease:
                    symptom.heart_desease = heart_desease
                elif ever_married:
                    symptom.ever_married = ever_married
                elif work_type:
                    symptom.work_type = work_type
                elif resident_type:
                    symptom.resident_type = resident_type
                elif avg_glucose_level:
                    symptom.avg_glucose_level = avg_glucose_level
                elif bmi:
                    symptom.bmi = bmi
                elif smoking_status:
                    symptom.smoking_status = smoking_status
                db.session.commit()
            except IndentationError:
                db.session.rollback()
                return jsonify({"message": "Can not update symptom!"}), 400
        else:
            return jsonify({"message": "Not found symptom!"}), 400

    return render_template("views.html", user=current_user)


@views.route("/image", methods=["POST", "GET"])
def VGG16():
    prediction = None
    img_url = None
    if request.method == "POST":
        load_predict = prediction_model()
        prediction = load_predict[0]
        img_url = load_predict[1]

    return render_template("image.html", user=current_user, prediction=prediction, img_url=img_url)
