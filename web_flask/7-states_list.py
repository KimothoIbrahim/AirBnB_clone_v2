#!/usr/bin/python3
""" setup to serve info from db """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states():
    """ return all states """
    States = storage.all("State").values()
    return render_template("7-states_list.html", States=States)

@app.teardown_appcontext
def teardown(execption):
    """ chnge session """
    storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
