from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Welcome to home screen."

@app.route('/about')
def about():
    return "Welcome to about screen."

if(__name__=="__main__"):
    app.run(debug=True)