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
            	message = "The nearest holiday is " + us_holidays[date(now.year, now.month, now.day)] + " on " + str(now.month) + "-" + str(now.day) + "-" + str(now.year)
        	    output['output'] = message
        	    output['success'] = True
        	    break
            else:
                now += datetime.timedelta(days=1)
    except:
        output['success'] = False
    return output
