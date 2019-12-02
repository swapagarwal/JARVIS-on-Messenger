import config
import modules
from templates.text import TextTemplate

def bmi(string):
	x = string.split()
	mode = x[2]
    height = float(x[0])
    weight = float(x[1])
	if mode == "imperial":
		height_sq  = height*height
		bmi = weight / height_sq * 703
		bmi_final = int(round(bmi,0))
		if bmi_final <= 18.5:
			return ("Your BMI is {} and you belong to category underweight.".format(bmi_final))
		elif bmi_final < 25:
			return ("Your BMI is {} and you belong to category normal.".format(bmi_final))
		elif bmi_final < 30:
			return ("Your BMI is {} and you belong to category overweight.".format(bmi_final))
		else: 
			return ("Your BMI is {} and you belong to category obese.".format(bmi_final))
	else:
		heigh_new = heigh/100
		height_sq  = height*height
		bmi = weight / height_sq
		bmi_final = int(round(bmi,0))
		if bmi_final <= 18.5:
			return ("Your BMI is {} and you belong to category underweight.".format(bmi_final))
		elif bmi_final < 25:
			return ("Your BMI is {} and you belong to category normal.".format(bmi_final))
		elif bmi_final < 30:
			return ("Your BMI is {} and you belong to category overweight.".format(bmi_final))
		else: 
			return ("Your BMI is {} and you belong to category obese.".format(bmi_final))
			
	


def process(input, entities=None):
    output = {}
    try:
        
        text_i_want_returned = bmi(input) 
        
        message = TextTemplate(text_i_want_returned).get_message()
        output['input'] = input
        output['output'] = message
        output['success'] = True
    except:
        output['success'] = False
    return output



