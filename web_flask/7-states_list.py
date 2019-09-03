#!/usr/bin/python3
''' Start a Flask web app. '''
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__, template_folder='./templates')
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    ''' Return page data for list of States. '''
    states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_request
def teardown(exception):
    ''' Remove current SQLAlchemy session. '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
