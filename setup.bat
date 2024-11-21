echo Setting up the environment...

:: Create virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

:: Set environment variables
set FLASK_APP=wsgi.py
set FLASK_ENV=development

echo Setup complete! Virtual environment activated.
