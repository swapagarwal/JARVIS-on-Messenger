template = {
    'template_type': 'image',
    'value': {
        'attachment': {
            'type': 'image',
            'payload': {
                'url': ''
            }
        }
    }
}

class ImageTemplate:
    def __init__(self, url=''):
        self.template = template['value']
        self.url = url
    def set_url(self, url=''):
        self.url = url
    def get_message(self):
        self.template['attachment']['payload']['url'] = self.url
        return self.template
