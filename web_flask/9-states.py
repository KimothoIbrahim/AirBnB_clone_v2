#!/usr/bin/python3
""" setup to serve info from db """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def stateslist():
    """ return all states """
    States = storage.all("State")
    return render_template("9-states.html", state=States)


@app.route("/states/<id>", strict_slashes=False)
def states(id):
    """ return all states """
    States = storage.all("State")
    for state in States.values():
        print(state.id, id)
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(execption):
    """ chnge session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
