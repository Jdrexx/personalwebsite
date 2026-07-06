# Jonathan Dreksler — Personal Website

[![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Railway](https://img.shields.io/badge/Railway-Deployed-0B0D0E?logo=railway&logoColor=white)](https://railway.app)

**Live site:** [jdreksler.com](https://jdreksler.com)

A personal portfolio website built with Django 5.2. Dark theme, responsive layout, editable content isolated from templates. Deployed on Railway via Gunicorn and WhiteNoise.

## Features

- Home page with headline, tagline, focus areas, and CTAs
- Projects page — six showcased projects with descriptions and GitHub links
- Resume page — full work experience timeline with role details
- Contact section in the footer
- All site copy in `portfolio/content.py` — no template edits needed for text updates
- Responsive dark theme (blues, greys, blacks)
- SQLite by default, MySQL via env vars in production

## Tech Stack

| Layer | Technology |
|---|---|
| Framework | Django 5.2 |
| Language | Python 3.12+ |
| Frontend | HTML5, CSS3 (custom, responsive) |
| Server | Gunicorn |
| Static | WhiteNoise |
| Database | SQLite (dev) / MySQL (production via Railway) |
| Deploy | Railway |

## Quick Start

```bash
git clone https://github.com/Jdrexx/personalwebsite.git
cd personalwebsite
python -m venv .venv
source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
    cd /tmp/personalwebsite && source .venv/bin/activate && DJANGO_DEBUG=1 python manage.py runserver 8765


Open http://127.0.0.1:8000

## Project Structure

```
personalwebsite/
├── manage.py
├── requirements.txt
├── Procfile                  # Railway deployment
├── portfolio/                # Main Django app
│   ├── content.py            # All editable site content
│   ├── views.py              # Home/projects/resume views
│   ├── urls.py
│   ├── templates/portfolio/  # HTML templates
│   └── static/portfolio/css/ # Stylesheets
└── personalwebsite/          # Django project settings
```

## Editing Content

All portfolio text, resume sections, skills, and project cards live in:

```
portfolio/content.py
```

Update the `SITE_CONTENT` dictionary to change text without touching templates or views. Styling is in `portfolio/static/portfolio/css/site.css`.

## Deployment (Railway)

Configured for one-click deploy. Procfile handles migrations and Gunicorn start.

Required env vars: `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`. Set `DJANGO_DEBUG=1` for dev only.

## Tests

```bash
python manage.py test
```

## License

Private — personal portfolio site.
