# Jonathan Dreksler — Personal Website

[![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![HTML/CSS](https://img.shields.io/badge/HTML%2FCSS-Tailwind%20Inspired-E34F26?logo=html5&logoColor=white)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![Railway](https://img.shields.io/badge/Railway-Deployed-0B0D0E?logo=railway&logoColor=white)](https://railway.app)

> **Live site:** [https://jdreksler.com](https://jdreksler.com)

A clean, modern personal portfolio website built with **Django 5.2** and **Python**. Features a dark theme, responsive layout, and editable content isolated from templates. Deployed on Railway via Gunicorn and WhiteNoise.

---

## Features

- **Home page** — headline, tagline, summary, focus areas, and call-to-action buttons
- **Projects page** — portfolio of six showcased projects with descriptions and GitHub links
- **Resume page** — full work experience timeline with role details and bullet points
- **Contact section** — email, phone, location, and GitHub profile link in the footer
- **Editable content** — all site copy lives in `portfolio/content.py`; no template changes needed for text updates
- **Responsive dark theme** — blues, greys, and blacks with a clean, professional layout
- **SQLite by default** — optional MySQL via environment variables for production
- **Static file serving** — WhiteNoise for production-ready static asset delivery

---

## Tech Stack

| Layer      | Technology                                            |
| ---------- | ----------------------------------------------------- |
| Framework  | [Django 5.2](https://www.djangoproject.com/)          |
| Language   | [Python 3.12+](https://www.python.org/)               |
| Frontend   | HTML5, CSS3 (custom, responsive)                      |
| Server     | [Gunicorn](https://gunicorn.org/)                     |
| Static     | [WhiteNoise](https://whitenoise.readthedocs.io/)      |
| Database   | SQLite (dev) / MySQL (production via Railway)         |
| Deployment | [Railway](https://railway.app)                        |

---

## Quick Start

```bash
# Clone the repo
git clone https://github.com/Jdrexx/personalwebsite.git
cd personalwebsite

# Create and activate a virtual environment
python -m venv .venv
source .venv/Scripts/activate      # Windows Git Bash
# source .venv/bin/activate        # macOS / Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the dev server
python manage.py runserver
```

Open **http://127.0.0.1:8000** in your browser.

---

## Project Structure

```
personalwebsite/
├── manage.py
├── requirements.txt
├── Procfile                  # Railway deployment config
├── docs/                     # Documentation
│   └── SECURITY.md           # Security profile & audit history
├── portfolio/                # Main Django app
│   ├── content.py            # All editable site content
│   ├── views.py              # Home / projects / resume views
│   ├── urls.py
│   ├── templates/portfolio/  # HTML templates
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── projects.html
│   │   └── resume.html
│   └── static/portfolio/css/ # Stylesheets
│       └── site.css
└── personalwebsite/          # Django project settings
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

---

## Editing Site Content

All portfolio copy, resume sections, skill lists, and project cards live in a single file:

```text
portfolio/content.py
```

Update the `SITE_CONTENT` dictionary to change text without touching templates or views.

Styling is in:

```text
portfolio/static/portfolio/css/site.css
```

---

## Deployment (Railway)

This project is configured for one-click deployment on [Railway](https://railway.app).

### Procfile

The `Procfile` at the project root defines two commands:

```procfile
release: python manage.py migrate --noinput
web: python manage.py collectstatic --noinput && gunicorn personalwebsite.wsgi --bind 0.0.0.0:$PORT --workers 2 --timeout 120
```

- **release** — runs database migrations before the web process starts
- **web** — collects static files, then starts Gunicorn with 2 workers

### Required Environment Variables

| Variable             | Description                          | Required |
| -------------------- | ------------------------------------ | -------- |
| `DJANGO_SECRET_KEY`  | Django secret key                    | **Yes** (production) |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated hostnames         | Yes |
| `DJANGO_DEBUG`       | Set to `1` for debug (omit for prod) | No |

> **Important:** In production, `DJANGO_SECRET_KEY` **must** be set to a secure random value. If omitted, the app will refuse to start with a clear error message. Generate one with:
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

For MySQL on Railway, set any of the standard Railway MySQL environment variables (e.g. `MYSQLHOST`, `MYSQLUSER`, `MYSQLPASSWORD`, `MYSQLDATABASE`). If none are set, the site falls back to SQLite.

### Deploy Steps

1. Push the repo to GitHub
2. On Railway, create a new project → **Deploy from GitHub repo**
3. Add the environment variables above under **Variables**
4. Railway auto-detects the Procfile and deploys

---

## Tests

```bash
python manage.py test
```

---

## License

Private — personal portfolio site.
