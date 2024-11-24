from flask import Flask
from app.views.auth_views import auth_bp
from app.views.admin_views import admin_bp
from app.views.guest_views import guest_bp
from app.views.organization_views import organization_bp
from app.views.signatory_views import signatory_bp


def create_app():
    app = Flask(__name__)

    # Add secret key for forms and CSRF protection
    app.config["SECRET_KEY"] = "your_secret_key"

    # Debug mode configuration
    app.debug = True
    app.jinja_env.auto_reload = True
    app.config["TEMPLATES_AUTO_RELOAD"] = True

    # Register Blueprints
    app.register_blueprint(auth_bp, url_prefix="/")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(guest_bp, url_prefix="/guest")
    app.register_blueprint(organization_bp, url_prefix="/organization")
    app.register_blueprint(signatory_bp, url_prefix="/signatory")

    return app
