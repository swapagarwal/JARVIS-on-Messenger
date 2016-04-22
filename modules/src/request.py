def process(input, entities=None):
    request = '''
    Kindly head over to https://github.com/swapagarwal/JARVIS-on-Messenger/issues/new to file an issue:\n
    - If you find a bug (the bot couldn't handle the query and / or gave irrelevant results), include your search query and the expected result.\n
    - If you'd like to request a new functionality, feel free to do so by including some sample queries and their corresponding results.\n
    '''
    output = {
        'input': input,
        'output': request,
        'success': True
    }
    return output
