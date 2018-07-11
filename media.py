#defining the class is called movie
class movie():
    #defining __init__ function with the movie data parameters to take a place in the memory
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        #using self parameter we define instance variables
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        #here is the end of instance variables
