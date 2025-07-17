# 📝 Personal Task Tracker

A full-stack web application that allows users to manage their personal to-do tasks. Built using **Django**, **PostgreSQL**, and **vanilla HTML/CSS/JavaScript**.

---

## 🚀 Features

- 🔐 User Authentication (Register, Login, Logout)
- 📋 Task Management with CRUD functionality
- 📅 Fields: Title, Description, Due Date, Status (Pending, In Progress, Completed)
- 🧠 Input validation on both client and server sides
- 📌 Tasks sorted by creation date (newest first)
- 🧾 Admin panel for managing users and tasks
- 🎨 Responsive UI built with Bootstrap and custom CSS
- 📍 RESTful endpoints for backend integration (optional/extendable)

---

## 🧱 Tech Stack

| Layer     | Technology              |
|-----------|--------------------------|
| Backend   | Django (Python)          |
| Frontend  | HTML, CSS, JavaScript    |
| Database  | PostgreSQL               |
| Styling   | Bootstrap 5, Custom CSS  |
| Auth      | Django Auth system       |
| Admin     | Django Admin             |

---

## 📁 Project Structure
tasktracker/
├── accounts/ # Handles user registration/login/logout
├── tasks/ # Handles task models and CRUD views
├── templates/ # HTML templates
│ ├── register.html
│ ├── login.html
│ ├── dashboard.html
│ ├── task_form.html
├── static/
│ ├── css/
│ │ └── style.css
│ └── js/
│ └── main.js
├── tasktracker/ # Project settings and root URLs
├── manage.py
└── README.md


---

## 📦 Setup Instructions

### 1. Clone the Repository
git clone https://github.com/<your-username>/personal-task-tracker.git
cd personal-task-tracker

### 2. Set Up Virtual Environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows


### 3. Install Dependencies 
pip install -r requirements.txt

If requirements.txt is not present, install manually: pip install django psycopg2

### 4. Configure PostgreSQL Database 

In tasktracker/settings.py, update the database config:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


### 5. Apply Migrations

python manage.py makemigrations
python manage.py migrate

### 6. Create Superuser

python manage.py createsuperuser

### 7. Run the Server

python manage.py runserver
