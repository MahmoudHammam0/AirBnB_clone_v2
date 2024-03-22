#!/usr/bin/python3
'HBNB module'
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    'Hello HBNB!'
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    'HBNB home'
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    'C + text'
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    'python + text'
    text = text.replace('_', ' ')
    return f'Python {text}'


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
