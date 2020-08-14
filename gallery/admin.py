from django.contrib import admin
from .models import Image

class ImageAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['alt_text', 'image']
    list_filter = ['created_at']
    list_display = ['image_preview', 'image', 'created_at']
    ordering = ['-created_at']

    def get_fields(self, request, obj=None):
        if obj is None:
            return ['alt_text', 'image']
        return ['image_preview', 'created_at', 'alt_text', 'image']

    readonly_fields = ['image_preview', 'created_at']

admin.site.register(Image, ImageAdmin)