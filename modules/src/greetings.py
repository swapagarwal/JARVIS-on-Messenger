import json
import os

import config
import modules
import datetime
import calendarific
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate

CALENDARIFIC_API_KEY = os.environ.get('CALENDARIFIC_API_KEY', config.CALENDARIFIC_API_KEY)
def process(input, entities):
    output = {}
    
    try:
        d = datetime.datetime.today()
        calapi = calendarific.v2(CALENDARIFIC_API_KEY)
        parameters = {
            # Required
            'country': 'US',
            'year':    d.year,
            'month': d.month,
            'day': d.day
        }

        f_date = d.strftime('%m-%d-%Y') 

        request = calapi.holidays(parameters)
        all_holidays = []
        holiday_str = ""
        for h in request['response']['holidays']:
            holiday_str += "Happy " + h['name'] + "!\n"
        output['output'] = TextTemplate(
            'Today is {}, {}'.format(f_date, holiday_str)).get_message()

        output['success'] = True
    except:
        output['success'] = False
    return output
