from flask import Blueprint, render_template

signatory_bp = Blueprint("signatory", __name__, template_folder="templates/signatory")

@signatory_bp.route("/")
def dashboard():
    return render_template("signatory/dashboard.html")
