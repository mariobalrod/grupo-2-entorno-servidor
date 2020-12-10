from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

@app.route('/')
def index():
    return 'hola soy el servidor'

if __name__ == '__main__':
    app.run(debug=True)