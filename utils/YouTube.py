class YouTubeUtil:
    @staticmethod
    def get_video_url(id):
        return 'https://www.youtube.com/watch?v=' + id + '/'

    @staticmethod
    def get_channel_url(id):
        return 'https://www.youtube.com/channel/' + id + '/'
