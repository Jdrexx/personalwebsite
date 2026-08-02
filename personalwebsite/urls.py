from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from django.urls import include, path
from django.contrib.sitemaps.views import sitemap

from portfolio.sitemaps import CaseStudySitemap, ServiceSitemap, StaticSitemap
from portfolio.views import robots_txt

handler404 = 'portfolio.views.error_404'

sitemaps = {
    'static': StaticSitemap,
    'services': ServiceSitemap,
    'case-studies': CaseStudySitemap,
}

urlpatterns = [
    path('robots.txt', robots_txt, name='robots_txt'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('', include('portfolio.urls')),
]

# Admin is disabled by default. Set DJANGO_ADMIN_URL in the environment
# to a secret path (e.g. "mysecretadmin") and admin will be accessible
# at /mysecretadmin/ instead of /admin/.
if settings.ADMIN_URL:
    from django.contrib import admin
    urlpatterns.insert(0, path(f'{settings.ADMIN_URL}/', admin.site.urls))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Google Search Console verification
urlpatterns += [
    path('googled0311ec69bf9f0b1.html', lambda r: HttpResponse(
        'google-site-verification: googled0311ec69bf9f0b1.html',
        content_type='text/plain',
    )),
]
