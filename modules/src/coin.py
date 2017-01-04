import json
import random
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply

# Images by US Mint; published on wikimedia under public domain rights
coin_images = {
	'heads': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/2006_Quarter_Proof.png/244px-2006_Quarter_Proof.png',
	'tails': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/70/Oregon_quarter%2C_reverse_side%2C_2005.jpg/236px-Oregon_quarter%2C_reverse_side%2C_2005.jpg'
}

def process(input, entities=None):
    toss = AttachmentTemplate(coin_images[random.choice(['heads', 'tails'])], type='image').get_message()
    postback = {
        'intent': 'coin',
        'entities': None
    }
    message = add_quick_reply(toss, 'Flip again!', json.dumps(postback))
    output = {
        'input': input,
        'output': message,
        'success': True
    }
    return output
