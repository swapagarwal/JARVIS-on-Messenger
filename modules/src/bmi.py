
import config
import modules
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        
        text_i_want_returned = do_thing(input) ### TODO: define do_thing()
        
        message = TextTemplate(text_i_want_returned).get_message()
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output


def bmi(string):
    x = string.split() #string is divided into two variables
    height = float(x[0])
    weight = float(x[1])
    height_sq = height*height
    bmi = weight / height_sq * 703 #formula for bmi
    bmi_final = int(round(bmi,0)) #round bmi
    if bmi_final == 18.5: #prints to which category you belong including your bmi index
        return ('Your BMI is {} and you belong to category underweight'.format(bmi_final))
    elif bmi_final == 25:
        return ('Your BMI is {} and you belong to category underweight'.format(bmi_final))
    elif bmi_final == 30:
        return ('Your BMI is {} and you belong to category underweight'.format(bmi_final))
    else:
        return ('Your BMI is {} and you belong to category underweight'.format(bmi_final))
