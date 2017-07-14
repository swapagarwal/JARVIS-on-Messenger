#Jarvis Conversions
#import json
#from templates.text import TextTemplate
#from templates.quick_replies import add_quick_reply

import re

''' This module can be used for length,Area,volume,time, temperature,weight conversions 
    Try:     1 m in km, 1 yd in ft,A:\
            or 1 meter in kilometer
            1 sq cm in m,
            100 cubic meter in cubic millimeter,
            10 L in gallon,
            1 kg in lb, 
            98.4 F in celcius
'''

meter={'meter':1,'kilometer': 0.001,'centimeter': 100,'millimeter':1000,
        'micrometer':1000000,'nanometer':10**9,'mile':0.0006213689,
        'yard':1.0936132983,'foot':3.280839895,'inch':39.37007874,
        'light year':1.057008707*10**(-16)}

celcius= {'celcius':1,'kelvin':274.15,'farenheit':33.8}

squareMeter={'square meter':1,'square kilometer': 0.001**2,'square centimeter': 100**2,
        'square millimeter':1000**2,
        'square mile':0.0006213689**2,'square yard':1.0936132983**2,
        'square foot':3.280839895**2,'square inch':39.37007874**2}

cubicMeter={'cubic meter':1,'cubic kilometer': 0.001**3,'cubic centimeter': 100**3,
        'cubic millimeter':1000**3}

liter={'liter':1,'milliliter':1000,'gallon':0.2641721769,
        'quart':1.0566887074,'pint':2.1133774149,'cup':4.2267548297}
        
gram={'kilogram':0.001,'gram':1,'milligram':1000,'metric ton':0.000001,
        'long ton':9.842073304*10**(-7),'short ton':0.0000011023,'pound':0.0022046244,
        'ounce':0.0352739907,'carrat':5,'atomic mass unit':6.022136652*10**(23)}
        
minute={'second':60,'millisecond':60000,'microsecond':60**7,'nanosecond':60**10,
        'picosecond':60**13,'minute':1,'hour':60*0.0002777778,'day':60*0.0000115741,
        'week':60*0.0000016534,'month':60*3.802570537*10**(-7)}
        
abbreviation={'m':'meter', 'km':'kilometer', 'cm':'centimeter','mm':'millimeter',
                'nm':'nanometer','ft':'foot','c':'celcius','f':'farenheit','k':'kelvin',
                'sq m':'square meter','sq km':'square kilometer','sq ft':'square foot',
                'yd':'yard','sq yard':'square yard','l':'liter','ml':'milliliter','g':'gram',
                'kg':'kilogram','mg':'milligram','ton':'metric ton','lb':'pound',
                'amu':'atomic mass unit','s':'second','min':'minute','hr':'hour','ms':'millisecond',
                'ns':'nanosecond','ps':'picosecond','d':'day'}

                
def process(message=raw_input("Enter Message: "),entities=None):
    pattern=r'\sto\s|\sin\s'
    re.compile(pattern)
    values=re.split(pattern,message)
    print "values = ",values
    unit2=values[-1].lower().strip()
    print "unit2 = ",unit2
    try:
        number,unit1=values[0].strip().split(' ')
    except ValueError:
        number,unit1,unit3=values[0].strip().split(' ')
        unit1=unit1+" "+unit3
    try:
        unit1=abbreviation[unit1]
    except KeyError:
        pass
    try:
        unit2=abbreviation[unit2]
    except KeyError:    
        pass        
    if unit2 in meter.keys():
        return linearConversion(float(number),unit1.lower(),unit2)
    
    if unit2 in squareMeter.keys():
        return areaConversion(float(number),unit1.lower(),unit2)
        
    if unit2 in cubicMeter.keys():
        return volumeLengthConversion(float(number),unit1.lower(),unit2)
    
    if unit2 in liter.keys():
        return volumeConversion(float(number),unit1.lower(),unit2)
    
    if unit2 in gram.keys():
        return weightConversion(float(number),unit1.lower(),unit2)
    
    if unit2 in minute.keys():
        return timeConversion(float(number),unit1.lower(),unit2)
                                                             
    if unit2 in celcius.keys():
        return temperatureConversion(float(number),unit1.lower(),unit2)    

def linearConversion(number,unit1,unit2):
    #Length Conversions
    par2=meter[str(unit2)]
    par1=meter[unit1]
    print "parameter2 = ",par2
    ans=number*par2/float(par1)    
    if unit2=='foot':
        return str(str(number)+" "+unit1+" = "+str(ans)+" "+unit2)
    else:    
        return str(str(number)+" "+unit1+" = "+str(ans)+" "+unit2+"s")    
    
def areaConversion(number,unit1,unit2):
    #Area Conversions
    par2=squareMeter[str(unit2)]
    par1=squareMeter[unit1]
    print "parameter2 = ",par2
    ans=number*par2/float(par1)    
    return str(str(number)+" "+unit1+" = "+str(ans)+" "+unit2+"s")    

    
def volumeLengthConversion(number,unit1,unit2):
    #Volume Length Conversions
    par2=cubicMeter[str(unit2)]
    par1=cubicMeter[unit1]
    print "parameter2 = ",par2
    ans=number*par2/float(par1)    
    return str(str(number)+" "+unit1+" = "+str(ans)+" "+unit2+"s") 
    
def volumeConversion(number,unit1,unit2):
    #Volume Conversion
    par2=liter[str(unit2)]
    par1=liter[unit1]
    print "parameter2 = ",par2
    ans=number*par2/float(par1)    
    return str(str(number)+" "+unit1+" = "+str(ans)+" "+unit2+"s") 
     
def weightConversion(number,unit1,unit2):
    #Weight conversion
    par2=gram[str(unit2)]
    par1=gram[unit1]
    print "parameter2 = ",par2
    ans=number*par2/float(par1)    
    return str(str(number)+" "+unit1+" = "+str(ans)+" "+unit2+"s")    

def timeConversion(number,unit1,unit2):
    #time conversion
    par2=minute[str(unit2)]
    par1=minute[unit1]
    print "parameter2 = ",par2
    ans=round(number*par2/float(par1),0)    
    return str(str(number)+" "+unit1+" = "+str(ans)+" "+unit2+"s")    
    
def temperatureConversion(number,unit1,unit2):
    '''This only works conversion between Celcius,Farenheit,Kelvin
    E.g. 1 celcius in kelvin '''
    ans=0
    if unit1=='celcius': 
        if unit2=='farenheit':
            ans=number*1.8+32
            print "ans = ",ans
        if unit2=='kelvin':
            ans=number+273.15 
        elif unit1==unit2: ans=1
    if unit1=='farenheit':
        if unit2=='celcius':
            ans=(number-32)/1.8
            print "ans = ",ans
        if unit2=='kelvin':
            ans= (number+459.67)*5/9
            print "ans = ",ans
        elif unit1==unit2: ans=1                          
    if unit1=='kelvin':
        if unit2=='celcius':
            ans=number-273.15
        if unit2=='farenheit':
            ans=1.8*number-459.67
            print "ans = ",ans
        elif unit1==unit2: ans=1    
    return str(str(number)+" "+unit1+" = "+str(ans)+" "+unit2)        
                     
