from flask import Flask, render_template, redirect, url_for, flash
import os
app = Flask(__name__)
# Flashing is a mechanism to send one time messages from the server 
#to the client typically to inform users about the success 
#or failure of an action warning and other feedback.

app.secret_key = os.urandom(24)

@app.route('/')
def index():
    return render_template('flash.html')

@app.route('/flash')
def flash_message():
    flash('This is a Flashing messages')
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug = True)
