from copy import deepcopy as copy
from button import ButtonTemplate
ButtonTemplate.get_buttons = lambda self: self.template['attachment']['payload']['buttons']

TITLE_CHARACTER_LIMIT = 80
SUBTITLE_CHARACTER_LIMIT = 80
BUTTON_TITLE_CHARACTER_LIMIT = 20
BUTTON_LIMIT = 3
ELEMENTS_LIMIT = 4

template = {
    'template_type': 'list',
    'value': {
        'attachment': {
            'type': 'template',
            'payload': {
                'template_type': 'list',
                'top_element_style': 'compact',
                'elements': []
            }
        }
    }
}


class ListTemplate:
    def __init__(self, top_element_style=''):
        self.template = copy(template['value'])
        self.elements = []
        if top_element_style!= '':
            self.template['attachment']['payload']['top_element_style'] = top_element_style

    def add_element(self, title='', image_url='', subtitle='', buttons=[], default_action={}):
        element = {}
        element['title'] = title[:TITLE_CHARACTER_LIMIT]
        # won't render without an image_url
        element['image_url'] = image_url
        if subtitle != '':
            element['subtitle'] = subtitle[:SUBTITLE_CHARACTER_LIMIT]

        for button in buttons:
            button['title'] = button['title'][:BUTTON_TITLE_CHARACTER_LIMIT]
        if len(buttons) > 0:
            element['buttons'] = buttons[:BUTTON_LIMIT]
        if len(default_action) > 0:
            element['default_action'] = default_action
        if len(self.elements) < ELEMENTS_LIMIT:
            self.elements.append(element)

    def get_message(self):
        self.template['attachment']['payload']['elements'] = self.elements
        return self.template