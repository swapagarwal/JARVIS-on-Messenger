from copy import deepcopy as copy

from button import ButtonTemplate

ButtonTemplate.get_buttons = lambda self: self.template['attachment']['payload']['buttons']

TITLE_CHARACTER_LIMIT = 80
SUBTITLE_CHARACTER_LIMIT = 80
BUTTON_TITLE_CHARACTER_LIMIT = 20
BUTTON_LIMIT = 3
ELEMENTS_LIMIT = 10

template = {
    'template_type': 'generic',
    'value': {
        'attachment': {
            'type': 'template',
            'payload': {
                'template_type': 'generic',
                'image_aspect_ratio': 'horizontal',
                'elements': []
            }
        }
    }
}


class GenericTemplate:
    def __init__(self):
        self.template = copy(template['value'])
        self.elements = []

    def set_image_aspect_ratio_to_square(self):
        self.template['attachment']['payload']['image_aspect_ratio'] = 'square'

    def add_element(self, title='', item_url='', image_url='', subtitle='', buttons=[]):
        element = {}
        element['title'] = title[:TITLE_CHARACTER_LIMIT]
        if item_url != '':
            element['item_url'] = item_url
        element['image_url'] = image_url
        if subtitle != '':
            element['subtitle'] = subtitle[:SUBTITLE_CHARACTER_LIMIT]
        for button in buttons:
            button['title'] = button['title'][:BUTTON_TITLE_CHARACTER_LIMIT]
        if len(buttons) > 0:
            element['buttons'] = buttons[:BUTTON_LIMIT]
        if len(self.elements) < ELEMENTS_LIMIT:
            self.elements.append(element)

    def get_message(self):
        self.template['attachment']['payload']['elements'] = self.elements
        return self.template
