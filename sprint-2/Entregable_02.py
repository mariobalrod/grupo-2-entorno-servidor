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
import threading
# Constantes que necesitamos para el juego
COLORS = ["red", "green", "yellow", "blue"]
ESPECIALES = ["reverse", "skip", "draw2"]
JOKERS = ["wild", "wild4"]


# Constantes para elegir position
JUGADOR = 0
IA = 1


# Color actual para cuando se juega un comodin
current_color = []

# Funcion Victoria:
def is_victory(jugador, ia):
    if len(ia) == 0:
        return 'ia'

    if len(jugador) == 0:
        return 'jugador'

    return ''
   

#Decir Uno (Temporizacion)
def say_uno(len_mano):
    if len_mano == 1:
        print('Escribe Uno rapidamente: ')
        uno_escrito = input()
        cuenta_atras = threading.Timer(10.0,draw2())
        cuenta_atras.start()
        if uno_escrito == 'uno':
            cuenta_atras.cancel()
        else: 
            print('Te comes 2 cartas, no estuviste rápido!')

    
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

    print('cambia el turno', current_player)


# Funcionalidad para la carta Robar 2
def draw2(all_cards, baraja):
    for i in range(0, 2):
        baraja.append(all_cards[i])
        all_cards.pop(i)


# Funcionalidad para la carta Comodin
def wild(baraja, choice_card):
    for option in baraja:
        if option.color == current_color[len(current_color)-1] and option.value not in ESPECIALES:
            choice_card = option
            return choice_card

    for option in baraja:
        if option.color == current_color[len(current_color)-1]:
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
        print('===============================')
        print('CARTA EN JUEGO: ', card.value, ':', card.color)
        print('===============================')
        print()

    else:
        print('Estas son tus cartas: ')

        for i in range(len(all_cards)):
            print('(', i+1, ') ', all_cards[i].value, ':', all_cards[i].color, ' | ', end="" )
        
        print('** Teclee 0 para robar una carta **')

        print(' ')

# Filtro para ver si puede jugar una carta 
def filter(who, all_cards, current_card, mano, choice_card):
    # Opcion cambio de color ==> estudiamos opciones color y llamamos a wild()
    if current_card.value == 'wild':
        #------------ RED ------------------
        if current_color[len(current_color)-1] == 'red':
            choice_card = wild(mano, choice_card)

            if choice_card == '' and who == 'ia':
                for i in range(0, 1):
                    mano.append(all_cards[i])
                    all_cards.pop(i)

                choice_card = wild(mano, choice_card)

        #------------ GREEN ------------------
        if current_color[len(current_color)-1] == 'green':
            choice_card = wild( mano, choice_card)

            if choice_card == '' and who == 'ia':
                for i in range(0, 1):
                    mano.append(all_cards[i])
                    all_cards.pop(i)

                choice_card = wild(mano, choice_card)

        #------------ BLUE ------------------
        if current_color[len(current_color)-1] == 'blue':
            choice_card = wild(mano, choice_card)

            if choice_card == '' and who == 'ia':
                for i in range(0, 1):
                    mano.append(all_cards[i])
                    all_cards.pop(i)

                choice_card = wild(mano, choice_card)

        #------------ YELLOW ------------------
        if current_color[len(current_color)-1] == 'yellow':
            choice_card = wild(mano, choice_card)

            if choice_card == '' and who == 'ia':
                for i in range(0, 1):
                    mano.append(all_cards[i])
                    all_cards.pop(i)

                choice_card = wild(mano, choice_card)

    # Opcion numero ==> llama a la funcion number
    else:
        final_choice = number(current_card, mano, choice_card)

        # Si de primeras no tiene carta roba una
        if choice_card == '' and who == 'ia':
            for i in range(0, 1):
                mano.append(all_cards[i])
                all_cards.pop(i)
            
            final_choice = number(current_card, mano, choice_card)
    
    return choice_card


