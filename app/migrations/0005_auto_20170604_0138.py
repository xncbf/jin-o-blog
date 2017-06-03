# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20170604_0118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageinfo',
            name='origin_image',
        ),
        migrations.RemoveField(
            model_name='imageinfo',
            name='thumbnail',
        ),
        migrations.AddField(
            model_name='imageinfo',
            name='image',
            field=models.ImageField(verbose_name='이미지', default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
