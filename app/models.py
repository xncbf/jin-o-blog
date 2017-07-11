from django.db import models
from imagekit.models import ProcessedImageField, ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit, SmartResize


# Create your models here.
class ImageInfo(models.Model):
    origin_image = models.ImageField('원본이미지')
    # resized_image = models.ImageField('리사이징', editable=False)
    resized_image = ImageSpecField(source='origin_image',
                                   processors=[ResizeToFit(1920, 1281, mat_color=(255, 255, 255))],
                                   options={'quality': 100},)
    # thumbnail_image = models.ImageField('썸네일', editable=False)
    thumbnail_image = ImageSpecField(source='origin_image',
                                     processors=[ResizeToFit(215, 143, mat_color=(255, 255, 255))],
                                     options={'quality': 95},)
    title = models.CharField('제목', max_length=500)
    detail = models.CharField('내용', max_length=500, blank=True)

    class Meta:
        verbose_name = "이미지"

    def save(self, *args, **kwargs):
        # if self.origin_image:
            # self.origin_image = get_thumbnail(self.image, '1920x1281', qualit
            # self.resized_image = self._resized_image
            # self.thumbnail_image = self._thumbnail_image
        super(ImageInfo, self).save(*args, **kwargs)
