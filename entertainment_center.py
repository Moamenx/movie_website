import media
import learning

the_god_father = media.Movie("The God Father",
                             "The aging patriarch of an organized crime dynasty transfers control of his clandestine "
                             "empire to his reluctant son.",
                             "thegodfather.jpg",
                             "https://www.youtube.com/watch?v=sY1S34973zA")
brave_heart = media.Movie("Braveheart"
                          , "When his secret bride is executed for assaulting an English soldier who tried "
                            "to rape her, Sir William Wallace begins a revolt against King Edward I of "
                            "England."
                          , "braveheart.jpg"
                          , "https://www.youtube.com/watch?v=1cnoM8EiGGU")
threehundred = media.Movie("300",
                           "King Leonidas of Sparta and a force of 300 men fight the Persians at Thermopylae in 480 "
                           "B.C."
                           , "300.jpg"
                           , "https://www.youtube.com/watch?v=UrIbxk7idYA")
messi = media.Movie("Messi"
                    , "Lionel Messi from early life to international stardom."
                    , "messi.jpg"
                    , "https://www.youtube.com/watch?v=wWVvfuZlqSM")
movies = [the_god_father, messi, threehundred, brave_heart]

learning.open_movies_page(movies)
