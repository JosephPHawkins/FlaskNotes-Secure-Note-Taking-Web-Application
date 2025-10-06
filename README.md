# FlaskNotes – Secure Note-Taking Web Application

[![Python](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/)  
[![Flask](https://img.shields.io/badge/flask-2.3-green)](https://flask.palletsprojects.com/)  
[![License](https://img.shields.io/badge/license-MIT-orange)](LICENSE)

---

## Project Overview
**FlaskNotes** is a secure, full-stack web application that allows users to **register, log in, create, view, and manage personal notes**. Built with **Flask**, **SQLAlchemy**, and **Bootstrap 5**, this project demonstrates practical skills in **Python web development, database management, user authentication, and responsive UI design**.  



---

## Key Features
- **User Authentication**: Secure sign-up, login, and logout with hashed passwords  
- **CRUD Notes**: Create, view, and delete personal notes  
- **Responsive Design**: Mobile-friendly UI with Bootstrap 5  
- **Flash Messages**: Real-time feedback for user actions  
- **Database Integration**: SQLite database managed with SQLAlchemy ORM  
- **Secure Access**: Users can only access their own notes  

---

## Technologies Used
- **Backend:** Python, Flask, Flask-Login, SQLAlchemy  
- **Frontend:** HTML5, CSS3, Bootstrap 5, JavaScript  
- **Database:** SQLite  
- **Tools:** Jinja2 templating, Git & GitHub  

---

## Installation & Setup
1. **Clone the repository**
```bash
git clone https://github.com/yourusername/FlaskNotes.git
cd FlaskNotes

    Create a virtual environment

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

    Install dependencies

pip install -r requirements.txt

    Run the application

python run.py

    Open your browser

http://127.0.0.1:5000



Add Notes:
Future Improvements

    Add note editing functionality

    Implement search and filter notes

    Deploy to Heroku / AWS for live demo

    Add rich-text editor for notes

