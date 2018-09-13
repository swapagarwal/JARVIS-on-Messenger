from templates.text import TextTemplate

def process(input, entities):

    modern_numeral = entities['to_roman_numeral'][0]['value']
    
    try:
    
        modern_numeral = int(float(modern_numeral))
        
        tempa = modern_numeral
        count = 1
        
        while tempa > 5000:
            tempa = temp//1000+1
            count += 1
            
        
        # TODO remove runding and use decimal dot system too
        
        # TODO make it go both ways
        
        # TODO uses old number system f.x. VIIII update to the newer IX
        
        dicta = {}
        
        for i in range(count)[::-1]:
            
            dicta["thausends"+str(i)], modern_numeral = modern_numeral//(1000*1000**i), modern_numeral%(1000*1000**i)
            dicta["fivehundreds"+str(i)], modern_numeral = modern_numeral//(500*1000**i), modern_numeral%(500*1000**i)
            dicta["hundreds"+str(i)], modern_numeral = modern_numeral//(100*1000**i), modern_numeral%(100*1000**i)
            dicta["fifties"+str(i)], modern_numeral = modern_numeral//(50*1000**i), modern_numeral%(50*1000**i)
            dicta["tens"+str(i)], modern_numeral = modern_numeral//(10*1000**i), modern_numeral%(10*1000**i)
            dicta["fives"+str(i)], modern_numeral = modern_numeral//(5*1000**i), modern_numeral%(5*1000**i)
            dicta["ones"+str(i)], modern_numeral = modern_numeral//(1*1000**i), modern_numeral%(1*1000**i)
        
        out_line = "In roman numerals that would be "
        
        for i in range(count)[::-1]:
            
            out_line += ("("*i+"M"+")"*i)*dicta["thausends"+str(i)]*bool(dicta["thausends"+str(i)])
            out_line += ("("*i+"D"+")"*i)*dicta["fivehundreds"+str(i)]*bool(dicta["fivehundreds"+str(i)])
            out_line += ("("*i+"C"+")"*i)*dicta["hundreds"+str(i)]*bool(dicta["hundreds"+str(i)])
            out_line += ("("*i+"L"+")"*i)*dicta["fifties"+str(i)]*bool(dicta["fifties"+str(i)])
            out_line += ("("*i+"X"+")"*i)*dicta["tens"+str(i)]*bool(dicta["tens"+str(i)])
            out_line += ("("*i+"V"+")"*i)*dicta["fives"+str(i)]*bool(dicta["fives"+str(i)])
            out_line += ("("*i+"I"+")"*i)*dicta["ones"+str(i)]*bool(dicta["ones"+str(i)])
    
        output['input'] = input
        output['output'] = TextTemplate(out_line).get_message()
        output['success'] = True
        
    except:
    
        output['error_msg'] = TextTemplate("Please give me a number consistent of arabic numbers.").get_message()
        output['success'] = False
        
    return output
