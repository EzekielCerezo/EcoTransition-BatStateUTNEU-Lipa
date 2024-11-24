from flask import Blueprint, render_template, request

organization_bp = Blueprint(
    "organization", __name__, template_folder="templates/organization"
)


@organization_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        # Example: Handle submitted organization data
        pass
    return render_template("organization/dashboard.html")
