from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['alt_text', 'image']
    list_filter = ['created_at']

admin.site.register(Image, ImageAdmin)