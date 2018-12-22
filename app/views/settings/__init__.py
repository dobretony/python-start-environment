from flask import Blueprint

settings_blueprint = Blueprint('settings', __name__, url_prefix='/settings')

def load_views():
        from app.views.settings.users import user
        print("Loaded settings views in settings blueprint")

load_views()
