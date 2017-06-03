# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20170604_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='origin_image',
            field=models.ImageField(upload_to='', height_field='url_height', width_field='url_width', verbose_name='원본이미지'),
        ),
    ]
