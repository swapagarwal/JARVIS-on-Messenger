def process(input, entities=None):
    request = '''
Kindly head over to https://github.com/swapagarwal/JARVIS-on-Messenger/issues/new to:\n
  - Report a bug (I couldn't handle the query and/or gave unexpected results), by including your search query and the expected result.\n
  - Request a new feature, by including some sample queries and their expected results.\n
    '''
    output = {
        'input': input,
        'output': request,
        'success': True
    }
    return output
