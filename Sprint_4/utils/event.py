from flask_socketio import emit

def emitAll(event, data):
    emit(event, data, broadcast = True)

def emitOne(event, data):
    emit(event, data)