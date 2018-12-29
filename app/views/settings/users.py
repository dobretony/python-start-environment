from . import settings_blueprint
from flask_login import login_required, current_user
from app.models.user import User
from app.models.comment import Comment
from .users_form import EditProfileForm
from app.models import db
from app import new_flask_app

from flask import (
    Blueprint, flash, redirect, render_template, request, session, url_for
)

@settings_blueprint.route('/user/<username>', methods=('GET', 'POST'))
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    page = request.args.get('page', 1, type=int)
    posts = user.comments.order_by(Comment.timestamp.desc()).paginate(
        page, new_flask_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('settings.user', username=user.username, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('settings.user', username=user.username, page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('settings/user.html.j2', user=user, posts=posts.items,
                            next_url=next_url, prev_url=prev_url)

@settings_blueprint.route('/edit_user', methods=('GET', 'POST'))
@login_required
def edit_user():
    form = EditProfileForm(current_user.username)
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
