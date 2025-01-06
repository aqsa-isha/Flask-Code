from flask import Flask, url_for, redirect
app = Flask(__name__)


@app.route('/admin')
def Hello_Admin():
    return 'Hello Admin...'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return f'Hello {guest}'

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))
    
if __name__ == '__main__':
    app.run(debug = True)
    

