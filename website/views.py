from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Ticket, User
from . import db

from website.forms import TicketForm


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


@views.route("/admin_nav_page")
@login_required
def admin_nav_page():
    return render_template("views/admin_nav_page.html")


@views.route("/admin_view_ticket", methods=["GET", "POST"])
@login_required
def admin_view_ticket():
    if current_user.is_authenticated and current_user.is_admin:
        all_tickets = Ticket.query.all()

    return render_template("views/admin_view_ticket.html", tickets=all_tickets)


@views.route("/admin_view_users", methods=["GET", "POST"])
@login_required
def admin_view_users():
    if current_user.is_authenticated and current_user.is_admin:
        all_users = User.query.all()

    return render_template("views/admin_view_all_users.html", users=all_users)


@views.route("/delete_ticket/<int:id>", methods=["GET", "POST"])
@login_required
def delete_ticket(id):
    ticket_to_delete = db.session.query(Ticket).get_or_404(id)

    try:
        db.session.delete(ticket_to_delete)
        db.session.commit()
        flash("Ticket deleted")

    except BaseException:
        flash("Unable to delete ticket at this time")

    return render_template("views/view_ticket.html", user=current_user)
