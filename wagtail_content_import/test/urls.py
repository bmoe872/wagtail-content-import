from django.conf.urls import include, url
from django.contrib import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail.core import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

from wagtail_content_import import urls as wagtail_content_import_urls

urlpatterns = [
    url(r'', include(wagtail_content_import_urls)),
    url(r"^django-admin/", admin.site.urls),
    url(r"^admin/", include(wagtailadmin_urls)),
    url(r"^documents/", include(wagtaildocs_urls)),
    url(r"", include(wagtail_urls)),
]
