from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media/')

class Image(models.Model):
    """
    Django model for the gallery.image object.
    """
    
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    alt_text = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(storage=fs)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return str(self.image)