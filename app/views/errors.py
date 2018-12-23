from app import new_flask_app
from flask import render_template
from app.models import db

@new_flask_app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html.j2'), 404

@new_flask_app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html.j2'), 500
