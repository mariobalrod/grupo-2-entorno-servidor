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

import random

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

    # generar y añadir las cartas de los numeros (2 de cada tipo y color menos el 0 que es solo 1)
    for color in COLORS:
        for i in range(0, 10):
            if i != 0:
                all_cards.append(Card(i, color, False))
                all_cards.append(Card(i, color, False))
            else:
                all_cards.append(Card(i, color, False))

    # generar y añadir las cartas de las especiales (2 de cada tipo y color)
    for color in COLORS:
        for especial in ESPECIALES:
                all_cards.append(Card(especial, color, False))
                all_cards.append(Card(especial, color, False))

    # generar y añadir las cartas de los comodines
    for joker in JOKERS:
        all_cards.append(Card(joker, None, True))
        all_cards.append(Card(joker, None, True))
        all_cards.append(Card(joker, None, True))
        all_cards.append(Card(joker, None, True))
    
    return all_cards


# funcion que baraja las cartas de la baraja
def barajarCards(all_cards):
    random.shuffle(all_cards)
    return all_cards


# funcion que reparte 7 cartas a cada jugador y las elimina de la baraja
def repartirCards(all_cards, jugador, ia):
    for i in range(0, 7):
        jugador.append(all_cards[i])
        all_cards.pop(i)

    for i in range(0, 7):
        ia.append(all_cards[i])
        all_cards.pop(i)


# funcion genera carta inicial y la quita de la baraja
def set_initial_card(all_cards, table):
    initial_card = random.choice(all_cards)

    while initial_card.joker == True or initial_card.value in ESPECIALES:
        initial_card = random.choice(all_cards)    

    table.append(initial_card)
    all_cards.remove(initial_card)


# TESTING
def testing(all_cards):
    for card in all_cards:
        print(card.value, '---', card.color)


def game():
    # Declaramos los jugadores con sus inventarios
    jugador = []
    ia = []

    # Declaramos las cartas en la mesa
    table = []

    print('Bienvenidos al Juego del UNO!')

    # 1. Generamos la Baraja de Cartas
    all_cards = generateCards()
    
    # 2. Barajamos todas las Cartas
    all_cards = barajarCards(all_cards)

    # 3. Repartimos
    repartirCards(all_cards, jugador, ia)

    # 4. Levantamas Carta inicial
    set_initial_card(all_cards, table)

    testing(table)
    print(len(all_cards))

game()