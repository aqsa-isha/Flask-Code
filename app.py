# Flask is a web application framework written in Python. It is developed by Armin Ronacher, who leads an international group of Python enthusiasts named Pocco. Flask is based on the Werkzeug WSGI toolkit and Jinja2 template engine. Both are Pocco projects.
# String: It is the default type and it accepts any text without a slash.
# int: It accepts positive integers.
# float: It accepts floating point numbers.
# path: It is like a string but also accepts slashes.
# uuid: It accepts uuid path.

from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug = True)
