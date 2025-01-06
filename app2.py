from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')
def Hello_User(name):
    return 'Hello {}'.format(name)

if __name__ == '__main__':
    app.run(debug = True)
    
    
app.route('/')
def Hello():
    return 'Hello'

