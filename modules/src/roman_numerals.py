from templates.text import TextTemplate

def process(input, entities):

    modern_numeral = entities['to_roman_numeral'][0]['value']
    
    try:
        
        modern_numeral = int(float(modern_numeral))
	
        tempa = modern_numeral
        count = 1

        while tempa > 5000:
            tempa = tempa//1000+1
            count += 1


        # TODO remove runding and use decimal dot system too

        # TODO make it go both ways

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

        roma_list = [("M","thausends"),("D","fivehundreds"),("C","hundreds"),("L","fifties"),("X","tens"),("V","fives"),("I","ones")]

        for i in range(count)[::-1]:

            for w, q in enumerate(roma_list):

                if dicta[q[1]+str(i)] != 4:
                    out_line += ("("*i+q[0]+")"*i)*dicta[q[1]+str(i)]*bool(dicta[q[1]+str(i)])
                elif w != 0:
                    out_line += ("("*i+q[0]+")"*i)+("("*i+roma_list[w-1][0]+")"*i)
                else:
                    out_line += ("("*i+q[0]+")"*i)+("("*(i+1)+roma_list[w-2][0]+")"*(i+1))

    
        output['input'] = input
        output['output'] = TextTemplate(out_line).get_message()
        output['success'] = True
        
    except:
    
        output['error_msg'] = TextTemplate("Please give me a number consistent of arabic numbers.").get_message()
        output['success'] = False
        
    return output
