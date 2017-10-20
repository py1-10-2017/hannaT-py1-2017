from flask import Flask, render_template, request, redirect, flash
app = Flask(__name__)
app.secret_key="very secret"

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=['POST'])
def result():
  if len(request.form['name']) < 1:
    flash("Name cannot be empty!")
    return redirect('/')
  elif len(request.form['comment']) > 120:
      flash("comment cannot be longer than 120 Characters")
      return redirect('/') 
  name = request.form['name']
  loc = request.form['loc']
  language = request.form['language']
  comment = request.form['comment']
  return render_template('result.html',name=name,loc=loc,language=language,comment=comment)
app.run(debug=True) # run our server