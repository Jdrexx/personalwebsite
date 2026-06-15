# Jonathan Dreksler — Personal Website

A clean, modern personal portfolio website built with **Python + Django**.

## Design

- Dark palette: blues, greys, and blacks
- Modern, clean one-page portfolio layout
- Image placeholder sections ready for future photos/screenshots
- Editable content isolated in `portfolio/content.py`
- Django templates split into reusable pages for easy maintenance

## Quick Start

```bash
python -m venv .venv
. .venv/Scripts/activate  # Windows Git Bash
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open: http://127.0.0.1:8000

## Run Tests

```bash
python manage.py test
```

## Editing Site Content

Most portfolio copy, resume sections, skill lists, and project cards live in:

```text
portfolio/content.py
```

Styling is in:

```text
portfolio/static/portfolio/css/site.css
```

Templates are in:

```text
portfolio/templates/portfolio/
```

## Image Placeholders

The site intentionally includes placeholder panels for future photos, headshots, project screenshots, and brand visuals.
