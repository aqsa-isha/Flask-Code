from flask import Flask, redirect, url_for, render_template, request, session, abort
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # To securely store session data

@app.route('/')
def index():
    return render_template('session.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        # Correct the conditional statement
        if username == 'Admin' or username == 'Aqsa':  # Logical OR
            session['username'] = username  # Store username in session
            return redirect(url_for('success'))
        else:
            abort(401)  # Unauthorized if the username is incorrect
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    if 'username' in session:  # Check if user is logged in
        return f"Logged in successfully as {session['username']}"
    return redirect(url_for('index'))  # Redirect if user is not logged in

if __name__ == '__main__':
    app.run(debug=True)
