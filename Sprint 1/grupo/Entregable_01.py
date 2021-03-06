# ==========================================================
# Desarrollo Web - Entorno Servidor
# Ciclo Superior Desarrollo Web
# Curso 2020-21
# Primera entrega
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

# Escribir el código Python de las funciones que se piden en el
# espacio que se indica en cada ejercicio.

# IMPORTANTE: NO CAMBIAR EL NOMBRE NI A ESTE ARCHIVO NI A LAS FUNCIONES QUE SE
# PIDEN (aquellas funciones con un nombre distinto al que se pide en el
# ejercicio NO se corregirán).

# ESTE ENTREGABLE SUPONEN 3 PUNTOS DE LA NOTA DEL TRIMESTRE PARA TODO EL GRUPO

# *****************************************************************************
# HONESTIDAD ACADÉMICA Y COPIAS: la realización de estos ejercicios es un
# trabajo grupal, por lo que deben completarse por cada grupo de estudiantes.
# La discusión y el intercambio de información de carácter general con los
# compañeros se permite (e incluso se recomienda), pero NO AL NIVEL DE CÓDIGO.
# Igualmente el remitir código de terceros, obtenido a través de la red o
# cualquier otro medio, se considerará plagio.

# Cualquier plagio o compartición de código que se detecte significará
# automáticamente la calificación de CERO EN LA ASIGNATURA para TODOS los
# alumnos involucrados. ¡Aseguraros!
# *****************************************************************************

# -----------------------------------------------------------------------------
# EJERCICIO 1)

# Supongamos que tenemos una cadena de caracteres con una frase, en la que
# pueden aparecer dígitos (entre 0 y 9), que hacen el papel de "comodines" que
# han de ser sustituidos por palabras concretas. Por ejemplo, si tenemos la
# siguiente frase:

# "1 me dijo que 0 vendría con 2"

# podemos pensar que 0, 1 y 2 hacen el papel de símbolos que pueden ser
# sustituidos por palabras concretas. Por ejemplo, sustituyendo 0 por Miguel,
# 1 por Juan y 2 por Pedro, tendríamos la frase:

# "Juan me dijo que Miguel vendría con Pedro"

# Para expresar las sustituciones a realizar, lo haremos mediante una
# secuencia p0:p1:p2:... de palabras separadas por el carácter ":", en la que
# la palabra de la posición i-ésima es la que hay que usar para sustituir al dígito i
#
# Por ejemplo, la sustitución del ejemplo anterior la expresaríamos por
# Miguel:Juan:Pedro
# (es decir, 0 por Miguel, 1 por Juan y 2 por Pedro).

# Supongamos que tenemos listadas en un fichero de texto una serie de
# sustituciones en el formato descrito, una por cada línea del fichero.

# Se pide definir una función sustituye_patrones(frase,fichero) que
# recibiendo como entrada una frase y un fichero en el que están listadas una
# serie de sustituciones (una por línea), escribe por pantalla las frases que
# se obtienen al aplicar cada sustitución del fichero a la frase.

# Por ejemplo, si tenemos un fichero sustituciones.txt con las siguientes
# líneas:

# Miguel:Juan:Pedro
# Luis:Antonio:Maria
# Marcos:Eva
# Ivan:Jesus:Antonio:Luis
# Rafael:Francisco:Jose

# entonces, el comportamiento de la función debe ser el siguiente:

# >>> sustituye_patrones("1 me dijo que 0 vendría con 2","sustituciones.txt")
# Juan me dijo que Miguel vendría con Pedro
# Antonio me dijo que Luis vendría con Maria
# Eva me dijo que Marcos vendría con 2
# Jesus me dijo que Ivan vendría con Antonio
# Francisco me dijo que Rafael vendría con Jose

# >>> sustituye_patrones("Los hijos de 1 son 2 y 0","sustituciones.txt")
# Los hijos de Juan son Pedro y Miguel
# Los hijos de Antonio son Maria y Luis
# Los hijos de Eva son 2 y Marcos
# Los hijos de Jesus son Antonio y Ivan
# Los hijos de Francisco son Jose y Rafael

