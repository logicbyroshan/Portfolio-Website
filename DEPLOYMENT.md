# 🚀 DevMeet Portfolio — Deployment & Branching Architecture

This document defines the deployment workflow, environment configuration, SSL reverse proxy integration, and Git branching standard for **[devmeet.logicbyroshan.in](https://devmeet.logicbyroshan.in)**.

---

## 🌿 Git Branching Strategy

| Branch | Role | Deployment Target | Access Policy |
|---|---|---|---|
| `main` | **Production Release Branch** | **Live Production** (`https://devmeet.logicbyroshan.in`) | Protected, deploy-ready code only |
| `dev` | **Development Branch** | **Staging / Local Testing** | Active feature work, experimental fixes |

### Workflow & Release Process:
1. **Daily Development**: Checkout the `dev` branch for all new features, style adjustments, and code changes:
   ```bash
   git checkout dev
   # make changes and verify locally
   git add .
   git commit -m "feat(module): description of changes"
   git push origin dev
   ```
2. **Release to Production**: When features on `dev` are tested and verified (`python manage.py test` passes 100%), merge into `main` and push to trigger production deployment:
   ```bash
   git checkout main
   git merge dev
   git push origin main
   ```

---

## 🔒 Production SSL & Reverse Proxy Configuration

The project is pre-configured to operate behind modern cloud reverse proxies (Nginx, Cloudflare, AWS ALB, Caddy, Render, Railway, DigitalOcean):

```python
# settings.py
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True
USE_X_FORWARDED_PORT = True

# Upload limits (prevent 413 Entity Too Large / RequestDataTooBig)
DATA_UPLOAD_MAX_MEMORY_SIZE = 100 * 1024 * 1024  # 100MB
FILE_UPLOAD_MAX_MEMORY_SIZE = 50 * 1024 * 1024   # 50MB
DATA_UPLOAD_MAX_NUMBER_FIELDS = 2500

if PRODUCTION:
    SECURE_SSL_REDIRECT = os.getenv('SECURE_SSL_REDIRECT', 'True').lower() == 'true'
    SECURE_HSTS_SECONDS = 31536000  # 1 year
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_REFERRER_POLICY = 'same-origin'
```

### 🌐 Production Nginx Server Block (`/etc/nginx/sites-available/devmeet`):
```nginx
server {
    listen 80;
    server_name devmeet.logicbyroshan.in;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl http2;
    server_name devmeet.logicbyroshan.in;

    # CRITICAL: Prevent HTTP 413 (Request Entity Too Large) on large project uploads
    client_max_body_size 100M;

    ssl_certificate /etc/letsencrypt/live/devmeet.logicbyroshan.in/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/devmeet.logicbyroshan.in/privkey.pem;

    location /static/ {
        alias /var/www/devmeet/staticfiles/;
        expires 30d;
        add_header Cache-Control "public, no-transform";
    }

    location /media/ {
        alias /var/www/devmeet/media/;
        expires 7d;
        add_header Cache-Control "public, no-transform";
    }

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_connect_timeout 300s;
        proxy_read_timeout 300s;
    }
}
```

---

## ⚙️ Production Environment Variables (`.env`)

```ini
# Core Django Settings
PRODUCTION=True
DEBUG=False
SECRET_KEY=your-production-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1,devmeet.logicbyroshan.in,.logicbyroshan.in
ADMIN_URL=dash-admin/

# Database Settings (MySQL in Production)
DB_NAME=portfolio_production_db
DB_USER=production_user
DB_PASSWORD=your_strong_password
DB_HOST=127.0.0.1
DB_PORT=3306

# Email Configuration (SMTP)
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False
EMAIL_HOST_USER=contact@logicbyroshan.in
EMAIL_HOST_PASSWORD=your_app_password
DEFAULT_FROM_EMAIL=contact@logicbyroshan.in

# SSL & Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
```

---

## 🛠️ Production Build & Verification Checklist

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```
3. **Collect Static Assets**:
   ```bash
   python manage.py collectstatic --noinput
   ```
4. **Run Unit Tests**:
   ```bash
   python manage.py test
   ```
5. **Start Production WSGI / Gunicorn Server**:
   ```bash
   gunicorn myportfolio.wsgi:application --bind 0.0.0.0:8000 --workers 3
   ```
