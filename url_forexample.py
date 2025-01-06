from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/success/<name>')
def hello_user(name):
    return f'Welcome {name}, Welcome to Aptech Learning...'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('hello_user', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('hello_user', name=user))
    
if __name__ == '__main__':
    app.run(debug=True)