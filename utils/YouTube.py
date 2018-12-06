class YouTubeUtil:
    def searchyoutube(term):
        return ("https://www.google.com/search?q="+ term +"+site:www.youtube.com&btnI")
    @staticmethod
    def get_video_url(id):
        return 'https://www.youtube.com/watch?v=' + id + '/'

    @staticmethod
    def get_channel_url(id):
        return 'https://www.youtube.com/channel/' + id + '/'
    def spotify_to_youtube()