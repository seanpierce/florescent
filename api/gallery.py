import json

from django.http import HttpResponse
from django.views.generic import View

from repositories.gallery import GalleryRepository as repo

class GetImages(View):
    """
    Gets Gallery Images.
    """
    def get(self, request, *args, **kwargs):
        return HttpResponse(json.dumps(repo.get_images()), content_type='application/json')