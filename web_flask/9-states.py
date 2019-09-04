#!/usr/bin/python3
''' Start a Flask web app. '''
from flask import Flask, render_template
from models import storage

app = Flask(__name__, template_folder='./templates')
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states(id=None):
    ''' Render page with State info. '''
    if id:
        state = storage.get_obj('State', id)
        return render_template('9-states.html', state=state)
    states = sorted(list(storage.all('State').values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_request
def teardown(exception):
    ''' Remove current SQLAlchemy session. '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0')
