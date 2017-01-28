from copy import deepcopy as copy

QUICK_REPLIES_LIMIT = 11
TITLE_CHARACTER_LIMIT = 20
PAYLOAD_CHARACTER_LIMIT = 1000


def add_quick_reply(message, title='', payload=''):
    message_with_quick_reply = copy(message)
    if 'quick_replies' not in message_with_quick_reply:
        message_with_quick_reply['quick_replies'] = []
    if len(message_with_quick_reply['quick_replies']) < QUICK_REPLIES_LIMIT:
        # TODO: location + image_url
        quick_reply = {
            'content_type': 'text',
            'title': title[:TITLE_CHARACTER_LIMIT],
            'payload': payload[:PAYLOAD_CHARACTER_LIMIT]
        }
        message_with_quick_reply['quick_replies'].append(quick_reply)
    return message_with_quick_reply
