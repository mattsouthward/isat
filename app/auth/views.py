from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user
from . import auth
from ..models import RadiusUser
from .forms import LoginForm


@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = RadiusUser.query.filter_by(userId=form.loginusername.data).first()
        if user is not None and user.verify_password(form.loginpassword.data) and user.satLvl != 'none':
            login_user(user)
            return redirect(url_for('main.index'))
        flash('Invalid username or password.')
    return render_template('auth/login.html', form=form)
