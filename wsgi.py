from dotenv import load_dotenv
import os

load_dotenv('.flaskenv')
print("FLASK_ENV from .flaskenv:", os.getenv("FLASK_ENV"))  # Add this line to debug

from app import create_app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
