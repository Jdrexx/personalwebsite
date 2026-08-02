from django.conf import settings
from django.http import Http404, HttpResponse
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
        "Jonathan Dreksler is a technical project manager and Python/Django builder "
        "focused on AI workflow automation, systems integration, and operational delivery."
    )
    profile = {
        "@type": "ProfilePage",
        "@id": f"{settings.SITE_URL}/#profile",
        "url": settings.SITE_URL,
        "name": "Jonathan Dreksler — Technical Project Manager",
        "mainEntity": {"@id": PERSON_ID},
        "dateModified": "2026-08-02",
    }
    seo = seo_context(
        title="Jonathan Dreksler | Technical Project Manager & AI Automation",
        description=description,
        path="/",
        content=SITE_CONTENT,
        schemas=[person_schema(SITE_CONTENT), profile],
    )
    return render(request, "portfolio/home.html", base_context("home", seo))


def resume(request):
    seo = seo_context(
        title="Technical Project Manager Resume | Jonathan Dreksler",
        description=(
            "Resume for Jonathan Dreksler: technical project management, AI automation, "
            "systems integration, software rollouts, operations, and Python/Django delivery."
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
        title="Python, Django & AI Automation Projects | Jonathan Dreksler",
        description=(
            "Explore six detailed Python, Django, OCR, document-search, data, CRM, "
            "and workflow-automation case studies built by Jonathan Dreksler."
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
        title="AI Automation & Technical Delivery Services | Jonathan Dreksler",
        description=(
            "Practical AI workflow automation, Python and Django systems integration, "
            "and technical project management for operational teams."
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
        description=service["description"],
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
        title="Contact Jonathan Dreksler | Technical Projects & Automation",
        description=(
            "Contact Jonathan Dreksler about technical project management, AI workflow "
            "automation, Python/Django systems integration, or operational delivery."
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
    path = reverse("portfolio:case_study", kwargs={"slug": project["name"].lower()})
    description = (
        f"{project['name']} case study: {project['description']} "
        "See the problem, workflow, technical decisions, results, and planned improvements."
    )
    article = {
        "@type": "TechArticle",
        "@id": f"{absolute_url(path)}#article",
        "headline": f"{project['name']} technical case study",
        "description": description,
        "url": absolute_url(path),
        "image": image_url(f"portfolio/projects/{project['name'].lower()}.png"),
        "author": {"@id": PERSON_ID},
        "dateModified": "2026-08-02",
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
