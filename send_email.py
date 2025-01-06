# flask Mail extension makes it very easy to set up a simple interface
# with any mail to the users or client.

# MAIL_SERVER: Name/IP address of email server
# Mail_PORT: Port number of served use
# MAIL_USE_TLS: Enable/disable Transport Security Layer encryption
# MAIL_USE_SSL: Enable/Disable Secure Socket Layer Encryption
# MAIL DEBUG: Debug Support, Default is Flask application's debug status.
# MAIL_USERNAME: User name of sender
# MAIL_PASSWORD: password of sender
# MAIL_DEFAULT_SENDER: sets default sender
# MAIL_MAX_EMAILS: Sets maximum mails to be sent
# MAIL_SUPPRESS_SEND: Sending suppressed if app.testing set to be TRUE
# MAIL_ASCII_ATTACHMENTS: if set to be true, attached filenames
# converted to ASCII.

# Methods of Mail Class
# send(): Send contents of Message class object
# connect(): Opens connection with mail host
# send_messages(): Sends message object

# Message Class Methods:
# attach()- adds an attachement to message.
# filename: name of file to attach
# content_type: MIME type of file
# data:raw file data
# disposition: content disposition if any
# add_recipient: adds another recipient to message

# pip install flask-mail

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# Configuration for the mail server
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'yourId@gmail.com'
app.config['MAIL_PASSWORD'] = '*****'  # Replace with your actual password
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

# Initialize Mail
mail = Mail(app)

@app.route('/')
def index():
    # Create a message
    msg = Message('Hello', sender='yourId@gmail.com', recipients=['id1@gmail.com'])
    msg.body = "Hello Flask message sent from Flask-Mail"
    
    # Send the email
    mail.send(msg)
    
    return "Sent"

if __name__ == '__main__':
    app.run(debug=True)
