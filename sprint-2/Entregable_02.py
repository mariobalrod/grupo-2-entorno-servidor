# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Segunda entrega
# ===========================================================

# GRUPO:
# INTEGRANTE 1:
#   APELLIDOS, NOMBRE: Ballestero Rodriguez, Mario
#   DNI: 29533046B
# INTEGRANTE 2:
#   APELLIDOS, NOMBRE: Del Junco Pérez, Esperanza
#   DNI: 49137125V
# INTEGRANTE 3:
#   APELLIDOS, NOMBRE: Ávila Chacón, Sergio
#   DNI: 29498790W

# ===========================================================
# Juego del UNO en Python

class Card:
    def __init__(self, value, color, function, joker):
        self.value = value
        self.color = color
        self.function = function
        self.joker = joker  


def game():
    print('Bienvenidos al Juego del UNO!')


game()