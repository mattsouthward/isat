from datetime import datetime
from flask import flash, redirect, render_template, request, session, url_for
from flask_login import login_required
from . import main
from .forms import SearchForm, AddUserForm
from .. import db
from ..models import RadiusUser

from flask import session
from ..models import RadiusUser


@main.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    search_terms = {}
    if form.validate_on_submit():
        for field_name, field_value in form.data.items():
            if field_value and field_name != 'submit':
                search_terms[field_name] = field_value
        if not search_terms:
            flash("At lease one field is required", "error")
    return render_template('main/search.html', form=form)



@main.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    form = AddUserForm()
    if form.validate_on_submit():
        user = RadiusUser(username=form.username.data,
                          password=form.password.data,
                          first_name=form.first_name.data,
                          last_name=form.last_name.data,
                          account_number=form.account_number.data,
                          company_name=form.company_name.data,
                          phone_number=form.phone_number.data,
                          secret_question=form.secret_question.data,
                          secret_answer=form.secret_answer.data,
                          email_account=form.email_account.data,
                          internet_service=form.internet_service.data,
                          notes=form.notes.data
                          )
        db.session.add(user)
        db.session.commit()
        flash("User added", "info")
        return redirect(url_for('main.search'))
    return render_template('main/add_user.html', form=form)


@main.route('/archived_user', methods=['GET', 'POST'])
@login_required
def archived_users():
    return render_template('main/index.html')


@main.route('/whos_online', methods=['GET', 'POST'])
@login_required
def whos_online():
    return render_template('main/index.html')


@main.route('/log_search', methods=['GET', 'POST'])
@login_required
def log_search():
    return render_template('main/index.html')


@main.route('/nas_stats', methods=['GET', 'POST'])
@login_required
def nas_stats():
    return render_template('main/index.html')