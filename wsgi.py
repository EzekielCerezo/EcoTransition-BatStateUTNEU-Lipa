from dotenv import load_dotenv
import os

# Load .flaskenv for Flask-specific variables
load_dotenv('.flaskenv')

from app import create_app

# Initialize Flask app with centralized configuration
app = create_app()

if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_ENV") == "development")
