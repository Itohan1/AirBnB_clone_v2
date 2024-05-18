#!/usr/bin/python3
"""Write a script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def Hello_HBNB():
    """display “Hello HBNB!”"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """display “HBNB”"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text(text):
    """display C followed by the value of the text variable"""
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route('/python/', strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pytext(text="is cool"):
    """display Python followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """display n is a number only if n is an integer"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.template_filter('odd_or_even')
def oddeven(n):
    """check if the number is odd or even"""
    if n % 2:
        return f"{n} is even"
    else:
        return f"{n} is odd"


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer"""
    return render_template("6-number_odd_or_even.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
