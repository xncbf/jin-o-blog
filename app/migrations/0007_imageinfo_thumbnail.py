# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20170607_2257'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageinfo',
            name='thumbnail',
            field=models.ImageField(editable=False, verbose_name='썸네일', upload_to='', default=1),
            preserve_default=False,
        ),
    ]
