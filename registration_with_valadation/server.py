import re
from flask import Flask, render_template, request, redirect, flash
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key="very secret"

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/user', methods=['POST'])
def user():
    errors = []
    if len(request.form['first_name']) < 1 or (request.form['first_name']).isalpha() == False:
        errors.append("First name cannot be empty and cannot contain any numbers!")
    if len(request.form['last_name']) < 1 or (request.form['last_name']).isalpha() == False:
        errors.append("Last name cannot be empty and cannot contain any numbers!")
    if len(request.form['email']) < 1:
        errors.append("email cannot be empty!")
    if not EMAIL_REGEX.match(request.form['email']):
        errors.append("Invalid Email Address!")
    if len(request.form['password']) < 8:
        errors.append("password should be 8 or more characters!")
    if request.form['password'] != request.form['conf_pass']:
        errors.append("Password must match!")
    if len(errors) == 0:
        errors.append("Thanks for submitting your information")
    
    for i in range(0,len(errors)):
        flash(errors[i])
    return redirect('/') 
  

app.run(debug=True) 