import re

def sustituye_patrones(frase, fichero):
    archivo = open(fichero, 'r')
    lineas = archivo.readlines()
    numeros = ['0','1','2','3','4','5','6','7','8','9']

#==================================================================================================    
    #Con esto controlamos que no haya un numero en la frase superior a 9
    #Hemos importado "re" y usamos .findall para buscar solo los numeros.
    #.findall --> nos devuelve una lista con los numeros del array
    numeros_frase = re.findall(r'\d+', frase)
    for x in numeros_frase:
        if int(x) > 9:
            print('Los numeros que introduzca en la frase han de ser IGUALES o INFERIORES que 9')
            exit()      
#==================================================================================================
    
    controlador = len(lineas)
    while (controlador != 0):
        numero = 0
        eliminarN = ''
        frase_auxiliar = ''

        for x in range(len(lineas)):
            nombres = lineas[controlador-1].split(':')
        for x in range(len(nombres)):
            numero = numero + 1

#==================================================================================================        
        #Esto esta echo para eliminar "\n" de los ultimos nombres de cada linea del archivo   
        eliminarN = ' '.join(nombres)
        eliminarN = eliminarN.replace('\n',' ').replace('\r','')
        lista_nombres_correcta = eliminarN.split()
#==================================================================================================
    
        for x in range(len(frase)):
            if frase[x] in numeros:
                if int(frase[x]) >= numero:
                    frase_auxiliar = frase_auxiliar + frase[x]
                else:
                    frase_auxiliar = frase_auxiliar + lista_nombres_correcta[int(frase[x])]
            else:
                frase_auxiliar = frase_auxiliar + frase[x]
        
        controlador = controlador - 1
        print(frase_auxiliar)

# Nótese que:
# - Supondremos que en la frase de entrada las palabras se separan mediante un
#   único espacio, y que los únicos números que aparecen son dígitos de 0 a 9.
# - No todas las sustituciones indican sustitución para todos los dígitos que
#   aparezcan en la frase. Por ejemplo, la tercera línea del ejemplo, no
#   indica sustitución para 2, y en ese caso se deja sin sustituir.
# - Asimismo, puede que la sustitución indique sustitución para más dígitos de
#   los que aparece en la frase.

# INDICACIÓN: pueden ser útiles los métodos split y join de la clase string.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# EJERCICIO 2)

# Supongamos que la ETSII ha comprado un nuevo ordenador que vamos a utilizar
# como servidor para las prácticas de la asignatura, y que necesitamos dar de
# alta a los alumnos como usuarios de ese servidor. Para ello, hemos de
# generar automáticamente un nombre de usuario para cada alumno, en base a su
# nombre y apellidos.

# En este ejercicio se pide una función imprime_usuarios(fichero), que
# recibiendo como entrada un fichero con los datos de cada usuario, imprime
# por pantalla un listado de los mismos en orden alfabético de apellidos,
# junto con el nombre de usuario automáticamente generado.

# Por ejemplo, aplicando la función imprime_usuarios al fichero nombres.txt
# que se proporciona, debe de mostrase el siguiente resultado:

# >>> imprime_usuarios("nombres.txt")
#
# DNI      Apellidos                      Nombre          Usuario
# -------- ------------------------------ --------------- --------
# 67834547 Abad Garcia                    Maria Jose      mjabagar
# 87452221 Fernandez Lopera               Maria           mferlop1
# 76865412 Fernandez Lopez                Mario           mferlop
# 36638712 Gomariz Gonzaga                Amador          agomgon1
# 12987534 Gomez Gonzalez                 Alicia          agomgon
# 21783647 Gonzalez Echevarri             Antonia Maria   amgonech
# 87654321 Luna Espejo                    Emilio          elunesp
# 78988851 Mencheta Ruiz                  Javier Liborio  jlmenrui2
# 88734412 Mencheta Ruiz                  Jose Luis       jlmenrui1
# 22426553 Menendez Ruiz                  Juan            jmenrui
# 23823472 Mensaque Ruibarros             Juan Luis       jlmenrui
# 63555789 Muela Garcia                   Lidia           lmuegar
# 73535787 Navas Suarez                   Rocio           rnavsua
# 73163633 Perez Posada                   Manuel Jose     mjperpos
# 73263638 Poza Ramirez                   Isabel          ipozram
# 73276362 Rodicio Martinez               Antonio Manuel  amrodmar1
# 12326523 Rodriguez Marquez              Antonio Manuel  amrodmar
# 34551211 Sanchez Sanchez                Fermin Jose     fjsansan
# 78363677 Sanchez Santaella              Enrique Manuel  emsansan
# 21334456 Torres Chacon                  Eduardo         etorcha


