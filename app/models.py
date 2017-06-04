from django.db import models


# Create your models here.
class ImageInfo(models.Model):
    image = models.ImageField('이미지')
    title = models.CharField('제목', max_length=500)
    detail = models.CharField('내용', max_length=500)

    class Meta:
        verbose_name = "이미지"
