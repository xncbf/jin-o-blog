# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('origin_image', models.ImageField(verbose_name='원본이미지', upload_to='')),
                ('thumbnail', models.ImageField(verbose_name='썸네일', upload_to='')),
                ('title', models.CharField(verbose_name='제목', max_length=500)),
                ('detail', models.CharField(verbose_name='내용', max_length=500)),
            ],
        ),
    ]
