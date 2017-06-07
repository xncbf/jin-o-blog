from django.db import models
from sorl.thumbnail import ImageField, get_thumbnail


# Create your models here.
class ImageInfo(models.Model):
    origin_image = models.ImageField('원본이미지')
    resized_image = models.ImageField('리사이징 이미지', editable=False)
    thumbnail_image = models.ImageField('썸네일', editable=False)
    title = models.CharField('제목', max_length=500)
    detail = models.CharField('내용', max_length=500)

    class Meta:
        verbose_name = "이미지"

    def save(self, *args, **kwargs):
        if self.origin_image:
            # self.origin_image = get_thumbnail(self.image, '1920x1281', quality=99)
            self.resized_image = get_thumbnail(self.origin_image, '1920x1281', quality=100).url
            self.thumbnail_image = get_thumbnail(self.origin_image, '215x143', quality=100).url
        super(ImageInfo, self).save(*args, **kwargs)
