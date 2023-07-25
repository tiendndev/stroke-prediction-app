from flask import Blueprint, render_template, request, flash, redirect, url_for, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, current_user, logout_user

from .models import User, Note
from . import db

# Khai bao Blueprint
user = Blueprint("user", __name__)


@user.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                # Check life time
                session.permanent = True

                # Luu nguoi dung khi login thanh cong
                login_user(user, remember=True)

                return redirect(url_for("views.dashboard"))
            else:
                flash("Wrong password! Please check again!", category="error")
        else:
            flash("User doesn't exist!", category="error")
    return render_template("login.html", user=current_user)


@user.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        # email, username, password chinh la "name" trong input
        email = request.form.get("email")
        user_name = request.form.get("user_name")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        user = User.query.filter_by(email=email).first()
        # Xac thuc user
        if user:
            flash("User existed!", category="error")
        elif len(email) < 4:
            flash("Email must be greater than 3 characters.")
        elif len(password) < 4:
            flash("Password must be greater than 4 characters.")
        elif password != confirm_password:
            flash("Password does not match!.", category="error")
        else:
            # Ma hoa password de dua vao database
            password = generate_password_hash(password, method="sha256")
            new_user = User(email, password, user_name)
            try:
                db.session.add(new_user)
                db.session.commit()
                # flash("User created!", category="success")

                # Tu dong login sau khi tao tai khoan thanh cong
                # login_user(user, remember=True)
                return redirect(url_for("views.form"))
            except:
                return jsonify({"message": "Error"}), 400

    return render_template("signup.html", user=current_user)


@user.route("/logout")
# Khi login thanh cong moi co logout
@login_required
def logout():
    logout_user()

    # Khi da su dung Blueprint o tren thi phai user.login
    return redirect(url_for("user.login"))