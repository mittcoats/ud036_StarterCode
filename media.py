import webbrowser

# Constructor for building movies
class Movie():
	def __init__(self, 
							 movie_title,
							 movie_summary,
							 movie_poster_img,
							 movie_trailer_url,
							 movie_studio,
							 movie_lead_actor):

		self.title 					= movie_title
		self.summary 				= movie_summary
		self.poster_img_url = movie_poster_img
		self.trailer_url 		= movie_trailer_url
		self.studio 				= movie_studio
		self.lead_actor 		= movie_lead_actor

	def show_trailer(self):
			webbrowser.open(self.trailer)
