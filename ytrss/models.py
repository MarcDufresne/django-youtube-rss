# -*- coding: utf-8 -*-
from django.db import models
from ytrss.constants import YOUTUBE_VIDEO_URL_FORMAT, YOUTUBE_CHANNEL_URL_FORMAT


class YouTubeChannel(models.Model):

    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        return YOUTUBE_CHANNEL_URL_FORMAT.format(self.id)


class YouTubeVideo(models.Model):

    video_id = models.CharField(primary_key=True, unique=True, max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField()
    channel = models.ForeignKey(YouTubeChannel)

    def get_absolute_url(self):
        return YOUTUBE_VIDEO_URL_FORMAT.format(self.video_id)