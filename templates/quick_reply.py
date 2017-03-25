from copy import deepcopy as copy

template = {
    'template_type': 'quick_reply',
    'value': {
      "quick_replies":[
      ]
    }
}

class QuickReplyTemplate:
    def __init__(self, text=''):
        self.template = copy(template['value'])
        self.text = text
    def add_quick_reply(self, title='', payload=''):
        quick_reply = {}
        quick_reply['content_type'] = 'text'
        quick_reply['title'] = title
        quick_reply['payload'] = payload
        self.template['quick_replies'].append(quick_reply)
    def set_text(self, text=''):
        self.text = text
    def get_message(self):
        self.template['text'] = self.text
        return self.template
