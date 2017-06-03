from django.contrib import admin
from .models import ImageInfo


# Register your models here.
class ImageInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'detail', 'image')
    search_fields = ('title', 'detail', 'image')

admin.site.register(ImageInfo, ImageInfoAdmin)
