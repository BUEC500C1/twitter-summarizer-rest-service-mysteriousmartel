from flask import Flask, request
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hi'

@app.route('/hello/<username>')
def hello(username):
  return 'Would you like a potato, ' + username

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return "Thanks!"
    else:
        return "Try again later!"