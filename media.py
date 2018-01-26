import webbrowser


class Movie():
    """ This is the base attributes of any movie"""
    def __init__(self,
                 movie_title,
                 story_line,
                 poster_image_url,
                 trailer_youtube_url):
        """ The constructor method takes 4 parameters movie title,
         storyline, poster image url and youtube trailer
        url """
        self.title = movie_title
        self.story_line = story_line
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        """ This method opens the browser's with the movie's trailer"""
        webbrowser.open(self.trailer_youtube_url)
