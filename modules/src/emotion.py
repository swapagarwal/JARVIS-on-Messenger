import random
from templates.text import TextTemplate

def process(input, entities=None):
  greetings = [
      'Gravity. It keeps you rooted to the ground. In space, there's not any gravity. You just kind of leave your feet and go floating around. Is that what being in love is like?',
      'Could you imagine how horrible things would be if we always told others how we felt? Life would be intolerably bearable.',
      'Love is the big booming beat which covers up the noise of hate.',
      'The first duty of love is to listen.',
      'Age does not protect you from love. But love, to some extent, protects you from age.',
      'There's always one who loves and one who lets himself be loved.',
      'I was born with an enormous need for affection, and a terrible need to give it.',
      'If someone wants a sheep, then that means that he exists.',
      'Immature love says, I love you because I need you, mature love says, I need you because I love you.'
      ]
      
      output = {
        'input':input,
        'output':TextTemplate(random.choice(greetings)).get_message(),
        'success':True
        }
return output      
