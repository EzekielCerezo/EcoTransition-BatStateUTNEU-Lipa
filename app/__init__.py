from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from dotenv import load_dotenv
import os

# Load environment variables from `.env`
load_dotenv()

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__)

    # Load configuration from `instance/config.py`
    app.config.from_object("instance.config.Config")

    # Initialize extensions with the app instance
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    mail.init_app(app)

    # Configure login behavior
    login_manager.login_view = "auth.login"
    login_manager.login_message = "Please log in to access this page."
    login_manager.login_message_category = "info"

    # Define `user_loader` for Flask-Login
    from app.models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    from app.routes import custom_cli
    from app.views.guest_views import guest_bp
    from app.views.organization_views import organization_bp
    from app.views.signatory_views import signatory_bp  # Ensure this works
    from app.views.admin_views import admin_bp
    from app.views.auth_views import auth_bp

    app.register_blueprint(custom_cli, cli_group="custom")
    app.register_blueprint(guest_bp, url_prefix="/guest")
    app.register_blueprint(organization_bp, url_prefix="/organization")
    app.register_blueprint(signatory_bp, url_prefix="/signatory")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(auth_bp, url_prefix="/auth")

    # Default route
    @app.route("/")
    def index():
        return redirect(url_for("auth.login"))

    # Register models and ensure tables are created during app initialization
    with app.app_context():
        from app.models import Signatory, StudentOrganization, Role

        db.create_all()

    return app
