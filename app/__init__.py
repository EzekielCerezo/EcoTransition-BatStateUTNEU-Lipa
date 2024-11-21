"""
Initializes the Flask application and defines the app factory.
"""

from flask import Flask


def create_app():
    """
    Factory function to create and configure the Flask application.
    """
    app = Flask(__name__)

    @app.route("/")
    def home():
        """
        Default route that returns a welcome message.
        """
        return "Hello, EcoTransition!"

    return app
