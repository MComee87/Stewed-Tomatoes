import webbrowser

"""
Attributes:
    title (str): create a title attr for each movie instance.
    storyline (str): create a storyline attr for each movie instance.
    poster_image_url (str): create a url attr for the poster image of each movie instance.
    trailer_youtube_url (str): create a youtube url attr for the trailer of each movie instance.
"""

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
# define a function to show the movies trailers.
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
