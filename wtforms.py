# WTForms is a flexible forms validation and rendering library for Python web development. 
# It is often used in Flask applications for handling forms in a clean, efficient, and secure way.

# Pip install flask-WTF
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired
import os

app = Flask(__name__)

app.secret_key = os.urandom(24)

# Define the Form class
class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    message = ""
    if form.validate_on_submit():
        name = form.name.data
        age = form.age.data
        message = f"Hello, {name}! You are {age} years old."
    return render_template('contact.html', form=form, message=message)


if __name__ == '__main__':
    app.run(debug=True)
