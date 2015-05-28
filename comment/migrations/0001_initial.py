# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.CharField(max_length=255, verbose_name='Comment')),
                ('com_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Creation')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('video', models.ForeignKey(to='video.Video')),
            ],
        ),
    ]
