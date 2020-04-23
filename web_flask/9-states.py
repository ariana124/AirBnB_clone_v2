#!/usr/bin/python3
"""
script that starts a Flask web app
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ removes the current SQLAlchemy Session """
    storage.close()


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states(id=None):
    """ displays the 9-states.html page """
    states = storage.all("State")
    if id is not None:
        state = "State.{}".format(id)
        state = states.get(state) # returns the state name (key value)
        return render_template("9-states.html", state=state)
    else:
        return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
