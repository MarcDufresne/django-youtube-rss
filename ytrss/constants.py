# -*- coding: utf-8 -*-

from __future__ import unicode_literals, absolute_import
from youtuberss import settings


YOUTUBE_API_KEY = settings.YOUTUBE_API_KEY
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

YOUTUBE_CHANNEL_URL_FORMAT = "https://www.youtube.com/user/{}"
YOUTUBE_VIDEO_URL_FORMAT = "https://www.youtube.com/watch?v={}"