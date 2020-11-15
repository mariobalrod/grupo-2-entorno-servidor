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


# Constantes para elegir position
JUGADOR = 0
IA = 1


# Obtenemos de forma aleatoria el jugador que empieza
current_player = random.randint(JUGADOR, IA)


# Color actual para cuando se juega un comodin
current_color = ''


# Card Class (Esqueleto)
class Card:
    def __init__(self, value, color, joker):
        self.value = value
        self.color = color
        self.joker = joker


# Funcionalidad para Cambio de turno global
def change_turn(current_player):
    if current_player == IA:
        current_player = JUGADOR
    else:
        current_player = IA


# Funcionalidad para la carta Robar 2
def draw2(all_cards, baraja):
    for i in range(0, 2):
        baraja.append(all_cards[i])
        all_cards.pop(i)


# Funcionalidad para la carta Comodin
def wild(baraja, choice_card):
    for option in baraja:
        if option.color == current_color and option.value not in ESPECIALES:
            choice_card = option
            return choice_card

    for option in baraja:
        if option.color == current_color:
            choice_card = option
            return choice_card

    for option in baraja:
        if option.joker:
            choice_card = option
            return choice_card

    return ''

# Funcionalidad para la carta Comodin +4
def wild4(all_cards, baraja):
    for i in range(0, 4):
        baraja.append(all_cards[i])
        all_cards.pop(i)


# Funcionalidad para la carta Número
def number(card, baraja, choice_card):
    show_cards(baraja, False)
    for item in baraja:
        if item.color == card.color and not item.value in ESPECIALES:
            choice_card = item
            return choice_card

    for item in baraja:
        if item.value == card.value and item.value not in ESPECIALES and not item.joker:
            choice_card = item
            return choice_card

    for item in baraja:
        if item.color == card.color:
            choice_card = item
            return choice_card

    for item in baraja:
        if item.joker:
            choice_card = item
            return choice_card

    return ''


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


# Funcion para mostrar cartas
def show_cards(all_cards, is_table):
    print('')

    if is_table == True:
        card = all_cards[len(all_cards) - 1]
        print('Carta en juego: ', card.value, ':', card.color)

    else:
        print('Estas son tus cartas: ')

        for card in all_cards:
            print(card.value, ':', card.color, ' | ', end="")

        print(' ')


# Funcion del turno del jugador
def turno_jugador(jugador, table, all_cards):
    print("Es tu turno!")

    # Carta que esta en juego
    card = table[len(table)-1]
    # Declarando la carta a escoger
    choice_card = ''
    
    show_cards(jugador)
    print()
    print('Elije una opcion (1-', len(jugador), '): ')

    eleccion = input()

    if eleccion - 1 not in range(0, len(jugador)):
        print('OPCION NO VALIDA')
    else:
        choice_card = jugador[eleccion]

    
    

#=============================================================================


# Funcion del turno de la maquina (inteligencia artificial lógica)
def turno_ia(ia, table, all_cards):
    # Carta que esta en juego
    card = table[len(table)-1]
    # Declarando la carta a escoger
    choice_card = ''

    # ===============================================
    # Empezamos a filtrar la elección de cartas mediante condicionales

    # Opcion chupate 2 ==> llamamos a la función draw2
    if card.value == 'draw2':
        card.draw2(all_cards, ia)

    # Opcion cambio de color ==> estudiamos opciones color y llamamos a wild()
    if card.value == 'wild':

        #------------ RED ------------------
        if current_color == 'red':
            choice_card = wild(ia, choice_card)

            if choice_card == '':
                for i in range(0, 1):
                    ia.append(all_cards[i])
                    all_cards.pop(i)

                choice_card = wild(ia, choice_card)

        #------------ GREEN ------------------
        if current_color == 'green':
            choice_card = wild( ia, choice_card)

            if choice_card == '':
                for i in range(0, 1):
                    ia.append(all_cards[i])
                    all_cards.pop(i)

                choice_card = wild(ia, choice_card)

        #------------ BLUE ------------------
        if current_color == 'blue':
            choice_card = wild(ia, choice_card)

            if choice_card == '':
                for i in range(0, 1):
                    ia.append(all_cards[i])
                    all_cards.pop(i)

                choice_card = wild(ia, choice_card)

        #------------ YELLOW ------------------
        if current_color == 'yellow':
            choice_card = wild(ia, choice_card)

            if choice_card == '':
                for i in range(0, 1):
                    ia.append(all_cards[i])
                    all_cards.pop(i)

                choice_card = wild(ia, choice_card)

    # Opcion chupate 4 ==> llama a la funcion wild4
    if card.value == 'wild4':
        wild4(all_cards, ia)

    # Opcion numero ==> llama a la funcion number
    else:
        choice_card = number(card, ia, choice_card)

        if choice_card == '':
            for i in range(0, 1):
                ia.append(all_cards[i])
                all_cards.pop(i)

            choice_card = number(card, ia, choice_card)


    # Estudiamos la carta elegida 
    # 1. Si no hay carta posible despues de haber robado cambia turno
    # 2. Hay carta
    #   2.1. Es joker => elegimos color y despues añadimos a tabla
    #   2.2. No es joker => añadimos a la tabla
    if choice_card == '':
        change_turn(current_player)
    else:
        if choice_card.joker == True:
            print(random.choice(COLORS))

        table.append(choice_card)
        ia.remove(choice_card)

    show_cards(table, True)


# JUEGO FUNCION PRINCIPAL
def game():
    # Declaramos los jugadores con sus inventarios
    jugador = []
    ia = []

    # Declaramos las cartas en la mesa
    table = []

    ganador = ''

    # =============================================================================
    print('Bienvenidos al Juego del UNO!')

    # 1. Generamos la Baraja de Cartas
    all_cards = generateCards()

    # 2. Barajamos todas las Cartas
    all_cards = barajarCards(all_cards)

    # 3. Repartimos
    repartirCards(all_cards, jugador, ia)

    # 4. Levantamas Carta inicial
    set_initial_card(all_cards, table)

    # 5. Mostrar la primera carta en juego
    show_cards(table, True)

    # 6. Controlamos turnos
    while ganador == '':
        if current_player == IA:
            turno_ia(ia, table, all_cards)
            ganador = 'ia'
        else:
            turno_jugador(jugador, table, all_cards)
            ganador = 'jugador'
        

    # 7. Presentar quien ha ganado
    if ganador == 'ia':
        print()
        print('Has perdido pringao!')
    else:
        print()
        print('Has ganado campeón!')


game()
