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


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ cisfun """
    spaced = text.replace("_", " ")
    return f"C {spaced}"


@app.route("/python/")
@app.route("/python/<text>", strict_slashes=False)
def pyth(text="is cool"):
    """ pyth/text """
    spaced = text.replace("_", " ")
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
