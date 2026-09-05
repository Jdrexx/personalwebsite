"""SEO metadata and JSON-LD builders for the public portfolio."""

import json

from django.conf import settings
from django.templatetags.static import static


PERSON_ID = f"{settings.SITE_URL}/#jonathan-dreksler"
SITE_ID = f"{settings.SITE_URL}/#website"


def absolute_url(path="/"):
    return f"{settings.SITE_URL.rstrip('/')}/{path.lstrip('/')}"


def image_url(path="portfolio/featured-work.png"):
    return absolute_url(static(path))


def person_schema(content):
    return {
        "@type": "Person",
        "@id": PERSON_ID,
        "name": content["name"],
        "url": settings.SITE_URL,
        "image": image_url("portfolio/me.jpg"),
        "jobTitle": content["headline"],
        "description": content["summary"],
        "email": f"mailto:{content['email']}",
        "homeLocation": {"@type": "Place", "name": content["location"]},
        "alumniOf": {
            "@type": "CollegeOrUniversity",
            "name": "University of Maryland Global Campus",
        },
        "sameAs": [content["github"], "https://www.linkedin.com/in/jdrexx"],
        "knowsAbout": content["skills"],
    }


def breadcrumbs(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": name,
                "item": absolute_url(path),
            }
            for index, (name, path) in enumerate(items, start=1)
        ],
    }


def seo_context(
    *,
    title,
    description,
    path,
    content,
    image=None,
    page_type="WebPage",
    robots="index,follow,max-image-preview:large",
    schemas=None,
):
    canonical = absolute_url(path)
    graph = [
        {
            "@type": "WebSite",
            "@id": SITE_ID,
            "url": settings.SITE_URL,
            "name": f"{content['name']} — Websites & AI Automation",
            "inLanguage": "en-US",
            "publisher": {"@id": PERSON_ID},
        },
        {
            "@type": page_type,
            "@id": f"{canonical}#webpage",
            "url": canonical,
            "name": title,
            "description": description,
            "isPartOf": {"@id": SITE_ID},
            "about": {"@id": PERSON_ID},
            "inLanguage": "en-US",
        },
    ]
    if schemas:
        graph.extend(schemas)
    return {
        "title": title,
        "description": description,
        "canonical": canonical,
        "robots": robots,
        "image": image or image_url(),
        "type": "article" if page_type in {"Article", "TechArticle"} else "website",
        "json_ld": json.dumps(
            {"@context": "https://schema.org", "@graph": graph},
            ensure_ascii=False,
            separators=(",", ":"),
        ).replace("</", "<\\/"),
    }