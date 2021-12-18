from flask_restful import Resource
import csv

class LinkDao(object):

    def __init__(self, movieId: int, imdbId: int, tmdbId: int):
        self.movieId = movieId
        self.imdbId = imdbId
        self.tmdbId = tmdbId


class Link(Resource):
    def get(self):
        return links_serialized


links = []
with open('links.csv', newline='\n', encoding="utf8") as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

    for row in spamreader:
        links.append(LinkDao(row[0], row[1], row[2]))

links_serialized = []


def serialized_links(links: list[Link]):
    for link in links:
        print(link.__dict__)
        links_serialized.append(link.__dict__)


serialized_links(links)
