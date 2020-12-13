from flask import Flask
from flask_socketio import SocketIO, emit
from flask_cors import CORS

# Iniciar app flask
app = Flask(__name__)

# Configuracion necesaria para la app flask
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'

# Añadiendo Cors a la app
CORS(app, resources={r"/*": {"origins": "*"}})

# Añadiendo socketio a la app y cors a los socket
socketio = SocketIO(app, cors_allowed_origins='*')

#Ruta Inicial del servidor Flask
@app.route('/')
def index():
    return 'Server running'

#Eventos Sockets

#Evento creacion del jugador
@socketio.on('join')
def handleJoin(player):
    emit("player_joined", player, broadcast = True)


# Método principal main (Inicializando servidor)
if __name__ == '__main__':
    socketio.run(app)