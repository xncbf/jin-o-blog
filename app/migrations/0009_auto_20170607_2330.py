# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20170607_2306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageinfo',
            name='image',
        ),
        migrations.RemoveField(
            model_name='imageinfo',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='imageinfo',
            name='origin_image',
            field=models.ImageField(verbose_name='원본이미지', default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageinfo',
            name='resized_image',
            field=models.ImageField(verbose_name='리사이징 이미지', default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageinfo',
            name='thumbnail_image',
            field=models.ImageField(verbose_name='썸네일', default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
