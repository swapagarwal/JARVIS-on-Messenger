from templates.button import ButtonTemplate


def process(input, entities=None):
    request = 'Kindly use the following buttons to:'
    request += '\n  - Request a new feature, by including some sample queries and their expected results.'
    request += '\n  - Report a bug (I couldn\'t handle the query and/or gave unexpected results), by including your search query and the expected result.'
    template = ButtonTemplate(request)
    template.add_web_url('File an Issue', 'https://github.com/swapagarwal/JARVIS-on-Messenger/issues/new')
    template.add_web_url('Chat with my Master', 'https://gitter.im/swapagarwal/JARVIS-on-Messenger')
    output = {
        'input': input,
        'output': template.get_message(),
        'success': True
    }
    return output
