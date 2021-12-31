from flask import Flask
app = Flask(__name__)

@app.route("/yellw")
def hello_world():
    print("hello world\n")
    return "<p>Hello, World!</p>"
