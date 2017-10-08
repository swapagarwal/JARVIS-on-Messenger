import requests
import json
import traceback

from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        word = entities[0]['word']
        r = requests.get("https://api.urbandictionary.com" + \
                         "/v0/define?term={}".format(word))
        response = json.loads(r.content)
        if response["result_type"] == "no_results":
            output['input'] = input
            error_message = "There aren't any definitions for " + str(word) + \
                            " on the Urban Dictionary."
            output['error_msg'] = TextTemplate(error_message).get_message()
            output['success'] = False
            return output
        meaning = response["list"][0]["definition"].replace("\r\n", "")
        response = 'Urban Dictionary definition for ' + word + ':\n'
        response += meaning
        output['input'] = input
        output['output'] = TextTemplate(response).get_message()
        output['success'] = True
    except:
        error_message = str(traceback.format_exc())
        # error_message = 'Something went wrong.'
        # error_message += '\nPlease ask me something else, like:'
        # error_message += '\n  - urban rawr'
        # error_message += '\n  - rawr urban'
        # error_message += '\n  - slang rawr'
        # error_message += '\n  - rawr slang'
        output['input'] = input
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
