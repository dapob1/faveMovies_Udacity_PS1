import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
#print (toy_story.storyline)

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=a0CDJZu4M5I")
#print avatar.storyline
#avatar.show_trailer()

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "https://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "www.youtube.com/watch?v=XCwy6lW5Ixc")
ratatouille = media.Movie("Ratatouille",
                          "A rat is a chef in Paris",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                          "www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                                "Going back in time to meet authors",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
                                "www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games",
                           "A really real reality show",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/a/ab/Hunger_games.jpg/220px-Hunger_games.jpg",
                           "www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
#fresh_tomatoes.open_movies_page(movies)
#print media.Movie.__module__
#print media.Movie.__name___
#print media.Movie.__dict__
#print media.Movie.__doc__