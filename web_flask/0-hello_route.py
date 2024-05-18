#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, request
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
