#!/usr/bin/python3
''' Start a Flask web app. '''
from flask import Flask, abort

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


@app.route('/python')
@app.route('/python/<text>')
def python(text='is cool'):
    ''' Return python page data.

        Args:
            text - Text to print.
    '''
    text = text.replace('_', ' ')
    return "Python " + text


@app.route('/number/<n>')
def number(n):
    ''' Return number page data.

        Args:
            n - Number

        Exceptions:
            - Abort with a 404 error if n is not an integer.
    '''
    if n.isdigit():
        return n + " is a number"
    abort(404)


if __name__ == '__main__':
    app.run()
