#!/usr/bin/python3
''' Start a Flask web app. '''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    ''' Return home page data. '''
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    ''' Return hbnb page data. '''
    return "HBNB"


@app.route('/c/<text>')
def c(text):
    ''' Return c page data.

        Args:
            text - Text to print.
    '''
    text = text.replace('_', ' ')
    return "C " + text


if __name__ == '__main__':
    app.run()
