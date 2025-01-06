from flask import Flask

app = Flask(__name__)

@app.route('/')
def Hello():
    return 'Hello World'

@app.route('/post/<int:id>')
def show_post(id):
    return f'This post has the id {id}'

@app.route('/user/<username>')
def show_user(username):
    return f'Hello {username}'


if __name__ == '__main__':
    app.run(debug= True)