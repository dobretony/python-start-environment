from flask import Blueprint

auth_blueprint = Blueprint('auth', __name__, url_prefix='/auth')

def load_views():
        from app.views.authentication.auth import login
        from app.views.authentication.auth import logout
        from app.views.authentication.auth import register
        print("Loaded Views")

load_views()
