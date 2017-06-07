# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170604_0138'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imageinfo',
            options={'verbose_name': '이미지'},
        ),
    ]
