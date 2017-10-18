# Facebook (+ Wit)
ACCESS_TOKEN = '<<ACCESS_TOKEN>>'
VERIFY_TOKEN = '<<VERIFY_TOKEN>>'
WIT_AI_ACCESS_TOKEN = 'IKJJJYYVR3X672DHFVS7U7C4L2MQSS2P'

# Offline data sources
FACTS_SOURCE_FILE = 'data/facts.json'
JOKES_SOURCE_FILE = 'data/jokes.json'
QUOTES_SOURCE_FILE = 'data/quotes.json'

# Access token files
SPOTIFY_TOKEN_FILE = 'tokens/spotify_token.json'

# API Keys
GOODREADS_ACCESS_TOKEN = '<<GOODREADS_ACCESS_TOKEN>>'
GOOGLE_URL_SHORTENER_API_KEY = '<<GOOGLE_URL_SHORTENER_API_KEY>>'
MAPQUEST_CONSUMER_KEY = '<<MAPQUEST_CONSUMER_KEY>>'
MUSIXMATCH_API_KEY = '<<MUSIXMATCH_API_KEY>>'
NEWS_API_KEY = '<<NEWS_API_KEY>>'
OPEN_WEATHER_MAP_ACCESS_TOKEN = '<<OPEN_WEATHER_MAP_ACCESS_TOKEN>>'
SPOTIFY_API_KEY = '<<SPOTIFY_API_KEY>>'
TIME_ZONE_DB_API_KEY = '<<TIME_ZONE_DB_API_KEY>>'
TMDB_API_KEY = '<<TMDB_API_KEY>>'
WORDS_API_KEY = '<<WORDS_API_KEY>>'
YOUTUBE_DATA_API_KEY = '<<YOUTUBE_DATA_API_KEY>>'


# Local Testing
WIT_LOCAL_DATA = 'local/wit.json'

# When a new key is added above it needs to be added
# here as well.

api_keys = {

    # Facebook (+ Wit)
    'ACCESS_TOKEN': ACCESS_TOKEN,
    'VERIFY_TOKEN': VERIFY_TOKEN,
    'WIT_AI_ACCESS_TOKEN': WIT_AI_ACCESS_TOKEN,

    # Offline data sources
    'FACTS_SOURCE_FILE': FACTS_SOURCE_FILE,
    'JOKES_SOURCE_FILE': JOKES_SOURCE_FILE,
    'QUOTES_SOURCE_FILE': QUOTES_SOURCE_FILE,

    # Access token files
    'SPOTIFY_TOKEN_FILE': SPOTIFY_TOKEN_FILE,

    # API Keys
    'GOODREADS_ACCESS_TOKEN': GOODREADS_ACCESS_TOKEN,
    'GOOGLE_URL_SHORTENER_API_KEY': GOOGLE_URL_SHORTENER_API_KEY,
    'MAPQUEST_CONSUMER_KEY': MAPQUEST_CONSUMER_KEY,
    'MUSIXMATCH_API_KEY': MUSIXMATCH_API_KEY,
    'NEWS_API_KEY': NEWS_API_KEY,
    'OPEN_WEATHER_MAP_ACCESS_TOKEN': OPEN_WEATHER_MAP_ACCESS_TOKEN,
    'SPOTIFY_API_KEY': SPOTIFY_API_KEY,
    'TIME_ZONE_DB_API_KEY': TIME_ZONE_DB_API_KEY,
    'TMDB_API_KEY': TMDB_API_KEY,
    'WORDS_API_KEY': WORDS_API_KEY,
    'YOUTUBE_DATA_API_KEY': YOUTUBE_DATA_API_KEY
}



class GetConfig:
    '''
    The GetConfig class abstracts retrieving a key or data file name from the
    config file. Create a GetConfig using the name of the key as an argument.
    It will attempt to retrieve the key file with that name and save it as a
    string to the object's result data member. If retrieving the key raises an
    exception, result will be set to False, so it is recommended to check the
    value of the variable after creating a GetConfig object.

    Usage:
    accessor = config.GetConfig("NAME_OF_KEY_OR_DATA_FILE")
    key_string = accessor.result
    assert(key_string)

    Return:
    key_string is either a string representing the string associated with
    NAME_OF_KEY_OR_DATA_FILE in config.py.api_keys, or False if an exception was
    raised.
    '''

    def __init__(self, line_name):
        import os

        try:
            self.result = os.environ.get(line_name, api_keys[line_name])
        except:
            self.result = False