#!/usr/bin/python3
'List of Cities module'
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def list_states(id=None):
    'display list cities by states'
    states = storage.all(State).values()
    return render_template('10-hbnb_filters.html', states=states)


@app.teardown_appcontext
def app_teardown(exception):
    'close sql alchemy session after each request'
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
