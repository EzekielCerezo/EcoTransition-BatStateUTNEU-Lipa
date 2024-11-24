from flask import Blueprint, render_template, request, session

guest_bp = Blueprint("guest", __name__, template_folder="templates/guest")


@guest_bp.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    if request.method == "POST":
        # Handle form submissions or actions
        # Example: Handle document upload (to be added later)
        pass
    return render_template("guest/dashboard.html")
