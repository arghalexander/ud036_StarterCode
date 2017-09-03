from media import Movie
from fresh_tomatoes import open_movies_page

'''
This file is a generator for both the movies, their data, and the html page itself.
It will create the movies added here, put them in a file, and open that file in your browser.
'''

walle = Movie('Wall-E', 'https://resizing.flixster.com/NUT-f5bym9L1h5q6uB2OYkTZveU=/206x305/v1.bTsxMjI3OTQxNjtqOzE3NDY3OzEyMDA7MjAzMjszMDQ4', 'https://www.youtube.com/watch?v=alIq_wG9FNk')
up = Movie('Up', 'https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg', 'https://www.youtube.com/watch?v=pkqzFUhGPJg')
avatar = Movie('Avatar', 'http://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp', 'https://www.youtube.com/watch?v=cRdxXPV9GNQ')

movies = (walle, up, avatar)

open_movies_page(movies)
