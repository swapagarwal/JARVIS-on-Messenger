template = {
    'template_type': 'attachment',
    'value': {
        'attachment': {
            'type': 'file',
            'payload': {
                'url': ''
            }
        }
    }
}


class AttachmentTemplate:
    def __init__(self, url='', type='file'):
        self.template = template['value']
        self.url = url
        self.type = type

    def set_url(self, url=''):
        self.url = url

    def set_type(self, type=''):
        # image / audio / video / file
        self.type = type

    def get_message(self):
        self.template['attachment']['payload']['url'] = self.url
        self.template['attachment']['type'] = self.type
        return self.template
