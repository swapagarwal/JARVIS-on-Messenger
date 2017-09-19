import json
from copy import deepcopy as copy

from text import TextTemplate

TextTemplate.get_text = lambda self: self.get_message()['text']

TEXT_CHARACTER_LIMIT = 640

template = {
    'template_type': 'button',
    'value': {
        'attachment': {
            'type': 'template',
            'payload': {
                'template_type': 'button',
                'text': '',
                'buttons': []
            }
        }
    }
}


class ButtonTemplate:
    def __init__(self, text=''):
        self.template = copy(template['value'])
        self.text = text

    def add_web_url(self, title='', url=''):
        web_url_button = {}
        web_url_button['type'] = 'web_url'
        web_url_button['title'] = title
        web_url_button['url'] = url
        self.template['attachment']['payload']['buttons'].append(web_url_button)

    def add_postback(self, title='', payload=''):
        postback_button = {}
        postback_button['type'] = 'postback'
        postback_button['title'] = title
        postback_button['payload'] = json.dumps(payload)
        self.template['attachment']['payload']['buttons'].append(postback_button)

    def set_text(self, text=''):
        self.text = text

    def get_message(self):
        self.template['attachment']['payload']['text'] = self.text
        return self.template
