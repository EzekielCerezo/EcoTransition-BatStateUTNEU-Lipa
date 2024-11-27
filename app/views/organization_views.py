from flask import Blueprint, render_template
from flask_login import login_required, current_user

organization_bp = Blueprint(
    "organization", __name__, template_folder="../templates/organization"
)


@organization_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    if current_user.role.name != "StudentOrganization":
        return "Access Denied", 403
    return render_template(
        "organization/organization.html", role="student_org", user=current_user
    )
