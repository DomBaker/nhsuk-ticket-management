from unicodedata import category
from flask import Blueprint, render_template, request, flash, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

from website.forms import RegisterForm, LoginForm

@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        password = request.form.get('password')
        confirm = request.form.get('confirm')

        current_user = User.query.filter_by(email=email).first()
        if current_user:
            flash('This email is already in use, please login')
        elif first_name.isnumeric():
            flash('First name cannot be numeric', category='error')
        elif last_name.isnumeric():
            flash('Last name cannot be numeric', category='error')
        elif password != confirm:
            flash('Passwords do not match', category='error')
        else:
            a_user = User(email=email, first_name=first_name, last_name=last_name, password=generate_password_hash(password, method='sha256'))
            db.session.add(a_user)
            db.session.commit()
            flash('Account Created')
            return redirect(url_for('views.home'))

    return render_template('auth/register.html', form=form)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'Post':
        email = request.form.get('email')
        password = request.form.get('password')

        current_user = User.query.filter_by(email=email).first()

        if current_user:
            if check_password_hash(current_user.password, password):
                flash('Logged in Successfully', category='success')
            else:
                flash('The email or password is incorrect')
        else:
            flash('User does not exist, please sign up')


    return render_template('auth/login.html', form=form)

@auth.route('/logout')
def logout():
    pass
