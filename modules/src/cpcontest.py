import requests
from templates.text import TextTemplate
from templates.button import ButtonTemplate


def process(input, entities):
    output = {}
    try:

        r = requests.get('https://cpcontest-api.herokuapp.com/')
        data = r.json()

        buttons = ButtonTemplate()

        # Number of results to be displayed
        num = 3
        for contest in data['result']['upcoming_contests']:
            buttons.add_web_url(contest['Name'], contest['url'])
            num -= 1
            if num == 0:
                break

        output['input'] = input
        output['output'] = buttons.get_message()
        output['success'] = True
    except:
        error_message = 'There was some error while retrieving data.'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
