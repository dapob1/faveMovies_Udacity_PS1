import webbrowser

class Movie():
    """This class provides a way to store and display movie related information"""

    VALID_RATINGS =["G", "PG", "PG-13", "R"]

    """A class that creates movie summary for a movie website"""
    def __init__(self,title, storyline, poster_image_url,trailer_youtube_url):
        """

        :rtype : object
        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        #why did jetbrains suggest: assert isinstance(youtube_trailer, object)
        self.trailer_youtube_url = trailer_youtube_url
    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)