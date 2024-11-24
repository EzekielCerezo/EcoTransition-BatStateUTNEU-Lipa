from flask import Blueprint, render_template, request

signatory_bp = Blueprint("signatory", __name__, template_folder="templates/signatory")


@signatory_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        # Example: Handle submitted organization data
        pass
    return render_template("signatory/dashboard.html")
