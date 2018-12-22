from flask import render_template
from flask_login import login_required

def index():
    return render_template('base.html.j2', active_page='index')

def about():
    return render_template('base.html.j2', active_page='about')
