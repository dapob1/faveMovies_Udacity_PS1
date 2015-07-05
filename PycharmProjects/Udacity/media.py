import webbrowser

class Movie():
    """This class provides a way to store and display movie related information"""


    """A class that creates movie summary for a movie website"""
    def __init__(self,title, storyline, poster_image_url,trailer_youtube_url,director):

        assert isinstance(title, object)
        self.title = title

        assert isinstance(storyline, object)
        self.storyline = storyline

        assert isinstance(poster_image_url, object)
        self.poster_image_url = poster_image_url

        assert isinstance(trailer_youtube_url, object)
        self.trailer_youtube_url = trailer_youtube_url

        assert isinstance(director,object)
        self.director = director

    def show_trailer(self):
        webbrowser.open(self.youtube_trailer)