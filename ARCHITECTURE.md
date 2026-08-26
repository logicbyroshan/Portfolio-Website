# 🏛️ DevMeet Technical Architecture & Design Document

## 1. System Overview
**DevMeet** is designed with high modularity, strong security posture, automated image optimization, and rich SEO structured data.

```
[ Client Browser / Googlebot ]
           │
           ▼
[ WhiteNoise Static / Media Engine ]
           │
           ▼
[ Django 5.2 Application Layer ]
   ├── URL Routing & Error Handlers (404, 500, 403, 400)
   ├── Views Layer (Prefetched Querysets, Q-Filters, Rate Limits)
   ├── Template System (Base Template + Modular Partials)
   └── Automated WebP Media Pipeline (Pillow LANCZOS)
           │
           ▼
[ Database Layer: SQLite (Dev) / MySQL (Prod) ]
```

---

## 2. Design System Tokens (`app/static/css/style.css`)

The UI is built on a custom design token architecture without third-party utility bloat:

```css
:root {
    --primary-color: #6366f1;       /* Indigo Accent */
    --accent-color: #10b981;        /* Emerald Active Glow */
    --body-color: #070b14;          /* Deep Space Blue Background */
    --container-color: #0d1322;     /* Card Glass Container */
    --heading-text-color: #ffffff;  /* Primary High-Contrast Text */
    --secondary-text-color: #94a3b8;/* Subtitle Slate Gray */
    --border-radius-card: 10px;     /* Crisp Sharp-Corner Radius */
    --border-radius-btn: 6px;       /* Crisp Button Radius */
}
```

---

## 3. Template Component Architecture

Templates are strictly divided into reusable partials:

- `app/templates/portfolio-base.html`: Main HTML shell containing global `<head>`, SEO metadata, Google JSON-LD schema, navigation, footer, and JavaScript initialization.
- `app/templates/components/navbar.html`: Desktop and mobile drawer navigation with glowing active page indicator.
- `app/templates/components/footer.html`: Brand typography, quick links, social channels, and dynamic typewriter animation.
- `app/templates/components/filters.html`: Glassmorphic search input, custom animated sort dropdown, and category tags.
- `app/templates/components/resume_modal.html`: Accessible PDF preview modal.
- `app/templates/components/skill_popups.html`: Resource link detail overlays.
- `app/templates/404.html`, `500.html`, `403.html`, `400.html`: Custom error handlers.

---

## 4. Query & Performance Optimization

1. **N+1 Query Elimination**:
   - `Project.objects.prefetch_related('images', 'skills', 'features', 'learnings')`
2. **Optimized Category Extraction**:
   - `get_unique_categories` executes direct database `values_list(field_name, flat=True)` queries rather than instantiating model rows in memory.
3. **Indexed Timestamp Queries**:
   - `Project.created_at`, `Blog.publication_date`, `Experience.start_date`, and `FAQ.created_at` are indexed (`db_index=True`) for fast sorting.

---

## 5. Security & Rate Limiting

- **IP-Based Contact Limiting**: Tracks submission volume per IP over 24-hour sliding windows (10/day max in production).
- **Hardened Allowed Hosts**: Strict host domain verification in production.
- **Content Security Policy (CSP)**: Blocks unauthorized external scripts and framing attempts.
