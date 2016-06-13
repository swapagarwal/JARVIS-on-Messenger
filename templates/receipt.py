from copy import deepcopy as copy

template = {
    'template_type': 'receipt',
    'value': {
        'attachment': {
            'type': 'template',
            'payload': {
                'template_type': 'receipt',
                'recipient_name': '',
                'order_number': '',
                'currency': '',
                'payment_method': ''
            }
        }
    }
}

class ReceiptTemplate:
    def __init__(self, recipient_name='', order_number='', currency='', payment_method='', timestamp='', order_url=''):
        self.template = copy(template['value'])
        self.template['attachment']['payload']['recipient_name'] = recipient_name
        self.template['attachment']['payload']['order_number'] = order_number
        self.template['attachment']['payload']['currency'] = currency
        self.template['attachment']['payload']['payment_method'] = payment_method
        self.template['attachment']['payload']['timestamp'] = timestamp
        self.template['attachment']['payload']['order_url'] = order_url
        self.elements = []
        self.address = {}
        self.summary = {}
        self.adjustments = []
    def add_element(self, title='', subtitle='', quantity=-1, price=0, currency='', image_url=''):
        element = {}
        element['title'] = title
        element['subtitle'] = subtitle
        element['quantity'] = quantity
        element['price'] = price
        element['currency'] = currency
        element['image_url'] = image_url
        self.elements.append(element)
    def set_address(self, street_1='', street_2='', city='', postal_code='', state='', country=''):
        self.address['street_1'] = street_1
        self.address['street_2'] = street_2
        self.address['city'] = city
        self.address['postal_code'] = postal_code
        self.address['state'] = state
        self.address['country'] = country
    def set_summary(self, subtotal=-1, shipping_cost=-1, total_tax=-1, total_cost=0):
        self.summary['subtotal'] = subtotal
        self.summary['shipping_cost'] = shipping_cost
        self.summary['total_tax'] = total_tax
        self.summary['total_cost'] = total_cost
    def add_adjustment(self, name='', amount=0):
        adjustment = {}
        adjustment['name'] = name
        adjustment['amount'] = amount
        self.adjustments.append(adjustment)
    def get_message(self):
        self.template['attachment']['payload']['elements'] = self.elements
        self.template['attachment']['payload']['address'] = self.address
        self.template['attachment']['payload']['summary'] = self.summary
        self.template['attachment']['payload']['adjustments'] = self.adjustments
        return self.template
