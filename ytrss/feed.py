# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from django.contrib.syndication.views import Feed
from django.http import Http404
from django.shortcuts import get_object_or_404
from ytrss.api import get_or_create_channel_from_name, create_videos_for_channel, get_or_create_channel_from_id
from ytrss.models import YouTubeVideo, YouTubeChannel


class YouTubeRSSFeed(Feed):

    filter = None
    get_by_id = False

    def __init__(self, get_by_id=False):
        self.get_by_id = get_by_id

    def get_object(self, request, **kwargs):
        self.filter = kwargs.get('filter')
        if self.get_by_id:
            channel_id = kwargs.get('channel_id')

            if channel_id:
                get_or_create_channel_from_id(channel_id)
                return get_object_or_404(YouTubeChannel, id=channel_id)
            else:
                raise Http404('Channel ID was not defined')
        else:
            channel_name = kwargs.get('channel_name')

            if channel_name:
                get_or_create_channel_from_name(channel_name)
                return get_object_or_404(YouTubeChannel, name=channel_name)
            else:
                raise Http404('Channel Name was not defined')

    def items(self, channel):
        create_videos_for_channel(channel)
        videos = YouTubeVideo.objects.filter(channel=channel).order_by('-pub_date')
        if self.filter:
            videos = videos.filter(title__icontains=self.filter)
        return videos[:25]

    def item_title(self, video):
        return video.title

    def item_description(self, video):
        return video.description

    def item_link(self, video):
        return video.get_absolute_url()

    def title(self, channel):
        return "{}'s videos".format(channel.name)

    def description(self, channel):
        return "Most recent YouTube videos for {}".format(channel.name)

    def link(self, channel):
        return channel.get_absolute_url()