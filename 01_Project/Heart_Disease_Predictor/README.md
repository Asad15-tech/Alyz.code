# Heart Disease Predictor

A Django-based web application for predicting heart disease risk using machine learning.

## Features

- Heart disease risk prediction using machine learning
- User-friendly web interface
- Blog system for health-related articles
- About page with mission information
- Admin interface for managing content

## Technology Stack

- Python 3.x
- Django
- Scikit-learn
- Bootstrap
- SQLite

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Asad15-tech/Heart_Disease_Predictor.git
cd Heart_Disease_Predictor
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install required packages:
```bash
cd Heart_Disease_Pred
pip install django scikit-learn numpy pandas
```

4. Apply database migrations:
```bash
python manage.py migrate
```

5. Create a superuser (for admin access):
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

7. Visit http://127.0.0.1:8000/ in your browser

## Project Structure

- `Heart_Disease_Pred/` - Main Django project directory
- `Heart_app/` - Django application containing the main functionality
- `templates/` - HTML templates
- `best_heart_disease_model.pkl` - Trained machine learning model

## Usage

1. Access the main page to make predictions
2. Use the admin interface (http://127.0.0.1:8000/admin/) to manage blog posts and about page content
3. View health-related articles in the blog section
4. Learn about the project in the about section

## Author

- **Asad Ali**
- Email: asadalyy834@gmail.com

## License

This project is licensed under the MIT License - see the LICENSE file for details