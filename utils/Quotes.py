import requests
import config
import json, ast
import random

def getQuote():
    resources = collect_quote_resources()
    if resources:
        resource = random.sample(resources, 1).pop()
        return callApi(resource)

def collect_quote_resources():
    quotes_resources = set()
    with open(config.QUOTES_RESOURCE_FILE, 'r') as quotes_resources_file:
        data = quotes_resources_file.read()
        json_data = json.loads(data)
        for q in json_data:
            params =  str(q['params']).replace("u'",'')
            quote = Quotes_Resource(q['url'], q['method'], params, q['name'], q['key'])
            quotes_resources.add(quote)
    return quotes_resources


def callApi(resource):
    try:
        response = requests.request(resource.method, resource.url, params=resource.params)
        data = json.loads(response.text.replace('[', '').replace(']', ''))
        return data[resource.getKey()]
    except ValueError:
        return getQuote()
    except requests.exceptions.ConnectionError:
        return getQuote()

class Quotes_Resource(object):
    def __init__(self, url, method, params, name, key):
        self.url = url
        self.method = method
        self.params = params
        self.name = name
        self.key = key

    def getKey(self):
        return self.key