from flask import Flask

app=Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "<h1>Welcome to home page!</h1>"

@app.route('/about')
def about():
    return "<h1>This is the about page</h1>"

@app.route("/addition/<int:num>")
def addition(num):
    return f"Input:{num},Output:{num+10}"

if __name__ =="__main__":
    app.run(debug=True)