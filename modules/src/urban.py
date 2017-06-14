import requests as rq
from bs4 import BeautifulSoup as bs
import re
import urllib

from templates.text import TextTemplate

def process(input, entities):
    output = {}
    try:
        orig_phrase = entities['phrase'][0]['value']
        phrase = urllib.quotes_plus(orig_phrase)
        page = rq.get("http://www.urbandictionary.com/define.php?term="+phrase)
        soup = bs(page.content, 'html.parser')
        meaning = soup.find('div', class_='meaning').text
        list_aux = meaning.split('.')
        if list_aux[0] == "\nThere aren't any definitions for " + orig_phrase +"
        yet":
            meaning = "There aren't any definitions for "+orig_phrase+" yet on
            Urban Dictionary."
        else:
            meaning = re.sub('&apos;', '\'', meaning)
            meaning = meaning[:min(len(meaning),300)]
            meaning += "....\n"
            meaning += "See the meaning at Urban Dictionary :-
            http://www.urbandictionary.com/define.php?term=" +  phrase
            output['input'] = input
            output['output'] = TextTemplate('Meaning of ' +
                                            orig_phrase +
                                            'from Urban Dictionary:\n' + meaning).get_message()
            output['success'] = True

    except:
        error_message = 'I couldn\'t find the meaning of that phrase.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\nurban lol'
        error_message += '\nlol urban'
        error_message += '\nslang lol'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
                                     
