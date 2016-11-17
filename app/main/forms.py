from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, validators, StringField, IntegerField
from wtforms.fields.html5 import EmailField

# class LoginForm(FlaskForm):
#     loginemail = EmailField('email', validators=[validators.DataRequired(), validators.Email()])
#     loginpassword = PasswordField('password', validators=[validators.DataRequired(message="Password is required")])
#     submit = SubmitField('submit', validators=[validators.DataRequired()])


class SearchForm(FlaskForm):
    username = StringField('username')
    account_number = IntegerField('account_number')
    phone_number = StringField('phone_number')
    last_name = StringField('last_name')
    submit = SubmitField('search', validators=[validators.DataRequired()])

    def validate(self):
        input_list = [self.username.data, self.account_number.data, self.phone_number.data, self.last_name.data]
        if not super(SearchForm, self).validate():
            return False
        if not input_list:
            msg = "At least one field is required."
            self.username.errors.append(msg)
            return False
        return True
