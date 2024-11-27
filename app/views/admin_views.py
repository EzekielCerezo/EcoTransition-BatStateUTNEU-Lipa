from flask import Blueprint, render_template
from flask_login import login_required, current_user

admin_bp = Blueprint("admin", __name__, template_folder="../templates/admin")


@admin_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    if current_user.role.name != "Admin":
        return "Access Denied", 403
    return render_template("admin/admin.html", role="admin", user=current_user)
