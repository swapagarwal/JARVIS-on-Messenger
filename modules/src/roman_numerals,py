import requests

from templates.text import TextTemplate

def process(input, entities):

    modern_numeral = entities['to_roman_numeral'][0]['value']
    
    try:
    
        modern_numeral = int(float(modern_numeral)) 
        
        # TODO remove runding and use decimal dot system too
        
        # TODO make it go both ways
        
        # TODO uses old number system f.x. VIIII update to the newer IX
        
        # TODO make use of () to * by a thausend f.x. (V) = 5000 and ((V)) = 5000000 to efficintlt write infinitly big numbers
        
        thausends, modern_numeral = modern_numeral//1000, modern_numeral%1000
        fivehundreds, modern_numeral = modern_numeral//500, modern_numeral%500
        hundreds, modern_numeral = modern_numeral//100, modern_numeral%100
        fifties, modern_numeral = modern_numeral//50, modern_numeral%50
        tens, modern_numeral = modern_numeral//10, modern_numeral%10
        fives, modern_numeral = modern_numeral//5, modern_numeral%5
        ones = modern_numeral
    
         out_line = "M"*thausends+"D"*fivehundreds+"C"*hundreds+"L"*fifties+"X"*tens+"V"*fives+"I"*ones
    
        output['input'] = input
        output['output'] = TextTemplate(out_line).get_message()
        output['success'] = True
        
    except:
    
        output['error_msg'] = TextTemplate("Please give me a number consistent of arabic numbers.").get_message()
        output['success'] = False
        
    return output
