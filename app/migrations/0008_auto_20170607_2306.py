# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_imageinfo_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageinfo',
            name='thumbnail',
            field=models.ImageField(upload_to='', null=True, editable=False, verbose_name='썸네일'),
        ),
    ]
