import config
import modules
from templates.text import TextTemplate

from datetime import datetime, timedelta
from time import strptime

def calculate_time(input_time=None): #Input must be in hh:mm format
    hours = [9, 7, 6, 4] 
    minutes = [0, 30, 0, 30] # The formula is based on www.sleepyti.me
    answer = []
    user_input = []
    _hour = 0
    _minute = 0

    if not input_time: #if user did not input any time 
        user_input.append(datetime.now().hour)
        user_input.append(datetime.now().minute)
    else:
        constructed_time = strptime(input_time, '%H:%M') # extract time from string to tuple of datetime format
        user_input.append(constructed_time[3])
        user_input.append(constructed_time[4])

    for i in range(4):
        _hour = user_input[0]
        _minute = user_input[1]
        output = ''
            
        if _hour - hours[i] < 0: #if time output will be a day before 
            _hour =+ 24

        if _minute - minutes[i] < 0: #if minute output will be an hour before
            _minute =+ 60

        output = timedelta(hours=_hour - hours[i], minutes=_minute - minutes[i]).__str__() #reconstruct to hh:mm format
        answer.append(output)
    
    return 'The best time to sleep is ' + answer[0] + '. \n' + 'You may also sleep at: ' + answer[1] + ", " + answer[2] + ", " + answer[3] + "."

def process(input, entities=None):
    output = {}
    try:
        
        assert('at' in entities)
        text_i_want_returned = calculate_time(entities['at'][0]['value'])
        
        message = TextTemplate(text_i_want_returned).get_message()
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        error_message = 'I couldn\'t perform that action.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - I want to wake up at 07:00'
        error_message += '\n  - I have to wake up at 04:25'
        error_message += '\n  - Wake up at 10:10'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output