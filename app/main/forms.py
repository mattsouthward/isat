from flask_wtf import FlaskForm
from ..models import RadiusUser
from wtforms import PasswordField, SubmitField, validators, StringField, IntegerField, ValidationError, BooleanField, \
    TextAreaField, DateTimeField
from wtforms.validators import DataRequired, Length, Regexp, IPAddress
import re


class SearchForm(FlaskForm):
    username = StringField('username')
    account_number = IntegerField('account_number')
    phone_number = StringField('phone_number')
    last_name = StringField('last_name')
    submit = SubmitField('search')

    def validate_not_blank(self):
        input_list = [self.username.data, self.account_number.data, self.phone_number.data, self.last_name.data]
        if not super(SearchForm, self).validate():
            return False
        for i in input_list:
            if i is not None:
                return True
        msg = "At least one field is required."
        self.username.errors.append(msg)
        return False


class AddUserForm(FlaskForm):
    first_name = StringField('first_name',
                             validators=[DataRequired(message="First name is required")])
    last_name = StringField('last_name',
                            validators=[DataRequired(message="Last name is required")])
    username = StringField('username',
                           validators=[DataRequired(message="Username is required"),
                                       Regexp('^[A-Za-z0-9._]{4,32}$',
                                              message="Username may contain letters, numbers, '_', and '.' only")])
    password = StringField('password',
                           validators=[DataRequired(message="Password is required"),
                                       Length(min=8, max=50, message="Password must be 8 characters or longer")])
    account_number = IntegerField('account_number', validators=[DataRequired(message="Account number is required")])
    company_name = StringField('company_name')
    phone_number = StringField('phone_number', validators=[DataRequired(message="Phone number required")])
    secret_question = StringField('secret_question')
    secret_answer = StringField('secret_question')
    email_account = BooleanField('email_account', default="")
    internet_service = BooleanField('internet_service', default="")
    # isat_role = IntegerField('isat_role', validators=[DataRequired(message='')])
    # radius_static_ip = StringField('radius_static_ip', validators=[IPAddress(message="Invalid IP address format")])
    notes = TextAreaField('notes')
    # creation_date = DateTimeField('creation_date', validators=[DataRequired()])
    submit = SubmitField('Add user')

    def validate_password(self, field):
        digit_missing = re.search(r"\d", field.data) is None
        uppercase_missing = re.search(r"\d", field.data) is None
        lowercase_missing = re.search("\d", field.data) is None
        symbol_missing = re.search("\d", field.data) is None
        password_ok = not (digit_missing or uppercase_missing or lowercase_missing or symbol_missing)
        if not password_ok:
            raise ValidationError('Password must contain at least one of each:\n'
                                  '- lowercase letter\n'
                                  '- uppercase letter\n'
                                  '- digit\n'
                                  '- special character (ex. !, @, #, %, *, ?, ...)')

    def validate_username(self, field):
        if RadiusUser.query.filter_by(username=field.data).first():
            raise ValidationError("Username is already in use")