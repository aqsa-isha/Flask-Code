from flask import Flask, url_for

app = Flask(__name__)

def hello_world():
    return 'Hello World....'
    app.url_for('/', 'hello', hello_world)

if __name__ == '__main__':
    app.run()