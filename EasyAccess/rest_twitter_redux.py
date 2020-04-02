from flask import Flask, request, send_file
from flask_restful import Resource, Api
import os
import tweet_queue as tq

''' Please use the commented out lines with
    your local file path if running locally.
    All tests utilizing the instance should
    leave the script as is. '''

app = Flask(__name__)
api = Api(app)

class Home(Resource):
  def get(self):
    return "Please input your search in the form of '/<username>/<cycle_number>'"

class Search(Resource):
  def get(self, username, id):
    nameList = [username]
    cycleList = [id]
    tq.main(nameList, cycleList)
    # folderName = '/media/sf_EC601/EC500/hw3/' + username + '_Video/'
    folderName = '/home/ec2-user/hw3/' + username + '_Video/'
    fileName = folderName + username + '_tweetVid.mp4'
    try:
      return send_file(fileName, as_attachment=True)
    except:
      return "Unable to return video. Please try a different search term."

api.add_resource(Home, '/')
api.add_resource(Search, '/<username>/<int:id>')

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(debug=True, host="0.0.0.0", port=80)  