from urlparse import urlparse

import requests

from templates.generic import *
from templates.text import TextTemplate


def process(input, entities):
    output = {}
    try:
        url = entities['url'][0]['value']
        if not urlparse(url).scheme:
            url = "https://" + url
        hostname = urlparse(url).hostname
        if hostname is None:
            raise Exception("Please enter a valid hostname to check availability.")
        r = requests.get('https://isitup.org/' + hostname + '.json')
        data = r.json()

        status = data['status_code']
        if status == 1:
            text = hostname + ' is up.'
            image_url = 'http://fa2png.io/media/icons/font-awesome/4-7-0/check-circle/256/0/27ae60_none.png'
        elif status == 2:
            text = hostname + ' seems to be down!'
            image_url = 'http://fa2png.io/media/icons/font-awesome/4-7-0/times-circle/256/0/c0392b_none.png'
        elif status == 3:
            text = 'Please enter a valid domain to check availability.'
            image_url = 'http://fa2png.io/media/icons/font-awesome/4-7-0/exclamation-circle/256/0/f1c40f_none.png'
        else:
            raise Exception("Something unexpected happened!")

        buttons = ButtonTemplate()
        buttons.add_web_url('View more info', 'https://isitup.org/' + hostname)
        buttons.add_web_url('Go to website', hostname)

        template = GenericTemplate()
        template.set_image_aspect_ratio_to_square()
        template.add_element(title=text, image_url=image_url, buttons=buttons.get_buttons())

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'There seems to be a problem looking up that domain.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n - is google.com up'
        error_message += '\n - google.com status'
        error_message += '\n - ping google.com'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
