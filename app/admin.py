from django.contrib import admin
from .models import ImageInfo


# Register your models here.
class ImageInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'origin_image', 'thumbnail')
    search_fields = ('title', 'detail', 'origin_image', 'thumbnail')

admin.site.register(ImageInfo, ImageInfoAdmin)
