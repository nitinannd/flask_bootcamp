from flask import Flask
app= Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/home')
def home():
    return "<h1>This is home page of puppies</h1>"

@app.route('/puppies/<name>')
def puppy_name(name):
    return "<h1> This is the homepage of {}".format(name)

if __name__== '__main__':
    app.run(port=5000)