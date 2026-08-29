<div align="center">

# 🌟 DevMeet - Production-Grade Personal Portfolio & CMS

<img src="app/static/images/stock/Portfolio.webp" alt="DevMeet Portfolio Cover" width="650" style="border-radius: 12px; box-shadow: 0 12px 40px rgba(0,0,0,0.5);" />

### 🚀 **Live Production:** [roshandamor.site](https://roshandamor.site) | [devmeet.rkdapp.site](https://devmeet.rkdapp.site)

![Django](https://img.shields.io/badge/Django-5.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

**A high-performance, responsive personal portfolio CMS and developer showcase platform for Roshan Damor. Built with Django 5.2, TinyMCE, Jazzmin Admin, WhiteNoise, automated WebP media optimization, and complete Schema.org JSON-LD SEO infrastructure.**

</div>

---

## 📑 Table of Contents
1. [Key Features](#-key-features)
2. [Tech Stack & Architecture](#-tech-stack--architecture)
3. [Quick Start & Local Setup](#-quick-start--local-setup)
4. [Environment Configuration](#-environment-configuration)
5. [Database Schema & Models](#-database-schema--models)
6. [Media Optimization Pipeline](#-media-optimization-pipeline)
7. [SEO & Search Engine Optimization](#-seo--search-engine-optimization)
8. [Management Commands](#-management-commands)
9. [Error Pages](#-custom-error-pages)
10. [Automated Testing](#-automated-testing)
11. [Production Deployment](#-production-deployment)
12. [License & Author](#-license--author)

---

## ✨ Key Features

### 🎨 **Frontend & UI/UX Excellence**
- **Futuristic Glassmorphism Aesthetic** - Refined dark palette (`#070b14`, `#0d1322`, `#6366f1`) with glowing borders and subtle micro-interactions.
- **Modular Component Architecture** - Cleanly separated partials (`navbar.html`, `footer.html`, `filters.html`, `resume_modal.html`, `skill_popups.html`, `pagination.html`).
- **Interactive Typewriter Hero** - Custom JavaScript typewriter animation featuring a single focused role title: `Software Engineer`.
- **Dynamic Image Sliders & Tech Grids** - Smooth carousel navigation on project detail pages with interactive feature breakdowns.
- **Glassmorphic Filter Toolbar** - Real-time client-side search, category filter pills, and custom animated sort dropdowns.
- **Custom Error Pages** - Fully responsive, branded error templates for `404`, `500`, `403`, and `400` with quick recovery routes.

### 🔧 **Backend & Core Engineering**
- **Django 5.2 Framework** - Clean Model-View-Template architecture with ORM parameterization.
- **High-Performance Querying** - Relational models leverage `prefetch_related` to completely eliminate N+1 database queries.
- **Automated WebP Image Compression** - Media upload pipeline automatically optimizes and converts uploaded PNG/JPG files to lightweight WebP format.
- **IP-Based Contact Rate Limiting** - Contact form enforces client IP rate limiting (10 submissions/day in production) to prevent spam abuse.
- **Jazzmin Dark Admin CMS** - Tailored Django administration dashboard with inline project images, features, learnings, and TinyMCE rich-text editor.
- **Dynamic Resume Delivery** - Safe PDF file streaming (`/resume/` inline view and `/resume/download/`) with disk existence verification.

### 🛡️ **Security & Production Hardening**
- **Content Security Policy (CSP)** - Configured with `django-csp` to protect against cross-site scripting (XSS) and iframe injection.
- **CSRF Token Verification** - Strict CSRF verification across all AJAX POST contact requests.
- **Input Sanitization & Boundary Capping** - Hard character limits across all form fields (`name[:100]`, `email[:254]`, `subject[:255]`, `message[:5000]`).
- **Dynamic Admin URL** - Configurable admin endpoint path via environment variables to mitigate automated scanner bots.
- **Orphan Media Cleanup** - Integrated `django-cleanup` automatically purges obsolete files when model instances are updated or deleted.

---

## 🛠️ Tech Stack & Architecture

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | Django 5.2 (Python 3.10+) |
| **Databases** | SQLite3 (Development) / MySQL 8.0 (Production) |
| **Static & Media Delivery** | WhiteNoise with Brotli/Gzip compression, Pillow (PIL) WebP engine |
| **Rich Text Editor** | TinyMCE |
| **Admin Dashboard** | Jazzmin Admin (Dark UI Theme) |
| **Frontend Technologies** | Semantic HTML5, Vanilla CSS3 (Custom Design System), Modern ES6+ JavaScript |
| **SEO & Schemas** | JSON-LD (Person, WebSite, SoftwareSourceCode, BlogPosting, FAQPage, BreadcrumbList), XML Sitemaps |
| **Testing** | Django TestCase with isolated temporary media environment |

---

## 🚀 Quick Start & Local Setup

### 1. Clone Repository
```bash
git clone https://github.com/logicbyroshan/devmeet-portfolio.git
cd devmeet-portfolio
```

### 2. Create and Activate Virtual Environment
```bash
# Windows (PowerShell)
python -m venv venv
venv\Scripts\activate

# Linux / macOS
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
```bash
cp .env.example .env
```
*(Optionally modify `.env` values for custom ports, database credentials, or email SMTP).*

### 5. Apply Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. (Optional) Seed Sample Portfolio Data
```bash
python manage.py seed_data
```

### 7. Run Local Development Server
```bash
python manage.py runserver 0.0.0.0:8000
```
Open **[http://127.0.0.1:8000](http://127.0.0.1:8000)** in your web browser.

---

## 🔐 Environment Configuration (`.env`)

| Variable | Default | Description |
| :--- | :--- | :--- |
| `PRODUCTION` | `False` | Toggle between development (SQLite, console email) and production (MySQL, SMTP) |
| `DEBUG` | `True` | Django debug mode flag |
| `SECRET_KEY` | `django-insecure-...` | Secret cryptographic key |
| `ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated list of authorized domains |
| `ADMIN_URL` | `dash-admin/` | Custom administration portal route |
| `DB_NAME` | `portfolio_db` | MySQL database name |
| `DB_USER` | `root` | MySQL user |
| `DB_PASSWORD` | `password` | MySQL password |
| `DB_HOST` | `127.0.0.1` | Database host |
| `DB_PORT` | `3306` | Database port |
| `EMAIL_HOST` | `smtp.gmail.com` | SMTP host for contact messages |
| `EMAIL_HOST_USER` | `contact@roshandamor.site`| Sender email address |
| `EMAIL_HOST_PASSWORD` | `app_password` | SMTP App password |

---

## 📊 Database Schema & Models

```
┌─────────────────┐       ┌─────────────────┐       ┌─────────────────┐
│     Project     │◄──────┤  ProjectImage   │       │      Skill      │
├─────────────────┤1     *├─────────────────┤       ├─────────────────┤
│ title (index)   │       │ image (WebP)    │       │ name (unique)   │
│ categories      │       │ created_at      │       │ level (0-100)   │
│ description     │       └─────────────────┘       │ status          │
│ slug (unique)   │◄──────┐                         │ icon (WebP)     │
│ publication_date│1     *│                         └────────┬────────┘
│ created_at      │       │     Feature     │                │
│ github_link     │       ├─────────────────┤                │
│ live_link       │       │ title           │                │
└────────┬────────┘       │ description     │                │
         │                │ image (WebP)    │                │
         │                └─────────────────┘                │
         │                ┌─────────────────┐                │
         │1              *│    Learning     │                │
         ├───────────────►├─────────────────┤                │
         │                │ paragraph       │                │
         │                └─────────────────┘                │
         │*                                                 *│
         └─────────────────── M2M Relation ──────────────────┘
```

- **`Project`**: Core showcase model supporting image carousels, feature cards, key learnings, and GitHub/Live links (ordered latest-first, 9 per page).
- **`Blog`**: Technical insights with TinyMCE rich text, automatic reading time computation, and cover images (ordered latest-first, 9 per page).
- **`Skill`**: Interactive skill bars with level percentages, status badges, and resource link popups (15 per page).
- **`Experience`**: Career history and company milestones ordered chronologically.
- **`FAQ`**: Curated Q&A section limited to max 6 entries enforced at model and admin layers, seamlessly integrated on the home page.
- **`Resume`**: PDF resume uploads with single active file delivery.
- **`ContactMessage`**: Contact form inquiries with client IP address logging for rate limiting.

---

## 🖼️ Media Optimization Pipeline

All image uploads are automatically intercepted and processed using the `optimize_image_field` helper in [app/models.py](app/models.py):
1. Detects file format (bypasses vectors like `.svg` and documents).
2. Resizes large images using high-fidelity `LANCZOS` downsampling.
3. Automatically converts RGB/RGBA color spaces into optimized `.webp` format (85% quality).
4. Results in **70% to 90% reduction in file size** while maintaining visual quality.

---

## 🔍 SEO & Search Engine Optimization

DevMeet is engineered for top Google ranking across primary target search queries (`roshan`, `roshan damor`, `roshan software engineer`, `roshan uit rgpv`, `roshan damor portfolio`):

1. **Dynamic XML Sitemap (`/sitemap.xml`)**:
   - Indexes all public views plus all individual project and blog detail pages.
2. **Search Engine Crawler Directives (`/robots.txt`)**:
   - Permits complete crawling while disallowing private admin directories.
3. **Structured Data (JSON-LD Schemas)**:
   - `Person` & `WebSite` entity graph (Roshan Damor, UIT RGPV, Indore MP, social channels).
   - `SoftwareSourceCode` schema on project detail pages.
   - `BlogPosting` schema on technical blog articles.
   - `FAQPage` schema for rich snippet Q&A cards in Google search.
   - `BreadcrumbList` navigation across all subpages.
4. **Social Sharing**:
   - Full OpenGraph (`og:`) and Twitter Card (`twitter:`) tags with canonical URLs.

---

## ⚙️ Management Commands

### Optimize Existing Media to WebP
Compresses and converts all existing images in `media/` and `app/static/images/` to WebP:
```bash
python manage.py optimize_all_media
```

### Seed Initial Portfolio Data
Populates the database with skills, projects, blog articles, experiences, and FAQs:
```bash
python manage.py seed_data
```

---

## 🚫 Custom Error Pages

Custom styled error templates matching the dark glassmorphism design:

| HTTP Status | Template | Trigger Condition |
| :--- | :--- | :--- |
| **404 Not Found** | [404.html](app/templates/404.html) | Invalid route or missing project/blog slug |
| **500 Server Error** | [500.html](app/templates/500.html) | Unhandled backend exception or internal crash |
| **403 Forbidden** | [403.html](app/templates/403.html) | Permission denied or CSRF token failure |
| **400 Bad Request** | [400.html](app/templates/400.html) | Malformed HTTP request or invalid parameters |

---

## 🧪 Automated Testing

Exhaustive test suite in [app/tests.py](app/tests.py) covering all views, edge cases, special character queries, rate limiting, and sitemaps:

```bash
python manage.py test
```

### Test Suite Output:
```
Ran 16 tests in 0.563s

OK
Destroying test database for alias 'default'...
```

---

## 🌐 Production Deployment

### 1. Configure Production Settings (`.env`)
```ini
PRODUCTION=True
DEBUG=False
SECRET_KEY=your_long_random_production_secret_key
ALLOWED_HOSTS=roshandamor.site,www.roshandamor.site,devmeet.rkdapp.site
DB_NAME=portfolio_production_db
DB_USER=production_user
DB_PASSWORD=your_secure_db_password
DB_HOST=127.0.0.1
DB_PORT=3306
```

### 2. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 3. Run Production Security Verification
```bash
python manage.py check --deploy
```

---

## 👨‍💻 Author & License

- **Developer:** **Roshan Damor**
- **Degree / College:** University Institute of Technology, RGPV (UIT RGPV Bhopal)
- **Portfolio Website:** [roshandamor.site](https://roshandamor.site)
- **GitHub:** [@logicbyroshan](https://github.com/logicbyroshan)
- **LinkedIn:** [iamroshandamor](https://www.linkedin.com/in/iamroshandamor/)
- **Twitter / X:** [@iamroshandamor](https://x.com/iamroshandamor)

*Licensed under the [MIT License](LICENSE).*
