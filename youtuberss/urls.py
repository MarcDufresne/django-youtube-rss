from django.conf.urls import patterns, include, url
# from django.contrib import admin
from ytrss.feed import YouTubeRSSFeed

urlpatterns = patterns('',

    url(r'^videos/(?P<channel_name>[a-zA-Z0-9]+)/?$', YouTubeRSSFeed()),
    url(r'^videos/(?P<channel_name>[a-zA-Z0-9]+)/(?P<filter>[a-zA-Z0-9?%&*!_ -():;,.\[\]\{\}\"\'|+#]+)/?$',
        YouTubeRSSFeed()),
)
