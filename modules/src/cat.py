import requests

import modules
from templates.attachment import AttachmentTemplate
from templates.quick_replies import add_quick_reply
from templates.text import TextTemplate

def process(input, entities=None):
    output = {}
    try:
        response = requests.get('http://thecatapi.com/api/images/get', params = {'format': 'xml'})
        cat_image = ''

        # Response example:
        # <?xml version="1.0"?>
        # <response>
        #   <data>
        #     <images>
        #       <image>
        #         <url>http://25.media.tumblr.com/tumblr_m0ew05LBKU1qz5v7io1_1280.jpg</url>   <- this URL should be returned
        #         <id>atf</id>
        #         <source_url>http://thecatapi.com/?id=atf</source_url>
        #       </image>
        #     </i
        # mages>
        #   </data>
        # </response>

        for r in response:
            x = r.find('<url>')
            if x != -1:
                cat_image = r[x+5:r.find('</url')].strip(' ')


        message = AttachmentTemplate(cat_image, type='image').get_message()
        message = add_quick_reply(message, 'More Cats', modules.generate_postback('cat'))
        output = {
            'input': input,
            'output': message,
            'success': True
        }
    except:
        error_message = 'There was some error while retrieving your cat picture.'
        output = {
            'error_msg': TextTemplate(error_message).get_message(),
            'success': False
        }
    return output