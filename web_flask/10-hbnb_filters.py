#!/usr/bin/python3
""" Task 11. HBNB filters """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.route("/hbnb_filters")
def hbnb_filters():
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template("10-hbnb_filters.html", states=states,
                           amenities=amenities)


@app.teardown_appcontext
def to_close(err):
    """ close app context """
    storage.close()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
