from flask import Flask, request, redirect, url_for, render_template, session

import os


app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('session.html')

@app.route('/set_session', methods=['POST'])
def set_session():
    session['username'] = request.form['username']
    return redirect(url_for('get_session'))

@app.route('/get_session')
def get_session():
    if 'username' in session:
        username = session['username']
        return f'Hello, {username}'
    return 'No username set in session'

if __name__ == '__main__':
    app.run(debug = True)