from flask_restful import Resource
import csv
from datetime import datetime


class RatingDao(object):

    def __init__(self, userId: int, movieId: int, rating: float,
                 timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.rating = rating
        self.timestamp = timestamp


class Rating(Resource):
    def get(self):
        return ratings_serialized


ratings = []
with open('ratings.csv', newline='\n', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in spamreader:
        ratings.append(RatingDao(row[0], row[1], row[2], row[3]))

ratings_serialized = []


def serialized_ratings(ratings):
    for rating in ratings:
        print(rating.__dict__)
        ratings_serialized.append(rating.__dict__)


serialized_ratings(ratings)

