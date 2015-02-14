# Django RSS app for YouTube

## Setup

1. Create a `secret_key` file in the root of the repo and add your Django secret key inside
2. Create a `yt_api_key` file and add your YouTube API key inside
3. Run `pip install django google-api-python-client` in your virtual env
4. Run `./manage.py syncdb`

## How to use

Once the setup is done and your server is running,
go to `/videos/<channel_username>` to get the RSS Feed of recent videos
