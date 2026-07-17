# Jonathan Dreksler — Personal Website

[![Django](https://img.shields.io/badge/Django-5.2-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)

Personal portfolio site — Django 5.2, dark theme, responsive. Deployed on Railway.

- **docs/SECURITY.md** — CWE audit history and security controls documentation

## Quick start

```
git clone https://github.com/Jdrexx/personalwebsite.git
cd personalwebsite
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000

## Editing content

Everything visible on the page (tagline, resume bullets, project descriptions, case studies) lives in one file:

```
portfolio/content.py
```

Change text there — no template edits needed. Styling is in `portfolio/static/portfolio/css/site.css`.

## Deployment

Deploys to Railway via git push. Requires two env vars:

- `DJANGO_SECRET_KEY` — generate with `python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'`
- `DJANGO_ALLOWED_HOSTS` — comma-separated (production domain)

Optional: `DJANGO_DEBUG=1` for local dev, `DJANGO_ADMIN_URL=<secret-path>` to gate admin behind a non-standard URL.

> **Note:** `DJANGO_SECRET_KEY` is mandatory in production — if omitted, the app refuses to start with a clear error message.

## Known quirks

- Admin is disabled by default. Set `DJANGO_ADMIN_URL` to something random and it activates at `/<that-value>/`.
- The contact form POSTs to Formspree. Works without a backend SMTP setup but your free Formspree plan has a monthly cap.
- CSP uses `'unsafe-inline'` for scripts. The inline JS powers the terminal widget and theme toggle. If those get extracted to static files someday I'll tighten it.

## Tests

```
python manage.py test
```

MIT license.
