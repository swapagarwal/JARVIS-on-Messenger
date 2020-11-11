from templates.attachment import AttachmentTemplate
import requests

def process(input, entities=None):
    r = requests.get('https://deckofcardsapi.com/api/deck/new/draw/?count=1')
    card = r.json()
    message = AttachmentTemplate(card['cards'][0]['image'], type='image').get_message()
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output


