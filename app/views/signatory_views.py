from flask import Blueprint, render_template
from flask_login import login_required, current_user

signatory_bp = Blueprint(
    "signatory", __name__, template_folder="../templates/signatory"
)


@signatory_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    if current_user.role.name != "Signatory":
        return "Access Denied", 403
    return render_template(
        "signatory/signatory.html", role="signatory", user=current_user
    )
