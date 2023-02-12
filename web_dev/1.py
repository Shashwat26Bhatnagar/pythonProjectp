from flask import Flask
app= Flask(__name__)
@app.route("/")
def hello():
    return "Hello world"

@app.route("/harry")
def harry():
    return "Hello harry bro!!"
app.run(debug=True) #by writing debug=True you do not need to relod after each and every chagne you make
