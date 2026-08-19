from django.conf import settings
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from django.shortcuts import render
from django.urls import reverse

from .content import SITE_CONTENT
from .seo import (
    PERSON_ID,
    absolute_url,
    breadcrumbs,
    image_url,
    person_schema,
    seo_context,
)
from .services import SERVICES


def base_context(active="home", seo=None):
    return {
        "content": SITE_CONTENT,
        "active": active,
        "seo": seo,
        "services": SERVICES,
        "analytics_id": settings.GOOGLE_ANALYTICS_ID,
    }


def home(request):
    description = (
        "Jonathan Dreksler designs, builds, and supports custom websites and AI "
        "workflow automation for small businesses and service teams."
    )
    profile = {
        "@type": "ProfilePage",
        "@id": f"{settings.SITE_URL}/#profile",
        "url": settings.SITE_URL,
        "name": "Jonathan Dreksler — Websites & AI Automation",
        "mainEntity": {"@id": PERSON_ID},
        "dateModified": "2026-08-18",
    }
    seo = seo_context(
        title="Websites and AI Automation Built Around Your Business | Jonathan Dreksler",
        description=description,
        path="/",
        content=SITE_CONTENT,
        schemas=[person_schema(SITE_CONTENT), profile],
    )
    return render(request, "portfolio/home.html", base_context("home", seo))


def resume(request):
    seo = seo_context(
        title="Resume | Jonathan Dreksler — AI Automation & Web Development",
        description=(
            "Resume for Jonathan Dreksler: AI workflow automation, custom websites, "
            "client onboarding, customer service, and technical project delivery."
        ),
        path=reverse("portfolio:resume"),
        content=SITE_CONTENT,
        image=image_url("portfolio/me.jpg"),
        schemas=[person_schema(SITE_CONTENT), breadcrumbs([
            ("Home", "/"), ("Resume", reverse("portfolio:resume"))
        ])],
    )
    return render(request, "portfolio/resume.html", base_context("resume", seo))


def projects(request):
    path = reverse("portfolio:projects")
    project_items = [
        {
            "@type": "ListItem",
            "position": index,
            "url": absolute_url(reverse("portfolio:case_study", kwargs={"slug": project["name"].lower()})),
            "name": project["name"],
        }
        for index, project in enumerate(SITE_CONTENT["projects"], start=1)
        if project.get("case_study")
    ]
    seo = seo_context(
        title="AI Automation & Web Application Projects | Jonathan Dreksler",
        description=(
            "Six detailed case studies in AI automation, OCR, document search, data, "
            "CRM, and productivity systems, built by Jonathan Dreksler."
        ),
        path=path,
        content=SITE_CONTENT,
        page_type="CollectionPage",
        schemas=[
            {"@type": "ItemList", "name": "Selected technical projects", "itemListElement": project_items},
            breadcrumbs([("Home", "/"), ("Projects", path)]),
        ],
    )
    return render(request, "portfolio/projects.html", base_context("projects", seo))


def services(request):
    path = reverse("portfolio:services")
    item_list = {
        "@type": "ItemList",
        "name": "Technical consulting services",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": service["name"],
                "url": absolute_url(reverse("portfolio:service_detail", kwargs={"slug": slug})),
            }
            for index, (slug, service) in enumerate(SERVICES.items(), start=1)
        ],
    }
    seo = seo_context(
        title="AI Automation & Website Design Services | Jonathan Dreksler",
        description=(
            "AI workflow automation, website design and development, customer service "
            "systems, and technical project management for small businesses."
        ),
        path=path,
        content=SITE_CONTENT,
        page_type="CollectionPage",
        schemas=[item_list, breadcrumbs([("Home", "/"), ("Services", path)])],
    )
    return render(request, "portfolio/services.html", base_context("services", seo))


