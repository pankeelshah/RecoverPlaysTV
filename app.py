from flask import Flask, request, Response, render_template, redirect
from flask_wtf.csrf import CSRFProtect
import RecoverPlaysTVClips
from flask_socketio import SocketIO, emit
import json

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "row the boat"
csrf.init_app(app)

socketio = SocketIO(app)

clients = []

@app.route('/')
def main():
    return redirect("/index")

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/proxy/download/<username>/<sid>')
def proxydownload(username, sid):
    print(sid)
    RecoverPlaysTVClips.create_zip(username, sid)
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
    clients.append(request.sid)
    print(clients)

@socketio.on('message')
def handle_message(message, sid):
    socketio.emit('message', message, room=sid)

@socketio.on('disconnect')
def handle_disconnect():
    clients.remove(request.sid)

@socketio.on('createzip')
def handle_zip(data):
    # data = json.loads(data)
    print("Printing data and id: " + data["user"] + " " + data["sid"])
    # print(id)
    # print(data[0] + " " + data[1])
    RecoverPlaysTVClips.create_zip(data["user"], data["sid"])
    socketio.emit('created-zip', data["user"], room=data["sid"])
    RecoverPlaysTVClips.delete_zip(data["user"]);
    


if __name__ == "__main__":
    app.run()

