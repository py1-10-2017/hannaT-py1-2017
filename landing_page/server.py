from flask import Flask, render_template  
app = Flask(__name__)                     
                                          
                                          
@app.route('/')                           
@app.route('/ninjas')


def greetings():
  return render_template('index.html')   
def ninjas():
  return render_template('ninjas.html')
@app.route('/dojo/<new>')
def new_dojo(new):
    return render_template('dojos.html')
                                         
                                          
                                          
 
app.run(debug=True)                       
