import urllib2
import json
from random import randint

import modules
from templates.generic import *

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0"}

#aww pulls top 25 posts from reddit.com/r/aww and serves the receipient a random image
def process(input, entities):
    output = {}

    request = urllib2.Request('https://www.reddit.com/r/aww/top.json?count=N&after=t3_XXXXX', None, headers)
    data = urllib2.urlopen(request)
    json_data = json.load(data)

    #request returns json array of 24 indicies (HOT posts from r/aww)
    r = randint(0, 24)

    post_title =  json_data['data']['children'][r]['data']['title']
    post_thumbnail = json_data['data']['children'][r]['data']['thumbnail']
    post_url = json_data['data']['children'][r]['data']['url']

    template = GenericTemplate()
    template.set_image_aspect_ratio_to_square()
    template.add_element(title=post_title, image_url=post_url)

    message = template.get_message()

    output = {
        'input': input,
        'output': message,
        'success': True
    }

    return output
