from templates.text import TextTemplate


def process(input, entities=None):
    helper = 'Hi there! I\'m Jarvis, your personal assistant.\n'
    if entities:
        if 'sender' in entities and 'first_name' in entities['sender']:
            helper = helper.replace('there', entities['sender']['first_name'])
    helper += """
    You can tell me things like:
      - define comfort
      - iron man 2 movie plot
      - tell me a joke/quote/fact
      - wiki html
      - anything you want book
      - usd to eur rate
      - death note anime
      - time in seattle
      - songs by linkin park
      - shorten google.com
      - weather in london
      - videos of sia
      - flip a coin
      - roll a die
      - show a random xkcd comic
      - latest news
      - paradise lyrics
      
    I'm always learning, so do come back and say hi from time to time!
    Have a nice day. :)"""

    output = {
        'input': input,
        'output': TextTemplate(helper).get_message(),
        'success': True
    }
    return output
