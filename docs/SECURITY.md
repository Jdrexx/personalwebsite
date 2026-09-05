# Security Profile — jdreksler.com

## Overview

This is a static portfolio website built with Django. It has no user accounts, no forms, no database of user data, and no file uploads from visitors. The attack surface is inherently minimal.

## PII Inventory

| Field    | Where Stored           | Where Displayed            | Risk                                                 |
| -------- | ---------------------- | -------------------------- | ---------------------------------------------------- |
| Name     | `portfolio/content.py` | All pages (header, footer) | Low — public portfolio                               |
| Email    | `portfolio/content.py` | Footer, resume page        | Low — public contact info (harvesting risk accepted) |
| Phone    | `portfolio/content.py` | Resume page                | Low — public contact info                            |
| Location | `portfolio/content.py` | Home, resume pages         | Low — public info                                    |

**Decision:** Email and phone are deliberately published as contact channels for a professional portfolio.

## Security Controls

### Transport Security (headers served on every response)

| Header                     | Value                                                                                                                                                                                                                                                                                                                                    | Set by                                                                                  |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Content-Security-Policy    | `default-src 'self'; script-src 'self' https://www.googletagmanager.com; connect-src 'self' https://www.google-analytics.com https://*.google-analytics.com; style-src 'self'; font-src 'self'; img-src 'self' data: https://www.google-analytics.com; form-action 'self' https://formspree.io; base-uri 'self'; frame-ancestors 'none'` | `personalwebsite/middleware.py`                                                         |
| Permissions-Policy         | `camera=(), microphone=(), geolocation=(), interest-cohort=()`                                                                                                                                                                                                                                                                           | `personalwebsite/middleware.py`                                                         |
| Strict-Transport-Security  | `max-age=31536000; includeSubDomains; preload`                                                                                                                                                                                                                                                                                           | Django `SecurityMiddleware` (`SECURE_HSTS_*`, prod only)                                |
| X-Frame-Options            | `DENY`                                                                                                                                                                                                                                                                                                                                   | Django `SecurityMiddleware` (`XFrameOptionsMiddleware`)                                 |
| X-Content-Type-Options     | `nosniff`                                                                                                                                                                                                                                                                                                                                | Django `SecurityMiddleware`                                                             |
| Referrer-Policy            | `strict-origin-when-cross-origin` (explicit business choice — keeps outbound origin attribution when visitors click through to GitHub/LinkedIn; never leaks the path)                                                                                                                                                                    | Django `SecurityMiddleware` (`SECURE_REFERRER_POLICY`, set in `settings.py` prod block) |
| Cross-Origin-Opener-Policy | `same-origin`                                                                                                                                                                                                                                                                                                                            | Django `SecurityMiddleware` default (`SECURE_CROSS_ORIGIN_OPENER_POLICY`)               |

No inline scripts or external stylesheets: fonts are self-hosted, interactive JS is in
versioned static files, and JSON-LD is inert metadata. The policy has no
`unsafe-inline` anywhere.

### Application-Level Controls (Django)

| Control                          | Status                                                                      |
| -------------------------------- | --------------------------------------------------------------------------- |
| CSRF protection                  | Active (`CsrfViewMiddleware`)                                               |
| X-Frame-Options                  | Active (`XFrameOptionsMiddleware` — DENY default)                           |
| SecurityMiddleware               | Active (X-Content-Type-Options, X-Frame-Options, SECURE_SSL_REDIRECT, HSTS) |
| Custom SecurityHeadersMiddleware | Active (sets CSP + Permissions-Policy; see table above)                     |
| Admin URL gating                 | Configurable via `DJANGO_ADMIN_URL` env var (hidden from scanners)          |
| Template auto-escaping           | Active — the only `                                                         | safe`is the server-side`</`-escaped JSON-LD block in `base.html`; no `{% autoescape off %}` |
| ALLOWED_HOSTS                    | Configured via `DJANGO_ALLOWED_HOSTS` env var                               |
| SESSION_COOKIE_SECURE            | True                                                                        |
| CSRF_COOKIE_SECURE               | True                                                                        |
| CSRF_TRUSTED_ORIGINS             | Configurable via `DJANGO_CSRF_TRUSTED_ORIGINS` env var                      |
| SECURE_PROXY_SSL_HEADER          | Configured for Railway                                                      |
| SECURE_HSTS_SECONDS              | 31536000 (production only)                                                  |
| SECURE_SSL_REDIRECT              | True (production only, gated via `DJANGO_SECURE_SSL`)                       |

### Audit History

| Date       | Finding                                                          | Fix Applied                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-07-17 | Hardcoded SECRET_KEY fallback                                    | Replaced with validation — raises `RuntimeError` in production if unset                                                                                                                                                                                                                                                                                                                                  |
| 2026-07-17 | DEBUG defaulted to True                                          | Changed default to `'0'` (False)                                                                                                                                                                                                                                                                                                                                                                         |
| 2026-07-17 | Missing SECURE_PROXY_SSL_HEADER                                  | Added `('HTTP_X_FORWARDED_PROTO', 'https')`                                                                                                                                                                                                                                                                                                                                                              |
| 2026-07-17 | Missing SESSION/CSRF secure cookies                              | Added `SESSION_COOKIE_SECURE = True`, `CSRF_COOKIE_SECURE = True`                                                                                                                                                                                                                                                                                                                                        |
| 2026-07-17 | Missing HSTS settings                                            | Added `SECURE_HSTS_SECONDS`, `SECURE_HSTS_INCLUDE_SUBDOMAINS`, `SECURE_HSTS_PRELOAD`                                                                                                                                                                                                                                                                                                                     |
| 2026-07-17 | Missing SECURE_SSL_REDIRECT                                      | Added (production only)                                                                                                                                                                                                                                                                                                                                                                                  |
| 2026-07-17 | Missing custom error pages                                       | Created `404.html` and `500.html`                                                                                                                                                                                                                                                                                                                                                                        |
| 2026-07-17 | Loose dependency pinning                                         | Pinned exact versions in `requirements.txt`                                                                                                                                                                                                                                                                                                                                                              |
| 2026-07-17 | Whitenoise typo in requirements                                  | Fixed `whitenoine` → `whitenoise`                                                                                                                                                                                                                                                                                                                                                                        |
| 2026-09-04 | docs/SECURITY.md drifted from code                               | Corrected CSP/header table to match `middleware.py` + Django SecurityMiddleware defaults; fixed the `                                                                                                                                                                                                                                                                                                    | safe` claim |
| 2026-09-04 | django 6.0.7 (PYSEC-2026-3717, GeoDjango-only, unreachable here) | Bumped to `django==6.0.8`                                                                                                                                                                                                                                                                                                                                                                                |
| 2026-09-04 | Triad+ audit pass                                                | Gated fade-in animations behind a `js` class (no-JS visitors no longer see a blank page); added pre-paint `theme-init.js` (FOUC fix, CSP-compatible); dropped frozen sitemap `lastmod`; switched Referrer-Policy to `strict-origin-when-cross-origin` (business choice); added `tests_audit.py` invariants (sitemap HTTP 200s, canonical-host independence, exact CSP, JSON-LD parse, one-hop redirects) |

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