import os

import requests
import datetime
import config
from templates.text import TextTemplate

STOCKS_API_KEY = os.environ.get('STOCKS_API_KEY', config.STOCKS_API_KEY)


def process(input, entities):
    output = {}
    try:
        r = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol=" + entities[0]['value'] + "&apikey=" + STOCKS_API_KEY)
        json_form = r.json() 
        lastBusDay = datetime.datetime.today()
        print("hello")
        if datetime.date.weekday(lastBusDay) == 5:      #if it's Saturday
            lastBusDay = lastBusDay - datetime.timedelta(days = 1) #then make it Friday
        elif datetime.date.weekday(lastBusDay) == 6:      #if it's Sunday
            lastBusDay = lastBusDay - datetime.timedelta(days = 2); #then make it Friday
        curr_date = ""
        curr_date += str(lastBusDay.year) + "-" + str(lastBusDay.month) + "-" + str(lastBusDay.day)

        last_close = json_form["Time Series (Daily)"][curr_date]["4. close"]
        output['input'] = input
        output['output'] = TextTemplate(
            'Latest Closing Price: $' + last_close).get_message()
        output['success'] = True
    except:
        error_message = "Sorry there was an error. You may have entered an invalid stock ticker. Please try again."
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
