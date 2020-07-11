from gallery.models import Image

class GalleryRepository:
    """
    Data access layer for Gallery models.
    """

    @staticmethod
    def get_images():
        return list(Image.objects
            .order_by('created_at')
            .values('id', 'title', 'image'))