#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ removes the current SLQAlchemy Session """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """ displays 7-states_list.html page """
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
