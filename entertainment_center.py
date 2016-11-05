import fresh_tomatoes                                                           
import media

# create a variable for each movie to be included in website.
# make sure to include a title, storyline, poster image url and trailer url.
toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come"
            "to life",
            "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
            "https://www.youtube.com/watch?v=vwyZH85NQC4")

avatar = media.Movie("Avatar", "A marine on an alien planet.",
            "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", # NOQA
            "http://www.youtube.com/watch?v=-9ceBgWV8io")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn.",
            "http://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg", # NOQA
            "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille", "A rat is a chef in Paris.",
            "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg", # NOQA
            "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to"
            "meet aurthors.",
            "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg", # NOQA
            "https://www.youtube.com/watch?v=atLg2wQQxvU")

hunger_games = media.Movie("Hunger Games", "A really real reality show.",
            "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg", # NOQA
            "https://www.youtube.com/watch?v=PbA63a7H0bo")

rio_2 = media.Movie("Rio 2", "A family of Blue Macaws learns they might not be"
            "the last of their kind.",
            "https://upload.wikimedia.org/wikipedia/en/thumb/6/67/Rio_2_Poster.JPG/220px-Rio_2_Poster.JPG", # NOQA
            "https://www.youtube.com/watch?v=JtP7zka5UI8")

frozen = media.Movie("Frozen", "An ice queen must learn to control her powers.",
            "https://upload.wikimedia.org/wikipedia/en/thumb/0/05/Frozen_%282013_film%29_poster.jpg/220px-Frozen_%282013_film%29_poster.jpg", # NOQA
            "https://www.youtube.com/watch?v=-WdC4DaYIeQ")

how_to_train_your_dragon = media.Movie("How to Train Your Dragon",
            "A viking boy must prove himself worthy.",
            "https://upload.wikimedia.org/wikipedia/en/thumb/9/99/How_to_Train_Your_Dragon_Poster.jpg/220px-How_to_Train_Your_Dragon_Poster.jpg", #NOQA
            "https://www.youtube.com/watch?v=VEcM3rbnwQ4")                    
                    
# create a movies array containing the variable names for each movie.
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
          hunger_games, rio_2, frozen, how_to_train_your_dragon]

# call the fresh tomatoes module to create the index.html file.
fresh_tomatoes.open_movies_page(movies)
