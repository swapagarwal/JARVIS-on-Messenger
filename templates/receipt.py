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
        if timestamp != '':
            self.template['attachment']['payload']['timestamp'] = timestamp
        if order_url != '':
            self.template['attachment']['payload']['order_url'] = order_url
        self.elements = []
        self.address = {}
        self.summary = {}
        self.adjustments = []

    def add_element(self, title='', subtitle='', quantity=-1, price=0, currency='', image_url=''):
        element = {}
        element['title'] = title
        if subtitle != '':
            element['subtitle'] = subtitle
        if quantity != -1:
            element['quantity'] = quantity
        element['price'] = price
        if currency != '':
            element['currency'] = currency
        if image_url != '':
            element['image_url'] = image_url
        self.elements.append(element)

    def set_address(self, street_1='', street_2='', city='', postal_code='', state='', country=''):
        self.address['street_1'] = street_1
        if street_2 != '':
            self.address['street_2'] = street_2
        self.address['city'] = city
        self.address['postal_code'] = postal_code
        self.address['state'] = state
        self.address['country'] = country

    def set_summary(self, subtotal=-1, shipping_cost=-1, total_tax=-1, total_cost=0):
        if subtotal != -1:
            self.summary['subtotal'] = subtotal
        if shipping_cost != -1:
            self.summary['shipping_cost'] = shipping_cost
        if total_tax != -1:
            self.summary['total_tax'] = total_tax
        self.summary['total_cost'] = total_cost

    def add_adjustment(self, name='', amount=0):
        adjustment = {}
        adjustment['name'] = name
        adjustment['amount'] = amount
        self.adjustments.append(adjustment)

    def get_message(self):
        self.template['attachment']['payload']['elements'] = self.elements
        if self.address != {}:
            self.template['attachment']['payload']['address'] = self.address
        self.template['attachment']['payload']['summary'] = self.summary
        if self.adjustments != []:
            self.template['attachment']['payload']['adjustments'] = self.adjustments
        return self.template
