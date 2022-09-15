import os
from urllib import response

from flask import Flask, jsonify, request,render_template, flash, redirect, url_for,logging,session
from flask_cors import CORS
from sympy import arg
from configuration import db
from config import config_by_name
from flask_restx import Api, Namespace, Resource, fields, reqparse
from werkzeug.datastructures import FileStorage
from functools import wraps
from controllers import TestApplication

def create_app(config_name):
    """Creates the flask app and initialize its component"""
    app = Flask(__name__)

    app.config.from_object(config_by_name[config_name])

    
    db.init_app(app)

    return app


app = create_app('env')
api = Api()
api.init_app(app)


parser = reqparse.RequestParser()
parser.add_argument(
    "filename", type=FileStorage, location="files", required=True
)

@app.route('/home')
def home():
    return render_template('home.html')



# User login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Get Form Fields
        username = request.form['username']
        password_candidate = request.form['password']
        result = TestApplication.check_identity(username,password_candidate)

       

        if result:
                # Passed
                role = TestApplication.get_role(username,password_candidate) 
                session['logged_in'] = True
                if role =='ADMIN':
                    session['is_admin'] = True
                    session['username'] = username
                    flash('You are now logged in', 'success')
                    return redirect(url_for('home'))
                else:
                    session['is_admin'] = False
                    session['username'] = username
                    flash('You are now logged in', 'success')
                    return redirect(url_for('home'))
                
        else:
            error = 'Invalid login'
            return render_template('login.html', error=error)
       
   

    return render_template('login.html')

# Check if user logged in
def is_logged_in(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('Unauthorized, Please login', 'danger')
            return redirect(url_for('login'))
    return wrap

# Logout
@app.route('/logout')
@is_logged_in
def logout():
    session.clear()
    flash('You are now logged out', 'success')
    return redirect(url_for('login'))

@api.route("/get")
class Get_File(Resource):
    def get(self):
        if request.method == 'GET':
            result = TestApplication.get_students()
            return jsonify(result)

@api.route("/upload_file")
class Upload_File(Resource):
    @api.expect(parser)
    def post(self):
        if request.method == "POST":
            args = parser.parse_args()
            temp_file = args.filename
            result = TestApplication.upload_file(temp_file)
            return result



if __name__ == '__main__':
    app.secret_key='secret123'
    port = 5000
    app.run(debug=True, host='0.0.0.0', port=port)