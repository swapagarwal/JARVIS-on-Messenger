import random

import modules
from templates.attachment import AttachmentTemplate
from templates.text import TextTemplate
from templates.quick_replies import add_quick_reply

dice_sides = {
    1: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-one/256/0/e74c3c_none.png',
    2: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-two/256/0/e74c3c_none.png',
    3: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-three/256/0/e74c3c_none.png',
    4: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-four/256/0/e74c3c_none.png',
    5: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-five/256/0/e74c3c_none.png',
    6: 'http://fa2png.io/media/icons/foundation-icon-fonts/2015-02-16/die-six/256/0/e74c3c_none.png'
}


def process(input, entities):
    try:
        message = None
        dice = entities['dice'][0]['value']
        if (dice == "d6"):
            message = AttachmentTemplate(dice_sides[random.randint(1, 6)], type='image').get_message()
        else:
            sides = int(dice[1:])
            message = TextTemplate("I rolled a " + dice + " and got " + str(random.randint(1, sides))).get_message()
        message = add_quick_reply(message, 'Roll again!', modules.generate_postback('dice'))
        message = add_quick_reply(message, 'Flip a coin.', modules.generate_postback('coin'))
        output = {
            'input': input,
            'output': message,
            'success': True
        }
    except:
        error =  "I'm sorry, something went wrong when rolling the dice."
        error += "\nI might not be certain what kind of dice you're trying to roll."
        error += "\nI can roll a d4, d6, d10, d12, d20, or d100 (d%)."
        error += "\nPlease phrase your request more like this:"
        error += "\n  - Roll a d6"
        error += "\n  - Jarvis, roll a die"
        error += "\n  - Can you roll a d20?"
        output = {
            'error_msg': error,
            'success': False
        }
    return output
