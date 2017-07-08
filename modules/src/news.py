import os

import requests

import config
from templates.generic import *
from templates.text import TextTemplate

NEWS_API_KEY = os.environ.get('NEWS_API_KEY', config.NEWS_API_KEY)


def process(input, entities=None):
    output = {}
    source = 'google-news'  # Can add more sources in future
    try:
        r = requests.get('https://newsapi.org/v1/articles?source=' + source + '&apiKey=' + NEWS_API_KEY)
        data = r.json()
        assert (len(data['articles']) > 0)
        template = GenericTemplate()
        for article in data['articles']:
            title = article['title']
            description = article['description']
            url = article['url']
            url_to_image = article['urlToImage']
            buttons = ButtonTemplate()
            buttons.add_web_url('Read more...', url)
            buttons.add_web_url('Powered by NewsAPI', 'https://newsapi.org/')
            template.add_element(title=title, item_url=url, image_url=url_to_image, subtitle=description,
                                 buttons=buttons.get_buttons())
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'There was some error while retrieving data from NewsAPI.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
