from flask import Blueprint, render_template
from flask_login import login_required, current_user

from website.forms import TicketForm


views =  Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template('views/home.html')

@views.route('/create_ticket')
@login_required
def create_ticket():
    form = TicketForm()

    return render_template('views/create_ticket.html', form=form)

@views.route('/profile')
@login_required
def profile():
    return render_template('user/profile.html')