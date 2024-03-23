#!/usr/bin/python3
'List of states module'
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_states():
    'display list of states'
    states_list = storage.all(State).values()
    return render_template('7-states_list.html', states_list=states_list)


@app.teardown_appcontext
def session_close(exception):
    'close sql alchemy session after each request'
    storage.close()


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
