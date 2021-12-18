from flask_restful import Resource
import csv


class MovieDao(object):

    def __init__(self, movieId: int, title: str, genres: str):
        self.movieId = movieId
        self.title = title
        self.genres = genres


class Movie(Resource):
    def get(self):
        return movies_serialized


movies = []
with open('movies.csv', newline='\n', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in spamreader:
        movies.append(MovieDao(row[0], row[1], row[2]))

movies_serialized = []


def serialized_movies(movies):
    for movie in movies:
        print(movie.__dict__)
        movies_serialized.append(movie.__dict__)


serialized_movies(movies)
