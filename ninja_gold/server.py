from flask import Flask, render_template, redirect, request,session
import random
app=Flask(__name__)
app.secret_key="very secret"
gold = 0

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/process_money', methods=['POST'])
def process_money():
    session['building'] = request.form['building']
    if session['building'] == 'farm':
        add_gold(10,21,"farm")
    elif session['building'] == 'cave':
        add_gold(5,11,'cave')
    elif session['building'] == 'house':
        add_gold(2,6,'house')
    elif session['building'] == 'casino':
        add_gold(-50,51,'casino')   
    return redirect('/')
def add_gold(x,y,place):
    random_number = random.randrange(x,y)
    win = "Earned {}".format(random_number)+" golds from the "+ place
    loss = "Entered a "+place+" and lose {}".format(random_number)
    msg = win if random_number >= 0 else loss

    global gold 
    gold += random_number
    session['gold'] = gold
    
    if(len(session['activities']) == 0):
        session['activities'] = []
    session['activities'].append(msg)
app.run(debug=True)