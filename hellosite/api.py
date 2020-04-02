from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class Home(Resource):
  def get(self):
    return "Please input your search in the form of '/<username>/<cycle_number>'"

  def post(self):
    return "Here's what happen when post is activated"

class Search(Resource):
  def get(self, username, id):
    return "Thanks, you sent: " + str(username) + ' and ' + str(id)

api.add_resource(Home, '/')
api.add_resource(Search, '/<username>/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)