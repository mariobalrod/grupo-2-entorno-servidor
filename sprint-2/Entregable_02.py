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

# Constantes que necesitamos para el juego
COLORS = ["red", "green", "yellow", "blue"]
ESPECIALES = ["reverse", "skip", "draw2"]
JOKERS = ["wild", "wild4"]

# Card Class (Esquelo y funcionalidades)
class Card:
    def __init__(self, value, color, joker):
        self.value = value
        self.color = color
        self.joker = joker  

    def reverse():
        print("reverse")

    def skip():
        print("skip")

    def draw2():
        print("draw2")

    def wild():
        print("wild")

    def wild4():
        print("wild4")

# Funcion que genera toda la baraja de cartas
def generateCards():
    all_cards = []

    for color in COLORS:
        for i in range(0, 10):
            if i != 0:
                all_cards.append(Card(i, color, False))
                all_cards.append(Card(i, color, False))
            else:
                all_cards.append(Card(i, color, False))

    for color in COLORS:
        for especial in ESPECIALES:
                all_cards.append(Card(especial, color, False))
                all_cards.append(Card(especial, color, False))

    for joker in JOKERS:
        all_cards.append(Card(joker, None, True))
        all_cards.append(Card(joker, None, True))
        all_cards.append(Card(joker, None, True))
        all_cards.append(Card(joker, None, True))
    
    return all_cards


def game():
    # Declaramos los jugadores con sus inventarios
    jugador = []
    ia = []

    print('Bienvenidos al Juego del UNO!')

    # 1. Generamos la Baraja de Cartas
    all_cards = generateCards()
    
    # 2. Barajamos todas las Cartas

    # 3. Repartimos

game()