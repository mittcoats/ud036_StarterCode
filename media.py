import webbrowser


class Movie():
    """
    This constructor takes an array of values and returns a movie object
    with each of the values in the array assigned as properties of the object.

    The classes show_trailer() method takes a movie object as a parameters, and
    uses the trailer value to launch a web browser page displaying the trailer.
    """
    def __init__(self,
                 movie_title,
                 movie_summary,
                 movie_poster_img,
                 movie_trailer_url,
                 movie_studio,
                 movie_lead_actor):

        self.title = movie_title
        self.summary = movie_summary
        self.poster_img_url = movie_poster_img
        self.trailer_url = movie_trailer_url
        self.studio = movie_studio
        self.lead_actor = movie_lead_actor

    def show_trailer(self):
        webbrowser.open(self.trailer)
