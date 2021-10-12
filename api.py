#!/usr/bin/env python3
from flask import Flask
from flask_restful import Api, Resource
import datetime

app = Flask(__name__)
api = Api(app)

date = {
    "date": str(datetime.datetime.now())
}

class Date(Resource):
    def get(self):
        return date, 200

api.add_resource(Date, '/date')

if __name__ == '__main__':
    app.run(debug=True)
