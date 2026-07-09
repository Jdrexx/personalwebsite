from pathlib import Path
import os
from urllib.parse import urlparse

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Debug & Allowed Hosts ──────────────────────────────────────────────────
DEBUG = os.environ.get('DJANGO_DEBUG', '0') == '1'
ALLOWED_HOSTS = [
    host.strip()
    for host in os.environ.get('DJANGO_ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')
    if host.strip()
]

# ── Secret Key ─────────────────────────────────────────────────────────────
# Must be set via environment variable in production. Falls back to a dev
# key when unset — check --deploy will flag this as W009 in production.
import warnings as _warnings
_django_secret_key = os.environ.get('DJANGO_SECRET_KEY')
if not DEBUG and not _django_secret_key:
    _warnings.warn(
        "DJANGO_SECRET_KEY is not set! Session signing will be insecure. "
        "Generate one with: python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'",
        RuntimeWarning,
    )
SECRET_KEY = _django_secret_key or os.environ.get('HERMES_SECRET_KEY') or 'dev-key-do-not-use-in-production'

# ── Installed Apps ─────────────────────────────────────────────────────────
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'portfolio',
]

# ── Middleware ──────────────────────────────────────────────────────────────
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'personalwebsite.middleware.SecurityHeadersMiddleware',
]

ROOT_URLCONF = 'personalwebsite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'personalwebsite.wsgi.application'

# ── Database ───────────────────────────────────────────────────────────────
# Priority: full URL (Railway standard) → individual env vars → SQLite fallback
_db_url = os.environ.get('MYSQL_URL') or os.environ.get('MARIADB_URL') or ''

if _db_url:
    _parsed = urlparse(_db_url)
    db_host = _parsed.hostname or ''
    try:
        db_port = int(_parsed.port) if _parsed.port else 3306
    except (ValueError, TypeError):
        db_port = 3306
    db_name = _parsed.path.lstrip('/') if _parsed.path else 'railway'
    db_user = _parsed.username or 'root'
    db_pass = _parsed.password or ''
else:
    db_host = (
        os.environ.get('MARIADB_PRIVATE_HOST') or
        os.environ.get('MYSQL_HOST') or
        os.environ.get('MYSQLHOST') or
        ''
    )
    db_port_raw = (
        os.environ.get('MARIADB_PRIVATE_PORT') or
        os.environ.get('MYSQL_PORT') or
        os.environ.get('MYSQLPORT') or
        '3306'
    )
    try:
        db_port = int(db_port_raw)
    except (ValueError, TypeError):
        db_port = 3306
    db_name = (
        os.environ.get('MARIADB_DATABASE') or
        os.environ.get('MYSQL_DATABASE') or
        os.environ.get('MYSQLDATABASE') or
        'railway'
    )
    db_user = (
        os.environ.get('MARIADB_USER') or
        os.environ.get('MYSQL_USER') or
        os.environ.get('MYSQLUSER') or
        'root'
    )
    db_pass = (
        os.environ.get('MARIADB_PASSWORD') or
        os.environ.get('MYSQL_PASSWORD') or
        os.environ.get('MYSQLPASSWORD') or
        ''
    )

if db_host and not db_pass:
    _warnings.warn(
        "Database password is empty while using MySQL/MariaDB. "
        "Set MARIADB_PASSWORD or MYSQL_PASSWORD environment variable.",
        RuntimeWarning,
    )

if db_host:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': db_host,
            'PORT': db_port,
            'NAME': db_name,
            'USER': db_user,
            'PASSWORD': db_pass,
            'OPTIONS': {
                'autocommit': True,
            },
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# ── Auth ───────────────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internationalization ───────────────────────────────────────────────────
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = True
USE_TZ = True

# ── Static & Media ─────────────────────────────────────────────────────────
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ── Production Security (env-gated) ────────────────────────────────────────
if not DEBUG:
    SECURE_SSL_REDIRECT = os.environ.get('DJANGO_SECURE_SSL', '1') == '1'
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = int(os.environ.get('DJANGO_HSTS_SECONDS', '31536000'))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

    CSRF_TRUSTED_ORIGINS = [
        origin.strip()
        for origin in os.environ.get('DJANGO_CSRF_TRUSTED_ORIGINS', '').split(',')
        if origin.strip()
    ]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Admin Panel ────────────────────────────────────────────────────────────
# Admin is disabled by default. To enable, set DJANGO_ADMIN_URL in the
# environment to a secret path (e.g. "mysecretadmin"). Admin will be
# accessible at /mysecretadmin/ instead of /admin/. This hides the login
# page from scanners and bots while keeping it accessible to you.
ADMIN_URL = os.environ.get('DJANGO_ADMIN_URL', '')
