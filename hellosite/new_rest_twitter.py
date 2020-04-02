from flask import Flask, request, redirect, abort, send_file
from flask_restful import Resource, Api, reqparse
import os
# import tweet_queue as tq

app = Flask(__name__)
api = Api(app)

class Home(Resource):
  def get(self):
    return "Please input your search in the form of '/<username>/<cycle_number>'"

class Search(Resource):
  def get(self, username, id):
    fileName = '/media/sf_EC601/EC500/hw3/hellosite/requirements.txt'
    try:
      return send_file(fileName)
    except:
      return "Unable to return video. Please try a different search term."

api.add_resource(Home, '/')
api.add_resource(Search, '/<username>/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)  