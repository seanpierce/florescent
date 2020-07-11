from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from .views import index, gallery

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('gallery', gallery)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
