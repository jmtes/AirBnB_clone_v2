#!/usr/bin/python3
''' Start a Flask web app. '''
from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def home():
    ''' Return home page data. '''
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run()
