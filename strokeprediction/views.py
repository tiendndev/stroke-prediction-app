from flask import Blueprint, jsonify, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user

from .models import Note
from . import db
from strokeprediction.predict import prediction_model
from strokeprediction.RandomForestModel.randomForest import predict_Stroke
from strokeprediction import aiapi

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@views.route("/form", methods=["GET", "POST"])
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
        residence_type = request.form.get("residence_type")
        work_type = request.form.get("work_type")
        avg_glucose_level = request.form.get("avg_glucose_level")
        bmi = request.form.get("bmi")
        smoking_status = request.form.get("smoking_status")

        gd = 0 if gender == "male" else 1
        rsd_type = 1 if residence_type == "urban" else 0
        private = 0
        Govt_job = 0
        Self_employed = 0
        children = 0
        Never_worked = 0
        match work_type:
            case "private":
                private = 1
            case "govt_job":
                Govt_job = 1
            case "self_employed":
                Self_employed = 1
            case "children":
                children = 1
            case "never_worked":
                Never_worked = 1

        stroke = predict_Stroke(gd, age, hypertension, heart_desease,
                                ever_married, rsd_type, avg_glucose_level, bmi, private, Govt_job, Self_employed, children, Never_worked)

        # Lay data va user_id cua user (xem trong models.py - class user)
        new_note = Note(
            fullname=fullname,
            user_id=current_user.id,
            age=age,
            gender=gender,
            hypertension=hypertension,
            heart_desease=heart_desease,
            ever_married=ever_married,
            residence_type=residence_type,
            work_type=work_type,
            avg_glucose_level=avg_glucose_level,
            bmi=bmi,
            smoking_status=smoking_status,
            stroke=stroke
        )
        # Them vao databse
        db.session.add(new_note)
        db.session.commit()
        flash("Note added!", category="success")

    return render_template("form.html", user=current_user)


@views.route("/data", methods=["GET", "DELETE"])
def RetrivePatient():
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


@views.route("/chatbot", methods=["GET", "POST"])
def gpt():
    if request.method == 'POST':
        prompt = request.form['prompt']

        res = {}
        res['answer'] = aiapi.generateChatResponse(prompt)
        return jsonify(res), 200
    return render_template("gpt.html", user=current_user, **locals())
