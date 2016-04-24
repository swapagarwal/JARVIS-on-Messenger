from copy import copy

button = {
    'type': '',
    'title': '',
    'url': '',
    'payload': ''
}

def web_url(title, url):
    web_url_button = copy(button)
    web_url_button['type'] = 'web_url'
    web_url_button['title'] = title
    web_url_button['url'] = url
    return web_url_button

def postback(title, payload):
    postback_button = copy(button)
    postback_button['type'] = 'postback'
    postback_button['title'] = title
    postback_button['payload'] = payload
    return postback_button

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
        self.template = template['value']
        self.text = text
    def add_web_url(self, title='', url=''):
        web_url_button = web_url(title, url)
        self.template['attachment']['payload']['buttons'].append(web_url_button)
    def add_postback(self, title='', payload=''):
        postback_button = postback(title, payload)
        self.template['attachment']['payload']['buttons'].append(postback_button)
    def set_text(self, text=''):
        self.text = text
    def get_message(self):
        self.template['attachment']['payload']['text'] = self.text
        return self.template
