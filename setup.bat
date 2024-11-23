echo Setting up the environment...

:: Create virtual environment
python -m venv venv

:: Activate virtual environment
call venv\Scripts\activate

:: Install dependencies
pip install -r requirements.txt

echo Setup complete! Virtual environment activated.
