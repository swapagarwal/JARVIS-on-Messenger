import os

import requests
import requests_cache

import config
from templates.generic import *
from templates.text import TextTemplate
from utils.YouTube import YouTubeUtil

YOUTUBE_DATA_API_KEY = os.environ.get('YOUTUBE_DATA_API_KEY', config.YOUTUBE_DATA_API_KEY)

class TrendingUtil:
    @staticmethod
    def get_trending(regionCode):
        output = {}
        try:
            with requests_cache.enabled('video_cache', backend='sqlite', expire_after=3600):
                r = requests.get(
                    'https://www.googleapis.com/youtube/v3/videos?part=snippet&chart=mostPopular&regionCode='+regionCode.upper()+'&maxResults=10&key=' + YOUTUBE_DATA_API_KEY)
                data = r.json()
            template = GenericTemplate()
            videos = [item for item in data['items'] if item['kind'] == 'youtube#video']
            for item in videos:
                title = item['snippet']['title']
                item_url = YouTubeUtil.get_video_url(item['id'])
                image_url = item['snippet']['thumbnails']['high']['url']
                subtitle = item['snippet']['channelTitle']
                buttons = ButtonTemplate()
                buttons.add_web_url('YouTube Link', item_url)
                buttons.add_web_url('Channel Link', YouTubeUtil.get_channel_url(item['snippet']['channelId']))
                template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=subtitle,
                                    buttons=buttons.get_buttons())
            output['input'] = input
            output['output'] = template.get_message()
            output['success'] = True
        except:
            error_message = 'I couldn\'t find any trending videos in that region.'
            error_message += '\nPlease ask me something else, like:'
            error_message += '\n  - trending videos US'
            error_message += '\n  - trending videos MX'
            error_message += '\n  - trending videos JP'
            output['error_msg'] = TextTemplate(error_message).get_message()
            output['success'] = False
        return output
