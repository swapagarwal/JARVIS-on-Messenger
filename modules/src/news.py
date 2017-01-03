import requests
import config
import os
from templates.generic import *
from templates.text import TextTemplate

NEWS_API_KEY = os.environ.get('NEWS_API_KEY', config.NEWS_API_KEY)

def process(input, entities=None):
    output = {}
    source = 'google-news'
    try:
        r = requests.get('https://newsapi.org/v1/articles?source=' +  source + '&apiKey=' + NEWS_API_KEY)
        data = r.json()
        assert(len(data["articles"]) > 0)
        template = GenericTemplate()
        for article in data['articles']:
            title = article['title']
            description = article['description']
            url = article['url']
            buttons = ButtonTemplate()
            buttons.add_web_url('Powered by NewsAPI', 'https://newsapi.org/')
            template.add_element(title=title, item_url=url, subtitle=description, buttons=buttons.get_buttons())
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t perform that action.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - latest news'
        error_message += '\n  - world news'
        error_message += '\n  - news'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
