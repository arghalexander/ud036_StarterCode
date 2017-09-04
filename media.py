class Movie():

	'''
	A simple class to store movie data.
	When you need to create a new instance, pass this data to the constructor. 
	You can then call it using instance.title, or similar.
	'''
	
	def __init__(self, title, poster_image_url, trailer_youtube_url):
		
		'''
		Stores the passed data in variables,
		accessable by 'movie_name.variable'.
		'''
		
		self.title = title
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url
