import os 
import requests
import unirest
import json

MANGA_API_KEY = 'RkcSLeT9wDmshDvhRF2OGDnWp0OFp1ZZXt5jsnwx4nQiNrQrSd'


query = 'one piece'
response = unirest.get("https://doodle-manga-scraper.p.mashape.com/mangareader.net/search?l=1&q=" + query,
  headers={
    "X-Mashape-Key": "RkcSLeT9wDmshDvhRF2OGDnWp0OFp1ZZXt5jsnwx4nQiNrQrSd",
    "Accept": "application/json",
  }).body

mangaid = response[0]['mangaId']

response = unirest.get("https://doodle-manga-scraper.p.mashape.com/mangareader.net/manga/" + mangaid,
  headers={
    "X-Mashape-Key": "RkcSLeT9wDmshDvhRF2OGDnWp0OFp1ZZXt5jsnwx4nQiNrQrSd",
    "Accept": "text/plain"
  }
).body

output = "Name: " + response['name']
output += "\nAuthor(s): "
if len(response['author']) > 1:
	for x in range(0, len(response['author'])):
		if x == (len(response['author']) - 1):
			output += response['author'][x]
		else:
			output += response['author'][x] + ", "
else:
	output += response['author'][0]
output += "\nArtist(s): "
if len(response['artist']) > 1:
	for x in range(0, len(response['artist'])):
		if x == (len(response['artist']) - 1):
			output += response['artist'][x]
		else:
			output += response['artist'][x] + ", "
else:
	output += response['artist'][0]
output += "\nStatus: " + response['status']
output += "\nYear of Release: " + str(response['yearOfRelease'])
output += "\nGenre(s): "
if len(response['genres']) > 1:
	for x in range(0, len(response['genres'])):
		if x == (len(response['genres']) - 1):
			output += response['genres'][x]
		else:
			output += response['genres'][x] + ", "
else:
	output += response['genres'][0]

print(output)
