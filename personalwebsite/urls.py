from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path('', include('portfolio.urls')),
]

# Admin is disabled by default to reduce attack surface.
# Set DJANGO_ENABLE_ADMIN=1 in the environment to enable it.
if settings.ADMIN_ENABLED:
    from django.contrib import admin
    urlpatterns.insert(0, path('admin/', admin.site.urls))

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
