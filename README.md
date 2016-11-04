To use this source code for a Movie Trailer website, you must install Pyton. Python 2.7.12 is the python version used in this implementation, feel freeto adapt the code for a different version of python.


The file media.py creates a class that is responsible for defining different attributes about about the movies you wish to display. It is unnecessary to modify this file unless you wish to display more attributes for each movie.

In the file entertainment_center.py set variables to take the parameters of the attributes defined in the media.py file like so, 

movie_title_var = media.Movie("movie_title",
                                "movie_storieline",
                                "movie_poster-image_url",
                                "movie_trailer_url")

don't forget to set a variable called movies and set it to an array of the movies you have chosen. Like this,

movies = [movie_title_var 1, movie_title_var 2, movie_title_var 3]

and then call it in this function,

fresh_tomatoes.open_movies_page(movies)

the fresh_tomatoes.py file is responsible for creating the index.html file for your web page.

Run the entertainment center module to view your web page.