# Funcion del turno del jugador
def turno_jugador(jugador, table, all_cards, ia):
    # Carta que esta en juego
    card = table[len(table)-1]
    
    # Declarando la carta a escoger
    choice_card = ''

    # Mostrar mano de cartas al jugador
    show_cards(jugador, False)
    print()
    print(f'Elije una opcion (1-{len(jugador)}):')
        
    # Introducir la carta escogida
    eleccion = input()
    eleccion = int(eleccion) - 1
        
    # Controla una eleccion valida
    while eleccion not in range(-1, len(jugador)):
        print('validacion numero eleccion')
        print('OPCION NO VALIDA')

        show_cards(jugador, False)
        print()
        print(f'Elije una opcion (1-{len(jugador)}):')

        eleccion = input()
        eleccion = int(eleccion) - 1

        if eleccion != -1:
            choice_card = jugador[eleccion]

            # Controlamos que no se hagan trampas y que sea una carta que se pueda jugar contra la que habia en la mesa
            while (choice_card.value != card.value) and (choice_card.color != card.color) and (choice_card.value not in JOKERS):
                print("validacion carta")
                print('OPCION NO VALIDA')

                show_cards(jugador, False)

                print()
                print(f'Elije una opcion (1-{len(jugador)}):')

                eleccion = input()

                # Controlamos el mismo error de antes para evitar crashear la app
                while (int(eleccion) - 1) not in range(-1, len(jugador)):
                    print('validacion numero eleccion 2')
                    print('OPCION NO VALIDA')
                    show_cards(jugador, False)

                    print()
                    print(f'Elije una opcion (1-{len(jugador)}):')

                    eleccion = input()
                    eleccion = eleccion - 1

    # Una vez filtrada la eleccion valida vemos si debe robar o no
    # Robar carta si la eleccion es -1
    if eleccion == -1:
        for i in range(0, 1):
            jugador.append(all_cards[i])
            all_cards.pop(i)

        choice_card = filter('jugador', all_cards, card, jugador, choice_card)
    else:
        choice_card = jugador[eleccion]
    
    if choice_card == '':
        print('La carta robada no te sirve :( ')
    else:
        # Estudiamos la carta elegida para jugar y dependiendo de la que sea se realiza una accion u otra
        if choice_card.joker:
            print()
            print('Elije un color (red | green | yellow | blue): ')
            color_elegido = input()
                
            # Controlar color valido
            while color_elegido not in COLORS:
                print()
                print('COLOR NO VALIDO')
                print('Elije un color (red | green | yellow | blue): ')
                color_elegido = input()

            current_color.append(color_elegido)
            print('COLOR ELEGIDO: ', current_color[len(current_color)-1])

        if choice_card.value == 'wild4':
            wild4(all_cards, ia)
            
            # Añadir carta a la mesa
            table.append(choice_card)
            jugador.pop(eleccion)

            show_cards(table, True)
            return True
        
        if choice_card.value == 'draw2':
            draw2(all_cards, ia)
            
            # Añadir carta a la mesa
            table.append(choice_card)
            jugador.pop(eleccion)

            show_cards(table, True)
            return True
        
        if choice_card.value == 'reverse':
            
            # Añadir carta a la mesa
            table.append(choice_card)
            jugador.pop(eleccion)

            show_cards(table, True)
            return True
        
        if choice_card.value == 'skip':
            
            # Añadir carta a la mesa
            table.append(choice_card)
            jugador.pop(eleccion)

            show_cards(table, True)
            return True
            
        # Añadir carta a la mesa
        table.append(choice_card)
        jugador.pop(eleccion)

        show_cards(table, True)
        return False
    
#=============================================================================

# Funcion del turno de la maquina (inteligencia artificial lógica)
def turno_ia(ia, table, all_cards, jugador):
    print('ENTRAAAAAAAAAAAAAAAAA')
    # Carta que esta en juego
    card = table[len(table)-1]
    # Declarando la carta a escoger
    choice_card = ''

    # Filtramos las cartas mediante la función filter 
    choice_card = filter('ia', all_cards, card, ia, choice_card)

    # Estudiamos la carta elegida 
    # 1. Si no hay carta posible despues de haber robado cambia turno
    # 2. Hay carta
    #   2.1. Es joker => elegimos color y despues añadimos a tabla
    #   2.2. No es joker => añadimos a la tabla
    if choice_card == '':
        print()
    else:
        # Estudiamos la carta elegida para jugar y dependiendo de la que sea se realiza una accion u otra
        if choice_card.joker == True:
            current_color.append(random.choice(COLORS))
            print('CURRENT COLOR: ', current_color[len(current_color)-1])

        if choice_card.value == 'wild4':
            wild4(all_cards, jugador)

            # Añadimos carta a la tabla
            table.append(choice_card)
            ia.pop(eleccion)

            show_cards(table, True)
            return True            

        if choice_card.value == 'draw2':
            draw2(all_cards, jugador)
            
            # Añadimos carta a la tabla
            table.append(choice_card)
            ia.pop(eleccion)

            show_cards(table, True)
            return True

        if choice_card.value == 'reverse':
            # Añadimos carta a la tabla
            table.append(choice_card)
            ia.pop(eleccion)

            show_cards(table, True)
            return True

        if choice_card.value == 'skip':
            # Añadimos carta a la tabla
            table.append(choice_card)
            ia.pop(eleccion)

            show_cards(table, True)
            return True

        # Añadimos carta a la tabla
        table.append(choice_card)
        ia.pop(eleccion)

        show_cards(table, True)

        return False


# JUEGO FUNCION PRINCIPAL
def game():
    # Declaramos los jugadores con sus inventarios
    jugador = []
    ia = []

    # Declaramos las cartas en la mesa
    table = []

    ganador = ''

    # Obtenemos de forma aleatoria el jugador que empieza
    current_player = random.randint(JUGADOR, IA)

    # =============================================================================
    print()
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
            print()
            print('--------------------------- TURNO DE LA MAQUINA ------------------------------------------------------------')
            control = turno_ia(ia, table, all_cards, jugador)
            show_cards(table, True)

            if len(ia) == 1:
                print('LA MÁQUINA DIJO UNO')
                
            ganador = is_victory(jugador, ia)

            # Controlamos si la carta que ha jugado le da derecho a jugar de nuevo
            while control == True: 
                control = turno_ia(ia, table, all_cards, jugador)
                show_cards(table, True)

                if len(jugador) == 1:
                    print('LA MÁQUINA DIJO UNO')
                    
                ganador = is_victory(jugador, ia)
            
            if current_player == IA:
                current_player = JUGADOR
            else:
                current_player = IA
            
        else:
            print()
            print('--------------------------- ES TU TURNO --------------------------------------------------------------------')
            control = turno_jugador(jugador, table, all_cards, ia)

            say_uno(len(jugador))
            ganador = is_victory(jugador, ia)
            
            # Controlamos si la carta que ha jugado le da derecho a jugar de nuevo
            while control == True:
                control = turno_jugador(ia, table, all_cards, jugador)

                say_uno(len(jugador))
                ganador = is_victory(jugador, ia)    

            if current_player == IA:
                current_player = JUGADOR
            else:
                current_player = IA
            
        

    # 7. Presentar quien ha ganado
    if ganador == 'ia':
        print(current_player)
        print()
        print('HAS PERDIDO PRINGAO!')
    else:
        print()
        print('HAS GANADO CAMPEÓN!')


game()