# El fichero de entrada es una secuencia de líneas de la forma:
# DNI:Nombre1:Nombre2:Apellido1:Apellido2
# o bien (si el alumno no tuviera nombre compuesto):
# DNI:Nombre::Apellido1:Apellido2

# Como se muestra en el ejemplo anterior, el nombre de usuario de cada alumno
# se ha de generar mediante la siguiente regla: inicial del primer nombre,
# inicial segundo nombre (si tuviera), las tres primeras letras del primer
# apellido y las tres primeras letras del segundo apellido, todo en
# minúsculas. Si con esta regla hay varios alumnos a los que les corresponde
# el mismo nombre de usuario, se distinguen mediante sucesivos índices
# numéricos que se añaden al final.

# Nótese que si una línea del fichero no tiene el formato indicado, se ha de
# ignorar.

# INDICACIONES:
# - Pueden ser útiles los métodos split y lower de la clase string
# - Al leer cada línea del fichero de entrada, el último carácter será el
#   salto de línea "\n". Si tenemos una cadena l que tiene ese carácter de fin
#   de línea, entonces l[:-1] es la misma línea pero sin ese carácter.
# - Para ordenar las líneas por orden alfabético, puede ser util el método de
#   sort de la clase listas, y usar el parametro "key=...".
# - Las líneas de salida del ejemplo han sido impresas con la siguiente cadena
#   de formateo:  "{0:>8} {1:<30} {2:<15} {3}"
# ----------------------------------------------------------------------------------

# Función para comprobar si la linea del txt es un usuario
def is_user_line(list):
    # Longitud de items es 5 && si el elemento 0 es un dni 
    if len(list) == 5 and len(list[0]) == 8:
        return True

    else:
        return False

# ========================================================================================

# Función para establece el DisplayName del usuario
def set_name(nombre1, nombre2):
    # Comprobar si tiene segundo nombre
    if len(nombre2) > 0:
        return nombre1 + ' ' + nombre2
    
    else: 
        return nombre1

# ========================================================================================

# Función para montar todo los usernames
def set_usernames(users):
    # List en se añadir all usernames
    usernames = []

    # Recorro cada usuario en user
    for user in users:

        nombres = user['nombre'].split(' ')

        apellidos = user['apellidos'].split(' ')

        # Controlamos si tiene un nombre compuesto o simple
        if len(nombres) == 2:
            username = nombres[0][0]+nombres[1][0]+apellidos[0][0:3]+apellidos[1][0:3]
        
        else: 
            username = nombres[0][0]+apellidos[0][0:3]+apellidos[1][0:3]

        # Con esto vemos si el username ya existe si es asi lo tratamos para ponerle un numero superior hasta que sea un username unico
        while username.lower() in usernames:
            # Usamos regex para obtener el numero de los usernames que se repites
            numbers = re.findall(r'[0-9]+', username)

            # Asignamos el numero que pertenece a ese username
            if len(numbers) > 0:
                new_number_name = int(numbers[len(numbers)-1]) + 1

                username = username.replace(numbers[len(numbers)-1], str(new_number_name))
                
            else:
                username = username+str(1)

        # Añadimos el username creado a la lista de usernames
        usernames.append(username.lower())

        # Asignamos el valor obtenido al objeto user tratado
        user['usuario'] = username.lower()

