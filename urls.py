from django.conf import settings
from django.urls import include, path
from django.contrib import admin
from django.conf.urls.static import static
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('wagtail/', include(wagtailadmin_urls)),
    path('', include(wagtail_urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
