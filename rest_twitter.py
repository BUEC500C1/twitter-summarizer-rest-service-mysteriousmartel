from flask import Flask, request, render_template, redirect, abort, send_file
from flask_restful import Resource, Api, reqparse
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import os
import tweet_queue as tq

app = Flask(__name__)
api = Api(app)

class SearchForm(FlaskForm):
  username = StringField('Twitter username (without "@")', validators=[DataRequired()])
  cycles = StringField('Number of cycles', type=int, validators=[DataRequired()])
  submit = SubmitField('Submit')

# parser = reqparse.RequestParser()

# parser.add_argument('username', type=str, dest='name', required=True, help='Username without "@"')
# parser.add_argument('cycles', type=int, dest='cycles', required=True, help='Number of cycles to index through')

# args = parser.parse_args()

@app.route('/search', methods=['GET', 'POST'])

def search():
	form = SearchForm()
	Handles = []
	Cycles = []
	if form.validate_on_submit():
		Handles.append(form.username.data)
		Cycles.append(form.cycles.data)
		tq.main(Handles,Cycles)
		return redirect('/feedvideo')
	return render_template('feedSearch.html', form=form)

@app.route('/feedvideo', methods=['GET', 'POST'])

def feedvideo():
	video_name = SearchForm.username + '_tweetVid.mp4'
	try:
		return send_file(video_name)
	except:
		return abort(400, 'Unable to compile video for given handle')

if __name__ == "__main__":
    app.run(debug = True,host = '0.0.0.0',port = 80)    