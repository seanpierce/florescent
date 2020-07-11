from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='media/')

class Image(models.Model):
    """
    Django model for the gallery.image object.
    """
    
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255, default=None)
    image = models.ImageField(storage=fs, max_length=1000)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return self.title if self.title is not None else self.id

