Markdown
# 🎬 Movie Ticket Booking System (Backend)

A robust Django-based REST API designed for managing movie theater bookings. This project was developed as part of a backend developer assignment, focusing on database modeling, admin management, and API structure.

## 🚀 Features
- **Movie Management:** Add, edit, and delete movie listings (Title, Genre, Release Date, etc.).
- **Ticket Booking Logic:** Models for handling ticket reservations and seat tracking.
- **Admin Dashboard:** Fully functional Django Admin interface for backend management.
- **API Ready:** Structured with Django REST Framework for future frontend integration.

## 🛠️ Tech Stack
- **Backend:** Python 3.x, Django 4.2+
- **Database:** SQLite (Development)
- **API Tools:** Django REST Framework
- **Environment:** Virtualenv for dependency management

## 📂 Project Structure
- `bookings/`: Core application containing models, views, and serializers.
- `backend_ticket_booking/`: Main project configuration and settings.
- `requirements.txt`: List of all necessary Python packages.
- `Design_Doc.pdf`: Detailed system architecture and logic flow.

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/kavya0000/ticket-booking-backend.git](https://github.com/kavya0000/ticket-booking-backend.git)
   cd ticket-booking-backend
Create and Activate Virtual Environment:

Bash
python -m venv venv
# On Windows:
venv\Scripts\activate
Install Dependencies:

Bash
pip install -r requirements.txt
Run Migrations:

Bash
python manage.py migrate
Start the Server:

Bash
python manage.py runserver
👤 Admin Access
To access the admin panel at /admin/, use the superuser credentials created during setup (or create a new one using python manage.py createsuperuser).


---
