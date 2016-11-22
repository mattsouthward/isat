from flask import render_template, redirect, request, url_for, flash
from flask_login import login_user, current_user, logout_user, login_required
from . import auth
from ..models import RadiusUser
from .forms import LoginForm


@auth.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.search'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = RadiusUser.query.filter_by(username=form.loginusername.data).first()
            if user is not None and user.get_password(form.loginpassword.data) and user.satLvl != 'none':
                login_user(user)
                return redirect(url_for('main.search'))
            flash('Invalid username or password.')
        return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.index'))
