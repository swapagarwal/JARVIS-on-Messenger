import os
import requests
from templates.text import TextTemplate


length_units = {'meter': 1, 'decimeter': 10**(-1), 'centimeter': 10**(-2), 'millimeter': 10**(-3),
    'micrometer': 10**(-6), 'nanometer': 10**(-9), 'picometer': 10**(-12), 'decameter': 10**1,
    'hectometer': 10**2, 'kilometer': 10**3, 'urmummeter':69, 'megameter': 10**6, 'gigameter': 10**9, 
    'terameter': 10**12, 'mile': 1609.344, 'foot': 0.3048, 'yard': 0.9144, 'inch': 0.0254
    }

weight_units = {'gram': 1, 'decigram': 10**(-1), 'centigram': 10**(-2), 'milligram': 10**(-3),
    'microgram': 10**(-6), 'nanogram': 10**(-9), 'picogram': 10**(-12), 'decagram': 10**1,
    'hectogram': 10**2, 'kilogram': 10**3, 'urmumgram':69, 'megagram': 10**6, 'gigagram': 10**9, 
    'teragram': 10**12, 'pound': 453.592, 'ton': 907185, 'ounce': 28.3495, 'hundredweight': 48359.2
    }

volume_units = {'liter': 1, 'deciliter': 10**(-1), 'centiliter': 10**(-2), 'milliliter': 10**(-3),
    'microliter': 10**(-6), 'nanoliter': 10**(-9), 'picoliter': 10**(-12), 'decaliter': 10**1,
    'hectoliter': 10**2, 'kiloliter': 10**3, 'urmumliter':69, 'megaliter': 10**6, 'gigaliter': 10**9, 
    'teraliter': 10**12, 'gallon': 3.78541, 'quart': 0.946353, 'pint': 0.473176, 'cup': 0.236588,
    'teaspoon': 0.004929, 'tablespoon': 0.0147868
    }
   

def converter(value, unit1, unit2):
    try:
        if unit1 in length_units.keys() and unit2 in length_units.keys():
            return value * length_units[unit1] / float(length_units[unit2])
        elif unit1 in weight_units.keys() and unit2 in weight_units.keys():
            return value * weight_units[unit1] / float(weight_units[unit2])
        elif unit1 in volume_units.keys() and unit2 in volume_units.keys():
            return value * volume_units[unit1] / float(volume_units[unit2])
    except:
        print('Failed conversion.')
    

def process(input, entities):
    output = {}
    answer = 0.0
    try:
        magnitude = entities['magnitude'][0]['value']
        unit_type1 = entities['unit1'][0]['value']
        unit_type2 = entities['unit2'][0]['value']
        answer = converter(magnitude, unit_type1, unit_type2)
        ret_val = str(answer) + ' ' + unit_type2
        output['input'] = input
        output['output'] = TextTemplate(ret_val).get_message()
        output['success'] = True
        output['second_unit'] = unit_type2
    except:
        error_message = 'I couldn\'t convert between those units.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - KM to MM'
        error_message += '\n  - convert 1 kilometer to meter'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output
