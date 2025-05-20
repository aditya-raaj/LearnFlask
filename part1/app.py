from flask import FLASK

app=FLASK(__name__)

@app.route('/')
def home():
    return "Welcome to home page!"