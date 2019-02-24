from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)

app.config['SECRET_KEY'] = 'this_key'
socketio = SocketIO(app)


@app.route('/')
def index():
    return "Hello World!"


if __name__ == '__main__':
    socketio.run(app, debug=True)
