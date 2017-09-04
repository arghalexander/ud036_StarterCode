from media import Movie
from fresh_tomatoes import open_movies_page

'''
This file is a generator for both the movies,
their data, and the html page itself.
It will create the movies added here,
put them in a file, and open that file in your browser.
'''

walle = Movie(
    'Wall-E',
    'https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg',
    'https://www.youtube.com/watch?v=alIq_wG9FNk')
up = Movie(
    'Up',
    'https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg',
    'https://www.youtube.com/watch?v=pkqzFUhGPJg')
avatar = Movie(
    'Avatar',
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://www.youtube.com/watch?v=cRdxXPV9GNQ')

movies = (walle, up, avatar)

open_movies_page(movies)
'''
This function opens the created list of movies,
generates an HTML file with the movies inside,
saves said file, and opens a new browser tab
from the HTML file.
'''
