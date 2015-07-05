import media        # Import media to create instances of movie object
import fresh_tomatoes       #Import fresh_tomatoes that will be used to display HTML of my favorite movies page

"""Create instances of movie object for my favourite movies. This is represented with the title, story, image, trailer url, and director"""
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "John Lasseter")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=a0CDJZu4M5I",
                     "James Cameron")


the_shawshank_redemption = media.Movie("The Shawshank Redemption",
                                "Perseverance against all odds",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/8/81/ShawshankRedemptionMoviePoster.jpg/220px-ShawshankRedemptionMoviePoster.jpg",
                                "www.youtube.com/watch?v=6hB3S9bIaco",
                                "Frank Darabont")

city_of_god = media.Movie("City of God",
                           "Young criminals in Rio",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/1/10/CidadedeDeus.jpg/220px-CidadedeDeus.jpg",
                           "www.youtube.com/watch?v=ioUE_5wpg_E",
                           "Fernando Meirelles & Katia Lund")

movies = [toy_story,avatar,the_shawshank_redemption,city_of_god]        # Store the movie instances in a list
fresh_tomatoes.open_movies_page(movies)     # Create HTML file output and display on default browser
