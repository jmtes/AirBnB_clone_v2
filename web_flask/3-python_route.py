#!/usr/bin/python3
''' Start a Flask web app. '''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    text = text.replace('_', ' ')
    return "Python " + text


if __name__ == '__main__':
    app.run()
