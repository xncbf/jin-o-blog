# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='origin_image',
            field=models.ImageField(width_field=1440, height_field=950, upload_to='', verbose_name='원본이미지'),
        ),
    ]
