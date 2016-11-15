from datetime import datetime
from flask import redirect, render_template, request, session, url_for
from . import main
from flask_login import login_required



@main.route('/', methods=['GET', 'POST'])
@login_required
def index():
    return render_template('main/index.html')
