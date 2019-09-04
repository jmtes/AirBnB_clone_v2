#!/usr/bin/python3
''' Start a Flask web app. '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder='./templates')
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    ''' Render HBNB page. '''
    states = storage.all('State').values()
    amenities = storage.all('Amenity').values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    ''' Close SQLAlchemy session. '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
