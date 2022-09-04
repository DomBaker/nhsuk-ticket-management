from unittest import TestCase
from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField, BooleanField,
                     RadioField, EmailField, PasswordField)
from wtforms import validators 
from wtforms.widgets import PasswordInput

class RegisterForm(FlaskForm):
    email = EmailField('Email Address')
    first_name = StringField('First name', [validators.DataRequired()])
    last_name = StringField('Last name', [validators.DataRequired()])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

class LoginForm(FlaskForm):
    email = EmailField('Email Address')
    password = PasswordField('Password', [validators.DataRequired()])

class TicketForm(FlaskForm):
    title = StringField('Title', [validators.DataRequired()])
    description = TextAreaField('Description', [validators.DataRequired()])