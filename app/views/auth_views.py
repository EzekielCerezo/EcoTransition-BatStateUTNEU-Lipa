from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_bp = Blueprint("auth", __name__, template_folder="templates/auth")


@auth_bp.route("/", methods=["GET", "POST"])
def login():
    return render_template("login.html")
