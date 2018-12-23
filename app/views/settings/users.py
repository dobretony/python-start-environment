from . import settings_blueprint
from flask_login import login_required, current_user
from app.models.user import User
from .users_form import EditProfileForm
from app.models import db

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

@settings_blueprint.route('/user/<username>', methods=('GET', 'POST'))
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('settings/user.html.j2', user=user, posts=posts)

@settings_blueprint.route('/edit_user', methods=('GET', 'POST'))
@login_required
def edit_user():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Your changes have been saved.')
        return redirect(url_for('settings.edit_user'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('settings/edit_user.html.j2', user=user, form=form)
