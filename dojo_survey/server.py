from flask import Flask, render_template, request, redirect
app = Flask(__name__)
@app.route('/')
def index():
  return render_template("index.html")
@app.route('/result', methods=['POST'])
def result():
   name = request.form['name']
   loc = request.form['loc']
   language = request.form['language']
   comment = request.form['comment']
   return render_template('result.html',name=name,loc=loc,language=language,comment=comment)
app.run(debug=True) # run our server