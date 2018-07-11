# movie-trailer-website
this project is web page that contains some movie trailers , every movie contains:
* movie title
* movie poster image
* movie trailer video

this web page was created by three python files:

### media.py
this file contains the class is called 'movie', this class only contains __init__ function, this function takes several parameters that is required for
movie trailer like: self, movie_title, poster_image, trailer_youtube
then in __init__ function we define instance variables using self parameter.

### fresh_tomatoes.py
this file contain simple web page using HTML,CSS,JS , and the end of the file we have a function is called open_movies_page, by using it we can relate
our movies with web page, so we can put infinite number of movies

### entertainment_center.py
in this file we firstly import media.py and fresh_tomatoes.py inside this file, then we start creating the variables that contain movies information,
we set the information using movie class in media.py file, we must put the information with a specific arrangement according to the parameters in __init__
function in media.py, the arrangment is:
1. movie title
2. movie poster image URL
3. movie youtube trailer URL

at the end of the file we create a list that contains all the variable names, then we make the list is the input in open_movies_page function that is in fresh_tomatoes.py
file to relate the movies data with web page and run the trailers there.

## Running the web page
in order to run the web page with movie trailers we must put all the files inside the same folder, and we must run entertainment_center.py file specifically, Because it
relates all files with it
