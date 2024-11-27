from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user
from app import db

# Blueprint for CLI commands
custom_cli = Blueprint("custom", __name__)


# CLI commands
@custom_cli.cli.command("create-db")
def create_db():
    """Create the database."""
    db.create_all()
    print("Database created!")


@custom_cli.cli.command("drop-db")
def drop_db():
    """Drop the database."""
    db.drop_all()
    print("Database dropped!")


@custom_cli.cli.command("seed-db")
def seed_db():
    """Seed the database with initial data."""
    from seed import app

    with app.app_context():
        exec(open("seed.py").read())
    print("Database seeded!")


# Blueprint for routing
main_bp = Blueprint("main", __name__)


# Routes for user interfaces
@main_bp.route("/")
def index():
    # Redirect to login page if not authenticated
    if not current_user.is_authenticated:
        return redirect(url_for("main.login"))
    # Redirect to dashboards based on user role
    if current_user.role == "Admin":
        return redirect(url_for("main.admin_dashboard"))
    elif current_user.role == "Signatory":
        return redirect(url_for("main.signatory_dashboard"))
    elif current_user.role == "StudentOrganization":
        return redirect(url_for("main.organization_dashboard"))
    elif current_user.role == "Guest":
        return redirect(url_for("main.guest_dashboard"))


@main_bp.route("/login")
def login():
    # Render login page
    return render_template("login.html")


@main_bp.route("/admin")
@login_required
def admin_dashboard():
    if current_user.role == "Admin":
        return render_template("admin/admin.html")
    return "Access Denied", 403


@main_bp.route("/signatory")
@login_required
def signatory_dashboard():
    if current_user.role == "Signatory":
        return render_template("signatory/signatory.html")
    return "Access Denied", 403


@main_bp.route("/organization")
@login_required
def organization_dashboard():
    if current_user.role == "StudentOrganization":
        return render_template("organization/organization.html")
    return "Access Denied", 403


@main_bp.route("/guest")
@login_required
def guest_dashboard():
    if current_user.role == "Guest":
        return render_template("guest/guest.html")
    return "Access Denied", 403
