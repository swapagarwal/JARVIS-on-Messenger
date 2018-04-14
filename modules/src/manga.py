import os 
import requests
import config
import unirest

MANGA_API_KEY = os.environ.get('MANGA_API_KEY', config.MANGA_API_KEY)


def process(input, entities):
    output = {}
    try: 
        query = entities['manga'][0]['value']
        response = unirest.get("https://doodle-manga-scraper.p.mashape.com/mangareader.net/search?l=1&q=" + query,
          headers={
            "X-Mashape-Key": MANGA_API_KEY,
            "Accept": "text/plain",
          }).body

        mangaid = response[0]['mangaId']

        response = unirest.get("https://doodle-manga-scraper.p.mashape.com/mangareader.net/manga/" + mangaid,
          headers={
            "X-Mashape-Key": MANGA_API_KEY,
            "Accept": "text/plain"
          }).body

        output['input'] = input
        output['output'] = "Name: " + response['name']
        output['output'] += "\nAuthor(s): "
        output['output'] += listOutput(response['author'])
        output['output'] += "\nArtist(s): "
        output['output'] += listOutput(response['artist'])
        output['output'] += "\nStatus: " + response['status']
        output['output'] += "\nYear of Release: " + str(response['yearOfRelease'])
        output['output'] += "\nGenre(s): "
        output['output'] += listOutput(response['genres'])
        output['success'] = True
    except:
        error_message = 'I couldn\'t find any mangas matching your query.'
        error_message += '\nPlease ask me something else, like:'
        error_message += '\n  - Naruto manga'
        error_message += '\n  - One Piece manga status'
        error_message += '\n  - Information on Bleach manga'
        output['success'] = False
    return output


def listOutput(l):
    myString = ""
    if len(l) > 1:
        for x in range(0, len(l)):
            if x == (len(l) - 1):
                myString += l[x]
            else:
                myString += l[x] + ", "
    else:
        myString += l[0]
    return myString