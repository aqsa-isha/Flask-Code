# flask is micro web framework
from flask import Flask
# Flask is developed on 1st April 2010 by Armin Ronacher who is the lead of python enthusiast group.
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'

if __name__ == '__main__':
    app.run(debug = True)
    # debug = True: during development if there ius an error it will show.
    
# jinja template is simply a text file. Jinja can generate any text based on HTML, XML and CSv.                             
