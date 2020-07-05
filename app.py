import RecoverPlaysTVClips
from flask import Flask, request, Response, render_template, redirect, send_file
from flask_wtf.csrf import CSRFProtect
from flask_socketio import SocketIO, emit
import json
import os

csrf = CSRFProtect()
app = Flask(__name__)
app.config["SECRET_KEY"] = "row the boat"
csrf.init_app(app)
socketio = SocketIO(app)
socketio.init_app(app, cors_allowed_origins="*")
clients = []

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/guide")
def guide():
    return render_template("guide.html")

@socketio.on("my event")
def handle_my_custom_event(data):
    clients.append(request.sid)
    print(clients)

@socketio.on("message")
def handle_message(message, sid):
    socketio.emit("message", message, room=sid)

@socketio.on("disconnect")
def handle_disconnect():
    RecoverPlaysTVClips.delete_videos(request.sid)
    clients.remove(request.sid)

@socketio.on("createzip")
def handle_zip(data):
    RecoverPlaysTVClips.create_zip(data["user"], data["sid"])
    socketio.emit("created-zip", data["user"], room=data["sid"])
    
@socketio.on("deletezip")
def handle_deletezip(data):
    RecoverPlaysTVClips.delete_zip(data["user"])
    # pass

if __name__ == "__main__":
    app.run()

