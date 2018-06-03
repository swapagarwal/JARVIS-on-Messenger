import random

from templates.text import TextTemplate

def process(input, entities=None):
  menu = [
      'pizza',
      'chicken',
      'pasta',
      'steak',
      'sushi',
      'french fries',
      'hamburger',
      'hot dog',
      'salad',
      'bibimbap',
      'bulgogi',
      'popcorn',
      'saint louis pizza',
      'lobster',
      'curry',
      'serial',
      'fired rice',
      'toast',
      'brito',
      'intestine',
      'pork belly',
      'ramen',
      'bread',
      'cookie',
      'chili shrimp',
      'spicy sausage stew',
      'rice noodles',
 ]
 c_menu = random.choice(menus)
 
 message = ' ' 
 
 output = {
    'input' : input,
    'ouput' : TextTemplate(message).get_message(),
    'success' : True
    }
   
   return output  
     
