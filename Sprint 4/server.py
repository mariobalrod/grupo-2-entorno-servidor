from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS

from controllers.players import *

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

@socketio.on_error()
def error_handler(e):
    print(e)

#               Eventos Sockets
#==================================================

#Lo primero es restringit que los eventos solo aparezcan si estas conectado
#para ello los creamos dentro de la funcion on_connect()
@socketio.on('connect')
def on_connect():
    print('Someone has been connected')
    controllers = Controllers()

    #E. Unirse jugador
    @socketio.on('join')
    def on_join(name, id):
        controllers.join(name, id)

    #E. Para que comience el juego cuando este todos los jugadores listos
    @socketio.on('start')
    def on_start():
       controllers. start()

    #E. Votar
    @socketio.on('vote')
    def on_vote(id):
        controllers.vote(id)

    #E. Fin del juego 
    @socketio.on('end')
    def on_end():
        controllers.end_game()

    #E. Reseteo de los colores
    @socketio.on('clear')
    def on_clear():
        controllers.clear()

    #E. desconexion del servidor
    @socketio.on('disconnect')
    def on_disconnect():
        print('User has been disconnected')


# Método principal main (Inicializando servidor)
if __name__ == '__main__':
    socketio.run(app)