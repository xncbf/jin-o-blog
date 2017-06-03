# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170604_0111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='origin_image',
            field=models.ImageField(height_field='url_height', verbose_name='원본이미지', width_field='url_width', upload_to='images/fulls/'),
        ),
        migrations.AlterField(
            model_name='imageinfo',
            name='thumbnail',
            field=models.ImageField(verbose_name='썸네일', upload_to='images/thumbs/'),
        ),
    ]
