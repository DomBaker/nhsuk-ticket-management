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
            validators.EqualTo("confirm", message="Passwords must match"),
        ],
    )
    confirm = PasswordField("Repeat Password")


class LoginForm(FlaskForm):
    email = EmailField("Email Address")
    password = PasswordField("Password", [validators.DataRequired()])


class TicketForm(FlaskForm):
    title = StringField("Title", [validators.DataRequired()])
    description = TextAreaField("Description", [validators.DataRequired()])
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
