# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='Title', max_length=255)),
                ('desc', models.CharField(verbose_name='Description', max_length=1024)),
                ('upload_time', models.DateTimeField(verbose_name='Upload date', default=django.utils.timezone.now)),
                ('video_clip', models.FileField(upload_to='video')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
