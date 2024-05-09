#!/usr/bin/python3
""" Starts a Flask app """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message """
    return 'Hello HBNB!'

if __name__ == "__main__":
    """ Main """
    app.run(host='0.0.0.0', port=5000)
