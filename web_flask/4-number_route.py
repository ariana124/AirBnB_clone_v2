#!/usr/bin/python3
"""
starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ displays Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ displays HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ displays C followed by the value of the text variable """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """ displays python followed by the value of the text variable """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ displays n is a number only if n is an integer """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
