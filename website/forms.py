from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, EmailField, PasswordField
from wtforms import validators


# This form can be reused for updating the profile
class RegisterForm(FlaskForm):
    email = EmailField("Email Address")
    first_name = StringField("First name", [validators.DataRequired()])
    last_name = StringField("Last name", [validators.DataRequired()])
    password = PasswordField(
        "New Password",
        [
            validators.DataRequired(),
            validators.Length(min=8, max=100),
            validators.EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Repeat Password")


class LoginForm(FlaskForm):
    email = EmailField("Email Address")
    password = PasswordField("Password", [validators.DataRequired(), validators.Length(min=8, max=100)])


class TicketForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired(), validators.Length(min=5, max=100)])
    description = TextAreaField("Description", [validators.DataRequired(), validators.Length(min=10, max=1500)])
    area_of_business = SelectField(
        "Area of Business",
        choices=[
            ("HR", "HR"),
            ("Development", "Development"),
            ("Delivery", "Delivery"),
            ("Product", "Product"),
            ("Tech Support", "Tech Support"),
        ],
        validate_choice=True,
    )
