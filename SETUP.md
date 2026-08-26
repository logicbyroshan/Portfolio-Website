# 🛠️ DevMeet Developer Setup & Deployment Guide

This guide outlines detailed instructions for installing, configuring, running, testing, and deploying the DevMeet portfolio project.

---

## 1. Prerequisites
- **Python:** Version 3.10 or higher
- **Package Manager:** `pip`
- **Database:** SQLite3 (included with Python) for development; MySQL 8.0+ for production
- **Version Control:** Git

---

## 2. Local Development Installation

### Step 1: Clone Repository
```bash
git clone https://github.com/logicbyroshan/devmeet-portfolio.git
cd devmeet-portfolio
```

### Step 2: Set Up Virtual Environment
```bash
# Windows PowerShell
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Required Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables
Copy the template file:
```bash
cp .env.example .env
```

Review `.env`:
```ini
PRODUCTION=False
DEBUG=True
SECRET_KEY=your_dev_secret_key
ALLOWED_HOSTS=localhost,127.0.0.1
ADMIN_URL=dash-admin/
```

### Step 5: Initialize Database & Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Step 6: Create Admin Superuser (Optional)
```bash
python manage.py createsuperuser
```

### Step 7: Seed Initial Content (Optional)
```bash
python manage.py seed_data
```

### Step 8: Start Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```
Visit `http://127.0.0.1:8000` in your browser.

---

## 3. Running Automated Tests

Run the complete test suite:
```bash
python manage.py test
```

All 16 unit tests will execute against an isolated temporary media sandbox and in-memory test database.

---

## 4. Production Deployment Guide

### A. Environment Configuration (`.env`)
```ini
PRODUCTION=True
DEBUG=False
SECRET_KEY=generate_a_cryptographically_secure_50_character_key
ALLOWED_HOSTS=roshandamor.site,www.roshandamor.site,devmeet.rkdapp.site
ADMIN_URL=custom-admin-portal/

# MySQL Connection Details
DB_NAME=portfolio_production_db
DB_USER=portfolio_user
DB_PASSWORD=strong_database_password
DB_HOST=127.0.0.1
DB_PORT=3306

# Email SMTP Settings
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=contact@roshandamor.site
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=contact@roshandamor.site

# SSL / HTTPS
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

### B. Static Asset Compilation
```bash
python manage.py collectstatic --noinput
```

### C. Optimize Media Assets
```bash
python manage.py optimize_all_media
```

### D. WSGI / ASGI Execution (Gunicorn Example)
```bash
gunicorn myportfolio.wsgi:application --bind 0.0.0.0:8000 --workers 3
```
