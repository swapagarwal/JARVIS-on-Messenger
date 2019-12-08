import json


import config
import modules
import datetime
import holidays
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate


def process(input, entities):
    output = {}
    try:
        us_holidays = holidays.UnitedStates()
        d = datetime.datetime.today()
        f_date = d.strftime('%m-%d-%Y') 
        f_date = '1-1-2019'
        output['success'] = True
        if f_date in us_holidays:
            output['output'] = TextTemplate(
                'Today is {}, Happy {}!'.format(f_date, us_holidays.get(f_date))).get_message()
        else:
            output['output'] = TextTemplate(
                'Today is {}'.format(f_date) ).get_message()
        output['success'] = True
    except:
        output['success'] = False
    return output
