#!/usr/bin/python3
""" script that starts a Flask web application """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def app_home():
    """ function returns Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """ function returns HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ function returns c and value of text"""
    return "C " + text.replace('_', ' ')


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """function returns python and value of text"""
    return "Python " + text.replace('_', ' ')


@app.route("/number/<n>", strict_slashes=False)
def number_route(n):
    """function returns value of n if n is integer"""
    return "{} is a number".format(int(n))


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n):
    """function display html page if n is integer"""
    return render_template("5-number.html", num=int(n))


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n):
    """function display html page if n is integer and specify if even or odd"""
    return render_template("6-number_odd_or_even.html", num=int(n))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
