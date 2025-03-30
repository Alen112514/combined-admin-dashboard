
# 🛠️ Django + React Admin Dashboard

This is a full-stack web application built using **Django** (REST API + Auth) and **React** (Admin Dashboard UI). The app allows users to register, log in using OTP verification, manage their profile, and interact with product-related functionality through a modern frontend.

---

## 📁 Project Structure

```
├── client/                # React frontend
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── ...
├── django_task/          # Django backend
│   ├── login/            # Handles user auth and profile logic
│   └── rest_api/         # Placeholder for additional APIs
└── env/                  # Virtual environment (ignored in VCS)
```

---

## ✨ Features

- 🧾 **User Registration with OTP Verification**
- 👤 **Profile Creation and Update**
- 🔐 **Login & Logout**
- 📦 **CRUD operations for Products**
- 📊 **React Admin Dashboard (Material UI + Nivo Charts + Redux)**

---

## 🔧 Technologies Used

### Backend:
- Django
- Django REST Framework (partially scaffolded)
- SQLite (default DB)

### Frontend:
- React 18
- Redux Toolkit
- React Router
- Material UI
- Nivo Charts
- React Datepicker

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x
- Node.js + npm

### Backend Setup

```bash
cd django_task
python -m venv env
source env/bin/activate  # or `env\Scripts\activate` on Windows

pip install -r requirements.txt  # Create this if needed
python manage.py migrate
python manage.py runserver
```

### Frontend Setup

```bash
cd client
npm install
npm start
```

---

## 🌐 Available Routes

These are a few key routes handled by the Django `login` app:

| Endpoint                      | Description           |
|------------------------------|-----------------------|
| `/register/`                 | Register new users    |
| `/otp_verify/`               | OTP verification      |
| `/login/`                    | Login page            |
| `/logout/`                   | Logout user           |
| `/view_profile/`             | View user profile     |
| `/product/`                  | Product list/details  |
| `/product_create/`           | Create new product    |
| `/product_update/<id>/`      | Update product        |
| `/delete/<id>/`              | Delete product        |

---

## 🗃️ Models Example

```python
class Register(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    ...
```

---

## 📌 TODOs / Improvements

- ✅ Add basic API functionality
- 🔲 Full RESTful API integration with `rest_api/`
- 🔲 Add frontend validation
- 🔲 Deploy using Docker or a cloud service (Heroku, Vercel, etc.)

---
