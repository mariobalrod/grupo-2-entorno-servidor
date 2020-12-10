from flask import Flask
from flask_socketio import SocketIO
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

@app.route('/')
def index():
    return 'Hola soy el servidor'

# Método principal main (Inicializando servidor)
if __name__ == '__main__':
    socketio.run(app)