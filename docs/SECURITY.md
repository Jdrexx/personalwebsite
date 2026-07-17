# Security Profile — jdreksler.com

## Overview

This is a static portfolio website built with Django. It has no user accounts, no forms, no database of user data, and no file uploads from visitors. The attack surface is inherently minimal.

## PII Inventory

| Field | Where Stored | Where Displayed | Risk |
|-------|-------------|-----------------|------|
| Name | `portfolio/content.py` | All pages (header, footer) | Low — public portfolio |
| Email | `portfolio/content.py` | Footer, resume page | Low — public contact info (harvesting risk accepted) |
| Phone | `portfolio/content.py` | Resume page | Low — public contact info |
| Location | `portfolio/content.py` | Home, resume pages | Low — public info |

**Decision:** Email and phone are deliberately published as contact channels for a professional portfolio.

## Security Controls

### Transport Security (via Railway edge proxy)

| Header | Value |
|--------|-------|
| Content-Security-Policy | `default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' https://fonts.googleapis.com; font-src 'self' https://fonts.gstatic.com; img-src 'self' data:; form-action 'self' https://formspree.io; base-uri 'self'; frame-ancestors 'none'` |
| Strict-Transport-Security | `max-age=31536000; includeSubDomains; preload` |
| X-Frame-Options | `DENY` |
| X-Content-Type-Options | `nosniff` |
| Referrer-Policy | `same-origin` |
| Permissions-Policy | `camera=(), microphone=(), geolocation=(), interest-cohort=()` |
| Cross-Origin-Opener-Policy | `same-origin` |

### Application-Level Controls (Django)

| Control | Status |
|---------|--------|
| CSRF protection | Active (`CsrfViewMiddleware`) |
| X-Frame-Options | Active (`XFrameOptionsMiddleware` — DENY default) |
| SecurityMiddleware | Active (X-Content-Type-Options, X-Frame-Options, SECURE_SSL_REDIRECT, HSTS) |
| Custom SecurityHeadersMiddleware | Active (sets CSP, Permissions-Policy, Referrer-Policy, COOP) |
| Admin URL gating | Configurable via `DJANGO_ADMIN_URL` env var (hidden from scanners) |
| Template auto-escaping | Active — no `|safe` filters, no `{% autoescape off %}` |
| ALLOWED_HOSTS | Configured via `DJANGO_ALLOWED_HOSTS` env var |
| SESSION_COOKIE_SECURE | True |
| CSRF_COOKIE_SECURE | True |
| CSRF_TRUSTED_ORIGINS | Configurable via `DJANGO_CSRF_TRUSTED_ORIGINS` env var |
| SECURE_PROXY_SSL_HEADER | Configured for Railway |
| SECURE_HSTS_SECONDS | 31536000 (production only) |
| SECURE_SSL_REDIRECT | True (production only, gated via `DJANGO_SECURE_SSL`) |

### Audit History

| Date | Finding | Fix Applied |
|------|---------|-------------|
| 2026-07-17 | Hardcoded SECRET_KEY fallback | Replaced with validation — raises `RuntimeError` in production if unset |
| 2026-07-17 | DEBUG defaulted to True | Changed default to `'0'` (False) |
| 2026-07-17 | Missing SECURE_PROXY_SSL_HEADER | Added `('HTTP_X_FORWARDED_PROTO', 'https')` |
| 2026-07-17 | Missing SESSION/CSRF secure cookies | Added `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True` |
| 2026-07-17 | Missing HSTS settings | Added `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD` |
| 2026-07-17 | Missing SECURE_SSL_REDIRECT | Added (production only) |
| 2026-07-17 | Missing custom error pages | Created `404.html` and `500.html` |
| 2026-07-17 | Loose dependency pinning | Pinned exact versions in `requirements.txt` |
| 2026-07-17 | Whitenoise typo in requirements | Fixed `whitenoine` → `whitenoise` |

## Known Gaps (Acceptable Risk)

1. **Email/phone are public** — deliberate choice for portfolio visibility.
2. **No rate limiting** — no user-submission endpoints exist, so no rate limiting is configured.
3. **No custom 403 template** — the admin login is the only auth-gated path, and Django's default is adequate.

## Deployment Requirements

All production deploys **must** set:

```
DJANGO_SECRET_KEY=<generated key>
DJANGO_ALLOWED_HOSTS=jdreksler.com,www.jdreksler.com
```

Generate a key with:
```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```
