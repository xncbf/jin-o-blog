# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20170607_2330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='resized_image',
            field=models.ImageField(verbose_name='리사이징 이미지', upload_to='', editable=False),
        ),
        migrations.AlterField(
            model_name='imageinfo',
            name='thumbnail_image',
            field=models.ImageField(verbose_name='썸네일', upload_to='', editable=False),
        ),
    ]
