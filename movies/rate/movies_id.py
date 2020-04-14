import pandas as pd
import numpy as np
from random import randint
import requests
import json

imdb = pd.read_csv(filepath_or_buffer='rate/IMDBdata_hotlist2.csv')
movie_id = imdb.drop(['Movie_Title', 'YR_Released', 'Rating', 'Num_Reviews','Record', 'Runtime'], axis=1)


class MovieResponse:
    def __init__(self, movie_info):
        self.title = movie_info['Title']
        self.image = movie_info['Poster']
        self.genre = movie_info['Genre']
        self.actors = movie_info['Actors']
        self.director = movie_info['Director']

def get_Movie():
    ran = randint(1, 850)
    random_movie = (movie_id.iloc[ran]).Movie_ID
    movie_info = requests.get("http://www.omdbapi.com/?apikey=2571f659&i=" + random_movie)
    return MovieResponse(movie_info.json())