def service_detail(request, slug):
    service = SERVICES.get(slug)
    if not service:
        raise Http404("Service not found")
    path = reverse("portfolio:service_detail", kwargs={"slug": slug})
    related_projects = [
        project for project in SITE_CONTENT["projects"] if project["name"] in service["related"]
    ]
    service_schema = {
        "@type": "Service",
        "@id": f"{absolute_url(path)}#service",
        "name": service["name"],
        "description": service["description"],
        "provider": {"@id": PERSON_ID},
        "areaServed": {"@type": "Country", "name": "United States"},
        "url": absolute_url(path),
    }
    seo = seo_context(
        title=f"{service['name']} | Jonathan Dreksler",
        description=service.get("seo_description", service["description"]),
        path=path,
        content=SITE_CONTENT,
        schemas=[service_schema, breadcrumbs([
            ("Home", "/"),
            ("Services", reverse("portfolio:services")),
            (service["name"], path),
        ])],
    )
    context = {
        **base_context("services", seo),
        "service": service,
        "service_slug": slug,
        "related_projects": related_projects,
    }
    return render(request, "portfolio/service_detail.html", context)


def contact(request):
    path = reverse("portfolio:contact")
    seo = seo_context(
        title="Contact Jonathan Dreksler | AI Automation & Websites",
        description=(
            "Contact Jonathan Dreksler about a custom website, AI workflow automation, "
            "customer service system, or technical project."
        ),
        path=path,
        content=SITE_CONTENT,
        schemas=[breadcrumbs([("Home", "/"), ("Contact", path)])],
    )
    sent = request.method == "POST"
    return render(request, "portfolio/contact.html", {**base_context("contact", seo), "sent": sent})


def thanks(request):
    seo = seo_context(
        title="Message Sent | Jonathan Dreksler",
        description="Confirmation that your message was sent to Jonathan Dreksler.",
        path=reverse("portfolio:thanks"),
        content=SITE_CONTENT,
        robots="noindex,follow",
    )
    return render(request, "portfolio/thanks.html", base_context("contact", seo))


def case_study(request, slug):
    normalized_slug = slug.lower().replace("-", "")
    project = next(
        (p for p in SITE_CONTENT.get("projects", []) if p["name"].lower() == normalized_slug),
        None,
    )
    if not project or not project.get("case_study"):
        raise Http404("Case study not found")
    # Only the canonical slug may serve the page. Variants (hyphenated or
    # mixed-case URLs from older versions of the site) 301 to the canonical
    # URL so Google never sees a near-duplicate "alternate page".
    canonical_slug = project["name"].lower()
    if slug != canonical_slug:
        return HttpResponsePermanentRedirect(
            reverse("portfolio:case_study", kwargs={"slug": canonical_slug})
        )
    path = reverse("portfolio:case_study", kwargs={"slug": slug})
    # Keep search and social snippets concise while letting the visible page carry
    # the full problem, workflow, decisions, results, and roadmap narrative.
    description = f"{project['name']} case study: {project['description']}"
    article = {
        "@type": "TechArticle",
        "@id": f"{absolute_url(path)}#article",
        "headline": f"{project['name']} technical case study",
        "description": description,
        "url": absolute_url(path),
        "image": image_url(f"portfolio/projects/{project['name'].lower()}.png"),
        "author": {"@id": PERSON_ID},
        "dateModified": "2026-08-18",
        "mainEntityOfPage": {"@id": f"{absolute_url(path)}#webpage"},
        "keywords": project["tech"],
    }
    seo = seo_context(
        title=f"{project['name']} Case Study | Jonathan Dreksler",
        description=description,
        path=path,
        content=SITE_CONTENT,
        image=article["image"],
        page_type="TechArticle",
        schemas=[article, breadcrumbs([
            ("Home", "/"),
            ("Projects", reverse("portfolio:projects")),
            (project["name"], path),
        ])],
    )
    return render(request, "portfolio/case_study.html", {
        **base_context("projects", seo), "project": project, "cs": project["case_study"]
    })


def robots_txt(request):
    body = "\n".join([
        "User-agent: *",
        "Allow: /",
        "Disallow: /admin/",
        f"Sitemap: {settings.SITE_URL}/sitemap.xml",
        "",
    ])
    return HttpResponse(body, content_type="text/plain; charset=utf-8")


def error_404(request, exception):
    seo = seo_context(
        title="Page Not Found | Jonathan Dreksler",
        description="The requested page could not be found on Jonathan Dreksler's technical portfolio.",
        path=request.path,
        content=SITE_CONTENT,
        robots="noindex,follow",
    )
    return render(request, "404.html", base_context("home", seo), status=404)
