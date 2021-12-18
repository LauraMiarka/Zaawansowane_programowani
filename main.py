from flask import Flask
from flask_restful import Api
from movies import *
from links import *
from tags import *
from ratings import *

app = Flask(__name__)
api = Api(app)

api.add_resource(Movie, '/movies')
api.add_resource(Link, '/links')
api.add_resource(Rating, '/ratings')
api.add_resource(Tag, '/tags')


if __name__ == '__main__':
    app.run(debug=True)