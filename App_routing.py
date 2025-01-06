from flask import Flask

app = Flask(__name__)

# App routing means mapping the URLs to a specific function that will handle 
# the logic for that URL.
# App routing means mapping the URLs to a specific functions that will handle the logic of that URL.

@app.route('/home')
def Hello():
    return 'Welcome to my Home Page...'


@app.route('/')
def index():
    return 'Welcome to Aptech center'

@app.route('/user/<username>')
def show_user(username):
    return f'Hello {username}'

if __name__ == '__main__':
    app.run(debug = True)
    
# App routing means mapping the URL to a specific function that will handle the lgic of URL.
# App routing means mapping the url to a specific function that will handle the logic of URL.
# App routing means mapping the url to a specific function that will handle the logic of the URl
# We can also build dynamic URls by using varible in the URL. To add variables to URLs, use <variable_name> rule. tHe function then receives the <variable_name> as kyword argument.
# We can also build dynamic URLs by using variable in the URL. To add variables to URLs, use <variable> namerule
