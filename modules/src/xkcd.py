import requests
from random import randint
from datetime import datetime, timedelta, date
from templates.generic import *
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        start_date = date(2016, 12, 7)
        today = date.today()
        start_num = 1769

        mwf_count = 0
        for d in range(1, (today - start_date).days):
            cur_date = start_date + timedelta(days=d)
            if cur_date.weekday() in [0, 2, 4]:
                mwf_count = mwf_count + 1

        max_num = start_num + mwf_count

        r = requests.get('http://xkcd.com/%d/info.0.json' % randint(1, max_num) )
        data = r.json()


        title = data['title']
        item_url = 'http://xkcd.com/' + str(data['num']) + '/'
        image_url = data['img'].replace('\\', '')
        subtitle = data['alt']


        template = GenericTemplate()
        template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=subtitle, buttons=[])

        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'There was some error while retrieving data from xkcd.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
