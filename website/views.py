from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from .models import Ticket, User
from . import db

from website.forms import TicketForm


views = Blueprint("views", __name__)


@views.route("/")
def home():
    return render_template("views/home.html")


@views.route("/create_ticket", methods=["GET", "POST"])
@login_required
def create_ticket():
    form = TicketForm()

    if current_user.is_authenticated and request.method == "POST":
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
    if current_user.is_authenticated:
        return render_template("views/view_ticket.html", user=current_user)
    else:
        flash("You aren't allowed to access that page")
        return redirect(url_for("views.home"))


@views.route("/admin_nav_page")
@login_required
def admin_nav_page():
    if current_user.is_authenticated and current_user.is_admin:
        return render_template("views/admin_nav_page.html")
    else:
        flash("You aren't allowed to access that page")
        return redirect(url_for("views.home"))


@views.route("/admin_view_ticket", methods=["GET", "POST"])
@login_required
def admin_view_ticket():
    if current_user.is_authenticated and current_user.is_admin:
        all_tickets = Ticket.query.all()
        return render_template("views/admin_view_ticket.html", tickets=all_tickets)
    else:
        flash("You aren't allowed to access that page")
        return redirect(url_for("views.home"))


@views.route("/admin_view_users", methods=["GET", "POST"])
@login_required
def admin_view_users():
    if current_user.is_authenticated and current_user.is_admin:
        all_users = User.query.all()
        return render_template("views/admin_view_all_users.html", users=all_users)
    else:
        flash("You aren't allowed to access that page")
        return redirect(url_for("views.home"))


@views.route("/admin_delete_user/<int:id>", methods=["GET", "POST"])
@login_required
def admin_delete_user(id):
    user = db.session.query(User).get_or_404(id)

    try:
        db.session.delete(user)
        db.session.commit()
        flash("User deleted by an admin")
        return redirect(url_for("views.admin_view_users", id=id, user=user))

    except BaseException:
        flash("Unable to delete user")

    return redirect(url_for("views.admin_view_users"))


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


@views.route("/complete_ticket/<int:id>", methods=["GET", "POST"])
@login_required
def complete_ticket(id):
    ticket_to_complete = db.session.query(Ticket).get_or_404(id)

    ticket_to_complete.complete = True

    try:
        db.session.commit()
        flash("Marked as complete")
        return redirect(
            url_for(
                "views.admin_view_ticket", id=id, ticket_to_complete=ticket_to_complete
            )
        )

    except BaseException:
        flash("Unable to complete ticket")

    return redirect(url_for("views.admin_view_ticket"))


@views.route("/admin_delete_ticket/<int:id>", methods=["GET", "POST"])
@login_required
def admin_delete_ticket(id):
    ticket_to_delete = db.session.query(Ticket).get_or_404(id)

    try:
        db.session.delete(ticket_to_delete)
        db.session.commit()
        flash("Ticket deleted by an admin")
        return redirect(
            url_for("views.admin_view_ticket", id=id, ticket_to_delete=ticket_to_delete)
        )

    except BaseException:
        flash("Unable to complete ticket")

    return redirect(url_for("views.admin_view_ticket"))
