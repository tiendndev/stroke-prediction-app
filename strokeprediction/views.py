from flask import Blueprint, jsonify, render_template, flash, request, redirect, url_for
from flask_login import login_required, current_user

from .models import Note, User
from . import db
from strokeprediction.predict import prediction_model
from strokeprediction.RandomForestModel.randomForest import predict_Stroke
from strokeprediction import aiapi

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
@views.route('/dashboard', methods=["GET"])
@login_required
def dashboard():
    return render_template("dashboard.html", user=current_user)


@views.route("/form", methods=["GET", "POST"])
# Login roi moi duoc vao Form Page
@login_required
def form():
    if request.method == "POST":
        user_id = current_user.id
        if (db.session.query(Note.id).filter_by(user_id=user_id).first()):
            flash("Bạn đã nhập dữ liệu rồi!", category="error")
            return redirect(url_for("views.form"))
        # Lay noi dung tu input[name="fullname"],...
        fullname = request.form.get("fullname")
        age = int(request.form.get("age"))
        gender = request.form.get("gender")
        hypertension = request.form.get("hypertension")
        heart_disease = request.form.get("heart_disease")
        ever_married = request.form.get("ever_married")
        residence_type = request.form.get("residence_type")
        work_type = request.form.get("work_type")
        avg_glucose_level = float(request.form.get("avg_glucose_level"))
        bmi = float(request.form.get("bmi"))
        smoking_status = request.form.get("smoking_status")

        # Gender
        gender_Male = 0
        gender_Other = 0
        match gender:
            case "male":
                gender_Male = 1
            case "other":
                gender_Other = 1
        
        # Residence type
        rsd_type = 1 if residence_type == "urban" else 0

        # Work type
        Never_worked = 0
        private = 0
        Self_employed = 0
        children = 0
        match work_type:
            case "private":
                private = 1
            case "self_employed":
                Self_employed = 1
            case "children":
                children = 1
            case "never_worked":
                Never_worked = 1

        # Smoking status
        smoking_status_formerly_smoked = 0
        smoking_status_never_smoked = 0
        smoking_status_smokes = 0
        match smoking_status:
            case "formerly_smoked":
                smoking_status_formerly_smoked = 1
            case "never_smoked":
                smoking_status_never_smoked = 1
            case "smokes":
                smoking_status_smokes = 1

        # BMI
        bmi_cat_Ideal = 0
        bmi_cat_Overweight = 0
        bmi_cat_Obesity = 0
        if bmi >= 19 and bmi < 25:
            bmi_cat_Ideal = 1
        elif 25 <= bmi and bmi < 30:
            bmi_cat_Overweight = 1
        elif 30 <= bmi and bmi <= 1000:
            bmi_cat_Obesity = 1
        
        # Age
        age_cat_Teens = 0
        age_cat_Adults = 0
        age_cat_Mid_Adults = 0
        age_cat_Elderly = 0
        if 13 <= age and bmi < 18:
            age_cat_Teens = 1
        elif 18 <= age and age < 45:
            age_cat_Adults = 1
        elif 45 <= age and age < 60:
            age_cat_Mid_Adults = 1
        elif 60 <= age and age <= 200:
            age_cat_Elderly = 1

        # Average Glucose level
        glucose_cat_Normal = 0
        glucose_cat_High = 0
        glucose_cat_Very_High = 0
        if 90 <= avg_glucose_level and avg_glucose_level < 160:
            glucose_cat_Normal = 1
        elif 160 <= avg_glucose_level and avg_glucose_level < 230:
            glucose_cat_High = 1
        elif 230 <= avg_glucose_level and avg_glucose_level <= 500:
            glucose_cat_Very_High = 1

        strokeInfo = predict_Stroke(age, hypertension, heart_disease, ever_married, rsd_type, avg_glucose_level,
                   bmi, gender_Male, gender_Other, Never_worked, private, Self_employed,
                   children, smoking_status_formerly_smoked, smoking_status_never_smoked, 
                   smoking_status_smokes, bmi_cat_Ideal, bmi_cat_Overweight, bmi_cat_Obesity, age_cat_Teens,age_cat_Adults,
                   age_cat_Mid_Adults, age_cat_Elderly, glucose_cat_Normal, glucose_cat_High, glucose_cat_Very_High)
        stroke = strokeInfo[0]
        percentage = strokeInfo[1]
        print(strokeInfo)

        # Lay data va user_id cua user (xem trong models.py - class user)
        new_note = Note(
            fullname=fullname,
            user_id=current_user.id,
            age=age,
            gender=gender,
            hypertension=hypertension,
            heart_disease=heart_disease,
            ever_married=ever_married,
            residence_type=residence_type,
            work_type=work_type,
            avg_glucose_level=avg_glucose_level,
            bmi=bmi,
            smoking_status=smoking_status,
            stroke=stroke,
            percentageStroke=percentage
        )
        # Them vao databse
        db.session.add(new_note)
        db.session.commit()
        flash("Thêm thành công!", category="success")

    return render_template("form.html", user=current_user)


@views.route("/image", methods=["POST", "GET"])
def VGG16():
    prediction = None
    img_url = None
    if request.method == "POST":
        load_predict = prediction_model()
        prediction = load_predict[0]
        img_url = load_predict[1]

    return render_template("image.html", user=current_user, prediction=prediction, img_url=img_url)


@views.route("/setting", methods=["POST", "GET"])
def setting():
    return render_template("setting.html", user=current_user)


@views.route('/bmi', methods=["GET"])
def bmi():
    return render_template("bmi.html", user=current_user)

