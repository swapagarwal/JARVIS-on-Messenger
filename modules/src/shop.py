import config
from templates.generic import *
from templates.text import TextTemplate

from amazonproduct.api import API

def process(input, entities):
    output = {}

    api = API(cfg=config.AMAZON_KEYS)

    try:
        item = entities['item'][0]['value']
        result = api.item_search('Blended', ResponseGroup='ItemAttributes', Keywords=item, paginate=False)
        product = result.Items.Item[0]
        image_result = api.item_search('Blended',ResponseGroup='Images', Keywords=item, paginate=False)
        product_image = image_result.Items.Item[0]

        template = GenericTemplate()
        template.set_image_aspect_ratio_to_square()
        
        title = product.ItemAttributes.Title
        item_url = "https://www.amazon.com/gp/product/{0}".format(product.ASIN)
        image_url = product_image.LargeImage.URL
        price = product.ItemAttributes.ListPrice.FormattedPrice
        
        subtitle = price
        buttons = ButtonTemplate()
        buttons.add_web_url('Open on Amazon.com', item_url)
        template.add_element(title=title, item_url=item_url, image_url=image_url, subtitle=subtitle,
                                buttons=buttons.get_buttons())
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'I couldn\'t find that item.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - buy remote control'
        error_message += '\n  - I need toilet paper'
        error_message += '\n  - purchase television'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output