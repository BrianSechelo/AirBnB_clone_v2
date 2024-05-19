#!/usr/bin/python3
"""Starts a Flask web application
"""
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def home():
    """ 
    Displays Hello HBNB!.  
    """
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """
    Displays HBNB.
    """
    return "HBNB"

@app.route('/c/<text>')
def c_with_params(text):
        """
        is_cool
        """
        text_no_underscore = text.replace('_', ' ')
        return "c {}".format(text_no_underscore)

@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>')
def python_with_params(text):
        """
        is_cool
        """
        text_no_underscore = text.replace('_', ' ')
        return "Python {}".format(text_no_underscore)

@app.route('/number/<int:n>')
def number(n):
        """
        Display "n" if  n is a number
        """
        return "{} is a number".format(n)

@app.route('/number_template/<int:n>')
def number_template(n):
        """
        Display template if n is a number
        """
        return render_template('5-number.html', number=n)

@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
	"""
	Display page only if n is an interger
	"""
	even_or_odd = "even" if n % 2 == 0 else "odd"
	values = {
	  "number": n,
	  "even_or_odd": even_or_odd
	}
	return render_template('6-number_odd_or_even.html', values=values)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
