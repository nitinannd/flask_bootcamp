from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def index():
    name= 'nitin'
    list_name= list(name)

    return render_template('basic.html',name=name,list_name=list_name)

if __name__== '__main__':
    app.run(debug= True)