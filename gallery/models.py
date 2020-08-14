from django.db import models
from django.core.files.storage import FileSystemStorage
from django.utils.html import mark_safe

fs = FileSystemStorage(location='media/')

class Image(models.Model):
    """
    Django model for the gallery.image object.
    """
    
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    alt_text = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(storage=fs)

    def image_preview(self):
            return mark_safe('<img src="/media/%s" height="150" />' % (self.image))

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return str(self.image)