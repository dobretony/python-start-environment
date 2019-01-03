from flask import render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from flask_babel import _
from app import new_flask_app
from app.views.forms import CommentForm
from app.models.comment import Comment
from app.models import db

@new_flask_app.route('/index', methods=['GET', 'POST'])
@new_flask_app.route('/', methods=['GET', 'POST'])
def index():
    if current_user.is_anonymous:
        return render_template("index.html.j2", title='Home Page')
    form = CommentForm()
    if form.validate_on_submit():
        post = Comment(body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash(_('Your comment is now live!'))
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = current_user.followed_posts().paginate(
        page, new_flask_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template("index.html.j2", title='Home Page', form=form,
                           posts=posts.items, next_url=next_url, prev_url=prev_url)

@new_flask_app.route('/explore')
@login_required
def explore():
    page = request.args.get('page', 1, type=int)
    posts = Comment.query.order_by(Comment.timestamp.desc()).paginate(
        page, new_flask_app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('explore', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('explore', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('explore.html.j2', title='Explore', posts=posts.items,
                            next_url=next_url, prev_url=prev_url)

@new_flask_app.route('/about')
def about():
    return render_template('about.html.j2', active_page='about')
