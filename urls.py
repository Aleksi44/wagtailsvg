from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls

try:
    from wagtail import urls as wagtail_urls
except ImportError:
    from wagtail.core import urls as wagtail_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wagtail/', include(wagtailadmin_urls)),
    path('', include(wagtail_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
