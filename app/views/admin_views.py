from flask import Blueprint, render_template, request

admin_bp = Blueprint("admin", __name__, template_folder="templates/admin")


@admin_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        # Example: Handle submitted organization data
        pass
    return render_template("admin/dashboard.html")
