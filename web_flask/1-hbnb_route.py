#!/usr/bin/python3
""" run flask """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def greet():
    """ ftest function """
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ to /hbnb """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
