from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    loginusername = StringField('Username', validators=[DataRequired(message="Username is required")])
    loginpassword = PasswordField('Password', validators=[DataRequired(message="Password is required")])
    submit = SubmitField('Log In', validators=[DataRequired()])
