from flask import Blueprint, render_template

organization_bp = Blueprint("organization", __name__, template_folder="templates/organization")

@organization_bp.route("/")
def dashboard():
    return render_template("organization/dashboard.html")
