
# Wedding Planner Django Project

This is a Django-based wedding planner web application. Follow the steps below to set up and run the project on your local machine.

## Requirements

- Python 3.8 or higher
- Django 5.1.3 (or the version you are using)
- Virtual Environment (recommended but optional)

## Setup Instructions

### 1. Extract the ZIP file
Extract the contents of this ZIP file to a folder of your choice.

### 2. Set up the virtual environment (recommended)
```bash
python -m venv env
```

### 3. Activate the virtual environment
For **Windows**:
```bash
env\Scripts\activate
```

For **Mac/Linux**:
```bash
source env/bin/activate
```

### 4. Install dependencies
If `requirements.txt` is available:
```bash
pip install -r requirements.txt
```
If `requirements.txt` is not available, install Django manually:
```bash
pip install django
```

### 5. Run migrations (optional)
Run Django's migrations to set up the database:
```bash
python manage.py migrate
```

### 6. Run the server
Start the Django development server:
```bash
python manage.py runserver
```

The server will run at:
```
http://127.0.0.1:8000/
```

### 7. Stopping the server
To stop the server, press `CTRL+C` in your terminal/command prompt.

### Troubleshooting:
- If you encounter any issues with missing packages or dependencies, make sure to check the `requirements.txt` file or install packages manually using `pip`.
- Ensure you're using the correct Python version for compatibility.

---

## Project Details

- **Django Version**: 5.1.3
- **Python Version**: 3.x.x (Ensure compatibility)


