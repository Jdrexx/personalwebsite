"""Audit-driven invariants the original suite leaves unpinned.

Covers the gaps called out in the Triad+ audit: sitemap integrity, canonical
host independence, exact CSP, JSON-LD parse validity, dangling relationship
links, and redirect chains.
"""

import json
import re
from xml.etree import ElementTree

from django.test import TestCase, override_settings

from .content import SITE_CONTENT
from .services import SERVICES

SITEMAP_NS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

# Pinned verbatim to middleware.py so any CSP change forces a conscious update
# here and in docs/SECURITY.md at the same time.
EXPECTED_CSP = (
    "default-src 'self';"
    "script-src 'self' https://www.googletagmanager.com;"
    "connect-src 'self' https://www.google-analytics.com https://*.google-analytics.com;"
    "style-src 'self';"
    "font-src 'self';"
    "img-src 'self' data: https://www.google-analytics.com;"
    "form-action 'self' https://formspree.io;"
    "base-uri 'self';"
    "frame-ancestors 'none';"
)


class SitemapIntegrityTests(TestCase):
    def _locs(self):
        root = ElementTree.fromstring(self.client.get("/sitemap.xml").content)
        return [el.text for el in root.iter(f"{SITEMAP_NS}loc")]

    def test_every_advertised_url_resolves(self):
        for loc in self._locs():
            path = re.sub(r"^https?://[^/]+", "", loc)
            with self.subTest(loc=loc):
                self.assertEqual(self.client.get(path, secure=True).status_code, 200)

    def test_locs_use_canonical_host_not_request_host(self):
        for loc in self._locs():
            self.assertTrue(loc.startswith("https://jdreksler.com/"), loc)


@override_settings(ALLOWED_HOSTS=["*"], SITE_URL="https://jdreksler.com")
class HostIndependenceTests(TestCase):
    def test_canonical_ignores_request_host(self):
        body = self.client.get(
            "/", HTTP_HOST="evil.example.com", secure=True
        ).content.decode()
        self.assertIn('rel="canonical" href="https://jdreksler.com/"', body)
        self.assertNotIn("evil.example.com", body)


class HeaderAndSchemaTests(TestCase):
    PAGES = [
        "/",
        "/resume/",
        "/projects/",
        "/services/",
        "/contact/",
        "/does-not-exist/",
    ]

    def test_csp_header_is_exact_on_every_response_including_404(self):
        for path in self.PAGES:
            with self.subTest(path=path):
                self.assertEqual(
                    self.client.get(path, secure=True)["Content-Security-Policy"],
                    EXPECTED_CSP,
                )

    def test_json_ld_is_parseable_on_every_page(self):
        pattern = re.compile(
            r'<script type="application/ld\+json">(.*?)</script>', re.DOTALL
        )
        for path in self.PAGES:
            body = self.client.get(path, secure=True).content.decode()
            for block in pattern.findall(body):
                with self.subTest(path=path):
                    json.loads(block)


class ContentIntegrityTests(TestCase):
    def test_service_related_project_names_all_exist(self):
        project_names = {p["name"] for p in SITE_CONTENT["projects"]}
        for slug, service in SERVICES.items():
            for related in service.get("related", []):
                with self.subTest(slug=slug, related=related):
                    self.assertIn(related, project_names)

    def test_redirects_land_in_one_hop(self):
        for path in ["/index.html", "/portfolio/", "/about/", "/blog/", "/hire-me/"]:
            with self.subTest(path=path):
                response = self.client.get(path, secure=True, follow=True)
                self.assertEqual(response.status_code, 200)
                self.assertLessEqual(len(response.redirect_chain), 1)

    def test_robots_never_discloses_secret_admin_path(self):
        from django.conf import settings

        body = self.client.get("/robots.txt", secure=True).content.decode()
        # the default /admin/ disallow is harmless boilerplate (the path 404s);
        # the REAL requirement is that a configured secret admin URL never leaks
        if settings.ADMIN_URL:
            self.assertNotIn(settings.ADMIN_URL, body)
        self.assertIn("https://jdreksler.com/sitemap.xml", body)