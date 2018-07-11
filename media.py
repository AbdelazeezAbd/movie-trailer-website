#defining the class is called movie
class movie():
    """here we put movies information that is required create
       a movie trailer"""
    #defining __init__ function with the movie data parameters
    #to take a place in the memory
    def __init__(self, movie_title, poster_image, trailer_youtube):
        #using self parameter we define instance variables
        self.title = movie_title #defining an instance variable to put movie title
        self.poster_image_url = poster_image #defining an instance variable
                                             #to put poster image URL
        self.trailer_youtube_url = trailer_youtube #defining an instance variable
                                                   #to put trailer youtube URL
        #here is the end of instance variables
