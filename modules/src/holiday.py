import modules
import datetime
from datetime import date
import holidays

def process(input, entities=None):
    output = {}
    try:
        now = datetime.datetime.now()
        us_holidays = holidays.US()
        while 1:
            if date(now.year, now.month, now.day) in us_holidays:
        	    output['output'] = us_holidays[date(now.year, now.month, now.day)]
        	    output['success'] = True
        	    break
            else:
                now += datetime.timedelta(days=1)
    except:
        output['success'] = False
    return output
