from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from jinja2.exceptions import TemplateNotFound
from datetime import datetime

guest_bp = Blueprint("guest", __name__, template_folder="../templates/guest")

# Define status colors
status_colors = {
    "IN PROGRESS": "green",
    "APPROVED": "blue",
    "DISAPPROVED": "red",
}

# Dummy database of documents
documents = [
    {
        "id": 1,
        "title": "Document 1",
        "status": "IN PROGRESS",
        "uploader": "User A",
        "deadline": "2024-12-01",
    },
    {
        "id": 2,
        "title": "Document 2",
        "status": "APPROVED",
        "uploader": "User B",
        "deadline": "2024-11-30",
    },
    {
        "id": 3,
        "title": "Document 3",
        "status": "DISAPPROVED",
        "uploader": "User C",
        "deadline": "2024-11-29",
    },
]


@guest_bp.route("/", methods=["GET"])
@login_required
def dashboard():
    if current_user.role.name != "Guest":
        return "Access Denied", 403
    return render_template("guest/guest.html", role="guest", user=current_user)


@guest_bp.route("/api/documents", methods=["GET"])
@login_required
def get_documents():
    documents_with_colors = [
        {
            "id": doc["id"],
            "title": doc["title"],
            "status": doc["status"],
            "color": status_colors.get(doc["status"], "green"),
            "uploader": doc["uploader"],
            "deadline": datetime.strptime(doc["deadline"], "%Y-%m-%d").strftime(
                "%b %d, %Y"
            ),
        }
        for doc in documents
    ]
    return jsonify(documents_with_colors)


@guest_bp.route("/api/render-template/<template_name>", methods=["POST"])
@login_required
def render_template_with_data(template_name):
    try:
        data = request.json
        return render_template(f"{template_name}.html", **data)
    except TemplateNotFound:
        return jsonify({"error": f"Template '{template_name}' not found"}), 404
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500


@guest_bp.route("/api/upload-document", methods=["POST"])
@login_required
def upload_document():
    new_document = request.json
    new_document["status"] = "IN PROGRESS"
    new_document["color"] = status_colors["IN PROGRESS"]
    new_document["id"] = len(documents) + 1
    documents.append(new_document)
    return (
        jsonify(
            {"message": "Document uploaded successfully", "document": new_document}
        ),
        201,
    )
