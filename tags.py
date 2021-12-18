from flask_restful import Resource
import csv
from ratings import datetime


class TagDao(object):

    def __init__(self, userId: int , movieId: int, tag: str,
                 timestamp: datetime):
        self.userId = userId
        self.movieId = movieId
        self.tag = tag
        self.timestamp = timestamp


class Tag(Resource):
    def get(self):
        return tags_serialized


tags = []
with open('tags.csv', newline='\n', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in spamreader:
        tags.append(TagDao(row[0], row[1], row[2], row[3]))

tags_serialized = []


def serialized_tags(tags):
    for tag in tags:
        print(tag.__dict__)
        tags_serialized.append(tag.__dict__)


serialized_tags(tags)
