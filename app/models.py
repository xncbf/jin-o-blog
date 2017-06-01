from django.db import models


# Create your models here.
class ImageInfo(models.Model):
    origin_image = models.ImageField('원본이미지', )
    thumbnail = models.ImageField('썸네일', )
    title = models.CharField('제목', max_length=500)
    detail = models.CharField('내용', max_length=500)
