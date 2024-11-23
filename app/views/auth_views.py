from flask import Blueprint, render_template, request, redirect, url_for, flash

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        # Authentication logic
        if username == 'admin' and password == 'password':  # Example credentials
            return redirect(url_for('admin.dashboard'))  # Redirect based on user role
        else:
            flash('Invalid credentials. Please try again.', 'error')
    return render_template('login.html')
