from django.contrib import admin
from .models import ImageInfo


# Register your models here.
class ImageInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'origin_image', 'resized_image')
    search_fields = ('title', 'detail', 'origin_image')

admin.site.register(ImageInfo, ImageInfoAdmin)
