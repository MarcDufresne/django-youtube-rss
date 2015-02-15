# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from googleapiclient.discovery import build
from ytrss.constants import YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, YOUTUBE_API_KEY
from ytrss.models import YouTubeChannel, YouTubeVideo


def get_or_create_channel_from_name(channel_name):

    channel = None
    result_channel = None

    try:
        channel = YouTubeChannel.objects.get(name=channel_name)
    except YouTubeChannel.DoesNotExist:
        pass

    if not channel:
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

        result = youtube.channels().list(forUsername=channel_name, part='snippet').execute()

        items = result.get('items', [])
        channel_id = items[0].get('id')
        if channel_id:
            result_channel = YouTubeChannel()
            result_channel.id = channel_id
            result_channel.name = channel_name
            result_channel.save()

    else:
        result_channel = channel

    return result_channel


def create_videos_for_channel(channel):

    if not isinstance(channel, YouTubeChannel):
        raise ValueError('Channel should be a YouTubeChannel instance')

    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_API_KEY)

    result = youtube.search().list(
        order='date', part='snippet', channelId=channel.id, type='video', maxResults=25).execute()

    for item in result.get('items', []):
        video_id = item.get('id', {}).get('videoId')

        try:
            YouTubeVideo.objects.get(video_id=video_id)
            video_exists = True
        except YouTubeVideo.DoesNotExist:
            video_exists = False

        if not video_exists:
            video_title = item.get('snippet', {}).get('title')
            video_desc = item.get('snippet', {}).get('description')
            video_pub = item.get('snippet', {}).get('publishedAt')
            if video_id and video_desc and video_pub and video_title:
                video = YouTubeVideo(video_id=video_id, channel=channel, description=video_desc,
                                     title=video_title, pub_date=video_pub)
                video.save()