from __future__ import division
import requests
from templates import text
from templates.generic import *
from templates.button import *
import json



def api_query(username):
    r = requests.get('https://api.github.com/search/issues?q=-label:invalid+created:2017-09-30T00:00:00-12:00..2017-10-31T23:59:59-12:00+type:pr+is:public+author:' + username + '&per_page=300')
    data = r.json()
    return data


def process(input,entities):
    output = {}
    try:
        username = entities['hacktoberfest'][0]['value']
        data = api_query(username)
        template = GenericTemplate()
        if(data[u'total_count']==0):
            template.add_element(title='No contributions :(',item_url='https://hacktoberfest.digitalocean.com/',subtitle='You don\'t have any contributions yet.')
        elif(data[u'total_count']>=4):
            template.add_element(title='You have done it! :)',subtitle='You have completed the hacktoberfest challenge , some of your contributions are:')
            for i in range(0,4):
                contri = data[u'items'][i]
                status = contri[u'state'].encode("utf-8")
                url = contri[u'html_url'].encode("utf-8")
                sub = contri[u'title'].encode("utf-8")
                url_to_avatar = contri[u'user'][u'avatar_url'].encode("utf-8")
                title = "#" + str(i+1)
                buttons = ButtonTemplate()
                buttons.add_web_url(title=('Read moree about the '+status+' issue'),url=url)
                buttons.add_web_url(title='Powered by Github',url='https://github.com')
                try:
                    # I don't know about this error
                    # TODO:
                    # fix this error
                    template.add_element(title=title,item_url=url,image_url=url_to_avatar,subtitle=sub,
                            buttons=buttons)
                except:
                    print "Error in addition of elements"
        else:
            percent = str((data[u'total_count']/4)*100)+'%'
            template.add_element(title='A little more to go! :)',subtitle=u'You have completed it ' +percent )
            i=1
            for contri in data[u'items']:
                status = contri[u'state'].encode("utf-8")
                url = contri[u'html_url'].encode("utf-8")
                sub = contri[u'title'].encode("utf-8")
                url_to_avatar = contri[u'user'][u'avatar_url'].encode("utf-8")
                title = "#" + str(i)
                buttons = ButtonTemplate()
                buttons.add_web_url(title=(u'Read moree about the '+status+u' issue').encode("utf-8"),url=url)
                buttons.add_web_url(title='Powered by Github',url='https://github.com')
                try:
                    # I don't know about this error
                    # TODO:
                    # fix this error
                    template.add_element(title=title,item_url=url,image_url=url_to_avatar,subtitle=sub,
                        buttons=buttons)
                except:
                    print "Error in addition of contributions"
                i+=1
        output['input'] = input
        output['output'] = template.get_message()
        output['success'] = True
    except:
        error_message = 'Does this user exist?'
        output['error_msg'] = TextTemplate(error_message).get_message()
        output['success'] = False
    return output