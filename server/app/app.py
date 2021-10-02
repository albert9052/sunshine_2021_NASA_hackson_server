from flask import Flask
from flask_restful import Resource, Api, reqparse
import pandas as pd
import ast

app = Flask(__name__)
api = Api(app)
    
class Api(Resource):
    def get(self):
        
        parser = reqparse.RequestParser()  # initialize
        
        parser.add_argument('userId')  # add args
        parser.add_argument('name')
        parser.add_argument('city')
        
        args = parser.parse_args()  # parse arguments to dictionary

        data = {'hi': 123, 'list': [0, 1, 2, 3], 'yo': args['userId']}
        return {'data': data}, 200
    
api.add_resource(Api, '/api')

if __name__ == '__main__':
    app.run()
