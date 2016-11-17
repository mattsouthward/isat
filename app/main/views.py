from datetime import datetime
from flask import redirect, render_template, request, session, url_for
from . import main
from flask_login import login_required
from .forms import SearchForm


@main.route('/search', methods=['GET', 'POST'])
@login_required
def search():
    form = SearchForm()
    if form.validate():
        pass
    else:
        return render_template('main/index.html', form=form)



@main.route('/add_user', methods=['GET', 'POST'])
@login_required
def add_user():
    return render_template('main/index.html')


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