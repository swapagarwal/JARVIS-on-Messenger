"""Music conversion module."""
# pylint: disable=import-error
# pylint: disable=redefined-builtin
# pylint: disable=bare-except
import unicodedata
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from googleapiclient.discovery import build


def get_results_spotify(query):
    """Get results for spotify api query."""
    s_p = spotipy.Spotify(auth_manager=SpotifyOAuth(scope="user-library-read",
        # INSERT APP INFO HERE
        client_id='',
        client_secret='',
        redirect_uri=''))
    q_temp = query.split()
    query = ""
    for word in q_temp:
        query += ''.join(x for x in word if x.isalnum()) + ' '
    items = []
    while (len(items) == 0 or len(query) == 0):
        res = s_p.search(query, type="track")
        items = res.get("tracks").get('items')
        query = query.split()
        query.pop(-1)
        query = ' '.join(query)
    songs = [unicodedata.normalize('NFKD', x.get('name')).encode(
        'ascii', 'ignore') for x in items]
    artists_for_all = [x.get("artists") for x in items]
    artists = []
    for collection in artists_for_all:
        attributors = []
        for artist in collection:
            attributors.append(unicodedata.normalize(
                'NFKD', artist.get('name')).encode('ascii', 'ignore'))
        artists.append(attributors)
    output_list = []
    for _, index in enumerate(songs):
        output_list.append("{} by {}".format(
            songs[index], ", ".join(artists[index])))
    return output_list


# ADD API_KEY for YOUTUBE HERE
API_KEY = ''


scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def get_results_youtube(link):
    """Get results for youtube api query."""
    api_service_name = "youtube"
    api_version = "v3"
    youtube = build(api_service_name, api_version, developerKey=API_KEY)

    # Get video id
    idv = link.split("v=")[1]

    request = youtube.videos().list(
        part="snippet",
        id=idv
    )
    try:
        res = request.execute()
    except:
        print("Connection error")
        return ""

    return res.get("items")[0].get("snippet").get("title")


def process(input, entities=None):
    """Required process for Jarvis"""
    output = {
        'input': input,
        'output': get_results_spotify(get_results_youtube(entities["value"])),
        'success': True
    }
    return output
