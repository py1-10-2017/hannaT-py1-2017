from flask import Flask, render_template, session, request, redirect
import random


app=Flask(__name__)
app.secret_key = "secret keys"
random_number = random.randrange(0,101)


@app.route('/')
def index():  
    return render_template('index.html')

@app.route('/reset', methods=['POST'])
def reset():
    global random_number
    random_number = random.randrange(0,101)
    session['random_number'] = random_number
    session['msg']=''
    return redirect('/')

@app.route('/user', methods=['POST'])
def guess_num():
    session['msg'] = ""
    session['random_number'] = random_number
    number = int(request.form['number'])
    print session['msg']
    
    if number == random_number:
        session['msg'] = "win"
    elif number > random_number:
        session['msg'] = "high"
    else:
        session['msg'] = "low"

    return redirect('/')


app.run(debug=True)