from flask import Flask, request, Response, render_template, redirect
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
import RecoverPlaysTVClips
from flask_socketio import SocketIO, emit

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "row the boat"
csrf.init_app(app)

socketio = SocketIO(app)

@app.route('/')
def main():
    return redirect("/index")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/proxy/download/<username>')
def proxydownload(username):
    RecoverPlaysTVClips.create_zip(username)
    d = {}
    d[0] =  ["Hello lol"]
    return d

@app.route('/proxy/deletezip/<username>')
def proxydeletezip(username):
    RecoverPlaysTVClips.delete_zip(username)
    d = {}
    d[0] =  ["Hello lol"]
    return d

@socketio.on('my event')
def handle_my_custom_event(data):
    print(data)

@socketio.on('message')
def handle_message(message):
    socketio.emit('message', message)


