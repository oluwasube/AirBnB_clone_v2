#!/usr/bin/python3
"""start a flask web application for HBNB project"""
from flask import Flask
from flask import render_template
from models import storage
from models import State

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def display_cities():
    """show cities by states on the HTML page"""
    all_states = storage.all(State)
    return render_template("8-cities_by_states.html", allStates=all_states)


@app.teardown_appcontext
def remove_currentsession(exception):
    """remove current session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")