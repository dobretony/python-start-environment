from . import settings_blueprint
from flask_login import login_required
from app.models.user import User

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

@settings_blueprint.route('/user/<username>', methods=('GET', 'POST'))
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('settings/user.html.j2', user=user, posts=posts)
