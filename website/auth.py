from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from website.forms import RegisterForm, LoginForm

auth = Blueprint("auth", __name__)


@auth.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        user = User.query.filter_by(email=email).first()

        if user:
            flash("This email is already in use, please login")
        elif first_name.isnumeric():
            flash("First name cannot be numeric", category="error")
        elif last_name.isnumeric():
            flash("Last name cannot be numeric", category="error")
        elif password != confirm:
            flash("Passwords do not match", category="error")
        else:
            user = User(
                email=email,
                first_name=first_name,
                last_name=last_name,
                password=generate_password_hash(password, method="sha256"),
            )
            db.session.add(user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account Created")
            return redirect(url_for("views.home"))

    return render_template("auth/register.html", form=form, user=current_user)


@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        user = User.query.filter_by(email=email).first()

        if user:
            if check_password_hash(user.password, password):
                flash("Logged in Successfully", category="success")
                login_user(user, remember=True)
                return redirect(url_for("views.home"))
            else:
                flash("The email or password is incorrect")
        else:
            flash("User does not exist, please sign up")

    return render_template("auth/login.html", form=form, user=current_user)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    flash("Logout Successful")
    return redirect(url_for("auth.login"))
