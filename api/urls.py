from django.urls import path

from .gallery import GetImages

urlpatterns = [
    path('gallery/images', GetImages.as_view())
]