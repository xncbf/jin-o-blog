# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('app', '0001_initial'), ('app', '0002_auto_20170608_1021'), ('app', '0003_auto_20170608_1032'), ('app', '0004_auto_20170608_1046'), ('app', '0005_auto_20170608_1118'), ('app', '0006_auto_20170608_1125'), ('app', '0007_auto_20170608_1126'), ('app', '0008_auto_20170608_1255')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('origin_image', models.ImageField(verbose_name='원본이미지', upload_to='')),
                ('title', models.CharField(verbose_name='제목', max_length=500)),
                ('detail', models.CharField(verbose_name='내용', blank=True, max_length=500)),
            ],
            options={
                'verbose_name': '이미지',
            },
        ),
    ]
