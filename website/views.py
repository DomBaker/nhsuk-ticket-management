from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Ticket
from . import db

from website.forms import TicketForm, RegisterForm


views = Blueprint("views", __name__)


@views.route("/")
@login_required
def home():
    return render_template("views/home.html")


@views.route("/create_ticket", methods=["GET", "POST"])
@login_required
def create_ticket():
    form = TicketForm()

    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        area_of_business = request.form.get("area_of_business")

        new_ticket = Ticket(
            title=title,
            description=description,
            area_of_business=area_of_business,
            owner=current_user.id,
        )
        db.session.add(new_ticket)
        db.session.commit()
        flash("New ticket created")

        return redirect(url_for("views.create_ticket"))

    return render_template("views/create_ticket.html", form=form)


@views.route("/view_ticket", methods=["GET", "POST"])
@login_required
def view_ticket():
    return render_template("views/view_ticket.html", user=current_user)


@views.route("/profile")
@login_required
def profile():
    form = RegisterForm()

    if request.method == "POST":
        email = request.form.get("email")
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        password = request.form.get("password")
        confirm = request.form.get("confirm")

        if password != confirm:
            flash("Passwords do not match")

    elif request.method == "GET":
        form.email.data = current_user.email
        form.first_name.data = current_user.first_name
        form.last_name.data = current_user.last_name
        


    return render_template("user/profile.html", form=form)