# ========================================================================================

# Función principal que se encarga de usar las demás funcionalidades para montar la tabla de users
def imprime_usuarios(file):

    users = []

    # Recoge una lista de filas
    f = open(file, 'r')

    for line in f:
        items = line.split(':')

        # Si la fila coincide con el esquema de user, crea un objeto user que añade a la lista de users
        if is_user_line(items):
            new_user = {
                'dni': items[0],
                'apellidos': items[3] + ' ' + items[4].replace('\n', ''),
                'nombre': set_name(items[1], items[2]),
                'usuario': ''
            }

            users.append(new_user)

    # Paso todos los usuarios a la funcion set_usernames para montar el username
    set_usernames(users)

    # Presento la tabla final con los usuarios siguiendo el esquema de espaciado en el for para cada usuario
    print('DNI      Apellidos                      Nombre          Usuario')
    print('-------- ------------------------------ --------------- --------')

    for user in users:
        print(f"{user['dni']:>8} {user['apellidos']:<30} {user['nombre']:<15} {user['usuario']}")

    f.close()

# -----------------------------------------------------------------------------
# EJERCICIO 3) EL DECODIFICADOR

# Se tiene que realizar un juego con las siguientes instrucciones:

# 1. El programa decidirá 3 dígitos no repetidos. Ej: 123
# 2. El jugador deberá indicar 3 dígitos mediante la consola.
# 3. El programa nos devolverá una pista de las siguientes:
#
#     ¡Casi!: El jugador acertó los tres números, pero en el orden incorrecto.
#     Cerca: El jugador acertó un número en la posición correcta.
#     Nada: El jugador no acertó el resto de casos.
#
# 4. Basándonos en estas pruebas, el jugador tendrá que conseguir hacer que
#    coincidan los 3 dígitos en la misma posición, el programa responderá y
#    terminará con:
#                    ¡Enhorabuena, ahora eres un hacker!

# Por ejemplo, si intentamos jugar con la máquina y esta tiene almacenado el
# número 479, esto sería un ejemplo de una partida:

# >>> juego_decodificador()
# ¡Bienvenido al decodificador!
# ¿Cuál es tú apuesta?: 459
# Cerca, ¡sigue así!
# ¿Cuál es tú apuesta? 345
# Nada, inténtalo de nuevo.
# ¿Cuál es tú apuesta? 947
# ¡Casi!, reordénalos.
# ¿Cuál es tú apuesta? 479
# ¡Enhorabuena, ahora eres un hacker!
# >>>

# Es importante que el programa termine en esa sentencia.

# Notas:
# Hay que tener en cuenta la división de las tareas para completar este tiempo
# de tareas que podrían tener una complejidad elevada. ¡Divide y vencerás!
#
# Hay algunas instrucciones que pueden ser de utilidad para desarrollar este
# sencillo juego:

import random

def juego_decodificador():

    print("¡Bienvenido al decodificador!")

#==============================================================================================

    # Aquí creamos tres números aleatorios asegurándonos en el while de que no se repita ninguno.
    x = []
    while len(x) < 3:
       num = random.choice(range(1, 10))
       if num in x:
          num
       else:
          x.append(num)
    # A continuacuión unimos los tres números generados en un solo string para crear el número aleatorio que se usará en el juego.
    x = "".join([str(_) for _ in x])

    control = False

#===============================================================================================

    # Comprobamos mediante condicionales las coincidencias entre el número generado y el número que el jugador introduce.
    while control==False:
    
       guess = input("¿Cuál es tú apuesta?: ")
       array = list(guess)
    
       if x[0:3] == guess[0:3]:
       
          control = True
    
       elif x[0] in array and x[1] in array and x[2] in array:
       
          print('¡Casi!, reordénalos.')
    
       elif x[0] == guess[0] or x[1] == guess[1] or x[2] == guess[2]:
       
          print('Cerca, ¡sigue así!')
    
       else :
       
          print('Nada, inténtalo de nuevo.')

    print('¡Enhorabuena, ahora eres un hacker!')


