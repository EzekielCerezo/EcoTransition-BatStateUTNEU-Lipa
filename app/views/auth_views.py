import random
import string
from flask import (
    Blueprint,
    render_template,
    request,
    jsonify,
    flash,
    redirect,
    url_for,
    current_app,
)
from flask_mail import Message
from flask_login import login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from app import db, mail
from app.models import User, Role

# Blueprint setup, template folder path updated
auth_bp = Blueprint("auth", __name__, template_folder="../templates")


# Helper function to generate random credentials
def generate_random_credentials():
    username = "".join(random.choices(string.ascii_letters + string.digits, k=8))
    password = "".join(random.choices(string.ascii_letters + string.digits, k=12))
    return username, password


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")

        current_app.logger.info(f"Login attempt: Email={email}")

        if not email or not password:
            current_app.logger.warning("Validation failed: Missing email or password.")
            flash("Email and password are required", "danger")
            return render_template("login.html")  # Adjusted path

        try:
            user = User.query.filter_by(email=email).first()
            current_app.logger.info(f"User fetched: {user}")

            if user and check_password_hash(user.password, password):
                login_user(user)

                # Fetch role name dynamically
                role = Role.query.get(user.role_id)
                if role:
                    current_app.logger.info(f"User role: {role.name}")

                    # Redirect based on role name
                    role_redirects = {
                        "Admin": "admin.dashboard",
                        "Signatory": "signatory.dashboard",
                        "StudentOrganization": "organization.dashboard",
                        "Guest": "guest.dashboard",
                    }

                    redirect_url = role_redirects.get(role.name)
                    if redirect_url:
                        return redirect(url_for(redirect_url))
                    else:
                        current_app.logger.warning(f"Unknown role: {role.name}")
                        flash("Unknown user role. Please contact support.", "danger")
                else:
                    current_app.logger.error("User role not found in database.")
                    flash("Invalid user role. Please contact support.", "danger")
            else:
                current_app.logger.warning("Invalid email or password.")
                flash("Invalid email or password", "danger")

        except Exception as e:
            current_app.logger.error(f"Error during login: {e}")
            flash("An error occurred. Please try again later.", "danger")

    # Update to the correct template path
    return render_template("login.html")


@auth_bp.route("/guest-continue", methods=["POST"])
def continue_as_guest():
    try:
        current_app.logger.info("Guest continue endpoint hit")
        data = request.json  # Parse the incoming JSON request
        email = data.get("email")

        if not email:
            current_app.logger.warning("No email provided")
            return jsonify({"error": "Email is required"}), 400

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        username, password = generate_random_credentials()
        guest_role = Role.query.filter_by(name="Guest").first()

        if not guest_role:
            current_app.logger.error("Guest role not configured")
            return jsonify({"error": "Guest role not configured."}), 500

        if existing_user:
            current_app.logger.info(f"Existing user found: {existing_user.email}")
            existing_user.password = generate_password_hash(password)  # Update password
            db.session.commit()
            message = "Guest credentials updated and sent to your email."
        else:
            guest_user = User(
                email=email,
                role_id=guest_role.id,
                password=generate_password_hash(password),  # Hash and set password
            )
            db.session.add(guest_user)
            current_app.logger.info(f"New guest user created: {email}")
            message = "Guest credentials sent to your email."
            db.session.commit()

        # Send email with login credentials
        msg = Message(
            "Your Guest Login Credentials",
            recipients=[email],
            body=f"""Welcome to EcoTransition!

Your guest credentials are:
Email: {email}
Password: {password}

Please log in using these credentials.""",
        )
        mail.send(msg)
        current_app.logger.info("Email sent successfully")
        return jsonify({"message": message}), 200

    except Exception as e:
        current_app.logger.error(f"Error in guest-continue (Email Error): {e}")
        db.session.rollback()
        return jsonify({"error": "An internal email error occurred."}), 500


@auth_bp.route("/logout", methods=["GET"])
def logout():
    logout_user()
    flash("Logged out successfully.", "success")
    return redirect(url_for("auth.login"))
