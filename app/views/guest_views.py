from flask import Blueprint, render_template

guest_bp = Blueprint("guest", __name__, template_folder="templates/guest")

@guest_bp.route("/dashboard")
def dashboard():
    return render_template("guest/dashboard.html")
