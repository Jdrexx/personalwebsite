from datetime import date
from types import SimpleNamespace
from urllib.parse import urlparse

from django.conf import settings
from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from .content import SITE_CONTENT
from .services import SERVICES


LAST_CONTENT_UPDATE = date(2026, 8, 18)


class CanonicalSitemap(Sitemap):
    """Keep sitemap hosts stable even on Railway preview/custom domains."""

    def get_urls(self, page=1, site=None, protocol=None):
        parsed = urlparse(settings.SITE_URL)
        canonical_site = SimpleNamespace(domain=parsed.netloc)
        return super().get_urls(
            page=page,
            site=canonical_site,
            protocol=parsed.scheme or "https",
        )


class StaticSitemap(CanonicalSitemap):
    protocol = "https"

    def items(self):
        return ["home", "services", "projects", "resume", "contact"]

    def location(self, item):
        return reverse(f"portfolio:{item}")

    def priority(self, item):
        return {"home": 1.0, "services": 0.9, "projects": 0.9}.get(item, 0.6)

    def changefreq(self, item):
        return "weekly" if item in {"home", "projects"} else "monthly"

    def lastmod(self, item):
        return LAST_CONTENT_UPDATE


class ServiceSitemap(CanonicalSitemap):
    protocol = "https"
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return list(SERVICES.keys())

    def location(self, slug):
        return reverse("portfolio:service_detail", kwargs={"slug": slug})

    def lastmod(self, slug):
        return LAST_CONTENT_UPDATE


class CaseStudySitemap(CanonicalSitemap):
    protocol = "https"
    priority = 0.8
    changefreq = "monthly"

    def items(self):
        return [
            project for project in SITE_CONTENT["projects"] if project.get("case_study")
        ]

    def location(self, project):
        return reverse("portfolio:case_study", kwargs={"slug": project["name"].lower()})

    def lastmod(self, project):
        return LAST_CONTENT_UPDATE