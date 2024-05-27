#!/usr/bin/python3
""" flask app to serve airbnb clone """

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """ return states, cities and amenities """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()

    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


if __name__ == "__main__":
    """ start app """
    app.run(host="0.0.0.0", port=5000)
