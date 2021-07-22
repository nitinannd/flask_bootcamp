from flask import Flask
from flask import Request
app= Flask(__name__)

@app.route('/')
def home():
    return "<h1> This is home for flask API </h1>"

@app.route('/puppies')
def puppy():
    return "<h2> This is the homepage of cute puppies </h2>"

@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    pupname = ''
    if name[-1]== 'y':
        pupname = name[:-1] + 'iful'
    else:
        pupname = name + 'y'
    
    return " <h1> Your latin puppy name is: {} ".format(pupname)

if __name__== '__main__':
    app.run(port=5000)