from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
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