from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, validators
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    loginemail = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
    loginpassword = PasswordField('password', validators=[validators.DataRequired(message="Password is required")])
    submit = SubmitField('submit', validators=[validators.DataRequired()])
