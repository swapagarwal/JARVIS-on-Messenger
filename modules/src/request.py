from templates.text import TextTemplate

def process(input, entities=None):
    request = '''Kindly head over to https://github.com/swapagarwal/JARVIS-on-Messenger/issues/new to:\n
  - Report a bug (I couldn't handle the query and/or gave unexpected results), by including your search query and the expected result.\n
  - Request a new feature, by including some sample queries and their expected results.'''
    output = {
        'input': input,
        'output': TextTemplate(request).get_message(),
        'success': True
    }
    return output
