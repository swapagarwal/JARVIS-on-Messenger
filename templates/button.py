from copy import deepcopy as copy

from text import TextTemplate

TextTemplate.get_text = lambda self: self.get_message()['text']

TEXT_CHARACTER_LIMIT = 320

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
        web_url_button = {'type': 'web_url', 'title': title, 'url': url}
        self.template['attachment']['payload']['buttons'].append(web_url_button)

    def add_postback(self, title='', payload=''):
        postback_button = {'type': 'postback', 'title': title, 'payload': payload}
        self.template['attachment']['payload']['buttons'].append(postback_button)

    def set_text(self, text=''):
        self.text = text

    def get_message(self):
        self.template['attachment']['payload']['text'] = self.text
        return self.template
