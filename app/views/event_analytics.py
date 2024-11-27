from flask import Blueprint, render_template
from flask_login import current_user, login_required
from app.models import StudentOrganization, EventAnalytics

event_analytics_bp = Blueprint("event_analytics", __name__)


@event_analytics_bp.route("/analytics/<int:organization_id>", methods=["GET"])
@login_required
def view_analytics(organization_id):
    user = current_user
    organization = StudentOrganization.query.filter_by(id=organization_id).first()

    if user.role == "Signatory" and user.signatory in [
        organization.adviser,
        organization.co_adviser,
    ]:
        analytics = EventAnalytics.query.filter_by(
            organization_id=organization_id
        ).all()
        return render_template("analytics.html", analytics=analytics)

    return "Access Denied", 403
