# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='YouTubeChannel',
            fields=[
                ('id', models.CharField(max_length=100, serialize=False, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='YouTubeVideo',
            fields=[
                ('video_id', models.CharField(max_length=50, unique=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('pub_date', models.DateTimeField()),
                ('channel', models.ForeignKey(to='ytrss.YouTubeChannel')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
