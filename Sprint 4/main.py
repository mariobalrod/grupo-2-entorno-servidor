from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
    return 'hola soy el servidor'

if __name__ == '__main__':
    socketio.run(app, debug=True)