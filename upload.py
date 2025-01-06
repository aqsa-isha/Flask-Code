from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
# filename of uploaded file is safe to use in your system
# Werkzeug is a comprehensive and flexible utility library for 
# building web applications in Python. It is a WSGI (Web Server 
# Gateway Interface) utility library that provides various tools 
# and functionalities to help developers handle HTTP requests, 
# responses, and manage the internals of web applications.
import os

app = Flask(__name__)

# Configure the upload folder and allowed file extensions
app.config['UPLOAD_FOLDER'] = 'uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_form():
    if request.method == 'POST':
        f = request.files['file']
        if f and allowed_file(f.filename):
            if not os.path.exists(app.config['UPLOAD_FOLDER']):
                os.makedirs(app.config['UPLOAD_FOLDER'])
            
            filename = secure_filename(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'File uploaded successfully'
        else:
            return 'File not allowed'
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
