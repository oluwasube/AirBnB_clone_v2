#!/usr/bin/python3
"""start a flask web application"""
from flask import Flask


app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hnbn():
    """display Hello HBNB"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def show_hnbn():
    """display HBNB"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """display C followed by the value of text"""
    string = text.replace("_", " ")
    return "C {}".format(string)

@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_pythontext(text='is cool'):
    """display Python followed by the value of text"""
    string = text.replace("_", " ")
    return "Python {}".format(string)

@app.route("/number/<int:n>", strict_slashes=False)
def display_number(n):
    """display n is a number only if n is an integer"""
    return "{} is a number".format(n)

@app.route("/number_template/<int:n>", strict_slashes=False)
def display_htmlpage(n):
    """display a html page if n is an integer"""
    return render_template("5-number.html", n=n)

@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def show_odd_or_even(n):
    """display a HTML page if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
