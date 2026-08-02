# SEO operating guide

The site treats SEO as a maintained product surface rather than a collection of
template tags. Every indexable route is covered by automated metadata, canonical,
structured-data, and sitemap tests.

## Architecture

- `portfolio/seo.py` builds canonical URLs and schema.org JSON-LD.
- `portfolio/sitemaps.py` publishes static, service, and case-study URLs at
  `/sitemap.xml`. The host is pinned to `DJANGO_SITE_URL` so preview domains do
  not leak into the sitemap.
- `portfolio/services.py` is the canonical source for service-page content.
- `/robots.txt` allows public crawling and declares the canonical sitemap.
- `/thanks/` and custom 404 responses use `noindex,follow`.

## Content rules

1. Give every indexable page a unique title, description, canonical, and search
   intent. Keep descriptions between 80 and 160 characters so their core message
   survives typical search and social-preview truncation. Do not create multiple
   pages for keyword variants of the same intent.
2. Only add structured-data claims that a visitor can verify on the page.
3. Add each project with a stable slug, clear problem, technical decisions,
   outcomes, and honest qualification of measured versus expected results.
4. Link new service content to relevant evidence and link case studies back to
   the service they demonstrate.
5. Update `LAST_CONTENT_UPDATE` in `portfolio/sitemaps.py` after substantive
   public content changes.

## Release checklist

```bash
python manage.py test
python manage.py check --deploy
python manage.py collectstatic --noinput
```

After deployment:

1. Confirm `/robots.txt` and `/sitemap.xml` return HTTP 200.
2. Check the homepage, one service page, and one case study in Google's Rich
   Results Test and Search Console URL Inspection.
3. Submit `https://jdreksler.com/sitemap.xml` in Search Console.
4. Record a baseline for clicks, impressions, click-through rate, indexed pages,
   and contact conversions before changing content again.

## Measurement

Google Search Console verification is already present. Optional Google Analytics
support is enabled by setting `GOOGLE_ANALYTICS_ID` (for example, `G-XXXXXXXXXX`).
Tracked contact calls-to-action emit `contact_cta` and form submissions emit
`contact_submit`. If analytics is not configured, the site makes no analytics
requests and the tracking hooks are inert.

Review performance monthly by landing page and query. Use impressions as early
evidence of relevance, CTR to improve titles/descriptions, and conversions to
decide whether traffic is commercially useful. Avoid optimizing for raw traffic
without a relevant service or hiring intent.

## Performance targets

Use Search Console field data as the source of truth and Lighthouse as a release
diagnostic. Target the 75th percentile on mobile and desktop:

- LCP at or below 2.5 seconds
- INP at or below 200 milliseconds
- CLS at or below 0.1

Images include intrinsic dimensions, scripts are deferred, the design uses a
system font stack, and reduced-motion visitors bypass nonessential animations.
