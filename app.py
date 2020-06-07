from flask import Flask, request, Response, render_template, redirect
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
import RecoverPlaysTVClips

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "row the boat"
csrf.init_app(app)

@app.route('/')
def main():
    return redirect("/index")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/proxy/download/<username>')
def proxydownload(username):
    RecoverPlaysTVClips.create_zip(username)
    print("completed zip")
    d = {}
    d[0] =  ["Hello lol"]
    return d




