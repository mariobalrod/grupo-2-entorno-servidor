# Entregable 3

Desarrollo Web - Entorno Servidor <br>
Ciclo Superior Desarrollo Web <br>
Curso 2020-21 <br>
Segunda entrega <br>
<br>

#### GRUPO: 2  
<br>

- INTEGRANTE 1:  
    - APELLIDOS, NOMBRE: Ballestero Rodríguez, Mario  
    - DNI: 29533046B  
- INTEGRANTE 2:  
    - APELLIDOS, NOMBRE: Del Junco Pérez, Esperanza  
    - DNI: 49137125V  
- INTEGRANTE 3:  
    - APELLIDOS, NOMBRE: Ávila Chacón, Sergio  
    - DNI: 29498790W

<br>
<br>

## API 

Application Programming Interfaces

Se trata de un conjunto de definiciones y protocolos que se utiliza para desarrollar e integrar el software de las aplicaciones, permitiendo la comunicación entre dos aplicaciones de software a través de un conjunto de reglas (entre un entorno cliente y un entorno servidor).

Podemos hablar de una API como una especificación formal que establece cómo un módulo de un software se comunica o interactúa con otro para cumplir una o muchas funciones.



![img](https://lh4.googleusercontent.com/QK-y7aa-s6E_-hkvhdm6_dQf2FFJGukAvUlh8q8cru-ajEm-BwpKOWFxwxlusYdGD24qBWAPS7Lxgeij_DUJzE8ny8l3zX80wdXaffLERkIr2ZTI8Wwfze02_yvEg6HJMuGUpFdUstc)

<br>
<br>

## POSTMAN

Postman es una herramienta para crear peticiones sobre APIs de una forma sencilla y de esta forma poder testear la APIs. Características de Postman, permite:

Crear peticiones.

º Definir colecciones.

º Gestionar la documentación.

º Crear entorno colaborativo.

º Generar código de invocación.

º Establecer variables.

º Soporta el ciclo de vida API management.

º Crear mockups.


<br>

![img](https://lh6.googleusercontent.com/UIx_dI5AJ62wCzRIXDGWlQe5JyiThcgV90Io_ZwdGljcxwY9J9zHu6RQAAAcQv4I4I1jIwBj5q33deZzw-ASHwRgtfGtKR9g9bAUBWNUgKeSHoetf4RZh6mE9pzVPjcntTaCxss6VOM)


<br>

## Métodos:

**GET:** Es realizar una petición a la API para obtener los datos de la URI proporcionada.

**POST:** Es el método que nos permite crear los diferentes tipos de datos un, ejemplo sería utilizar el método 		    register, este recogerá los datos deseados y los enviará a la API para que esta le diese las 					      			funcionalidades correspondientes.

**PUT:**  Nos permite modificar los datos solicitados mediante el endpoint de la URI.

**DELETE:** Nos permite borrar algún dato específico, para seleccionarlo se indica en el endpoint de la URI mediante los queryparams.



### Colección de Postman con las peticiones de ejemplo

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/2e48b33fde1386c6406d)

<br>

![img](https://lh4.googleusercontent.com/3tHoqR_Ch4jGcdc4e5mzfSKKsU7-lksJd9oeMhDppTVLIlGbZKmBMxJJ8vkwWHCszf6zSiqaygHmkhnoNfU3AlJvL51wDjzLIniCZCR6Etf2SgTvryGsFi2tATf1OOdaCb_L-MZ2IXI)


<br>
<br>

## ¿Qué es Socket.IO ?

Comenzamos aclarando que Socket.IO es una librería desarrollada en JavaScript creada sobre Websocket y otras tecnologías. 

De hecho Socket.IO utiliza WebSocket cuando lo necesita además de respaldarse en otras tecnologías como AJAX Long Polling, AJAX Multipart Stream y muchas mas. Esto permite que web Socket.IO se utilice en otras ocasiones en las que no se admiten WebSockets.

<br>

## ¿Qué es WebSockets?

WebSockets es un protocolo de comunicación web que apareció por primera vez en 2010 en Google Chrome 4. 

Este canal de comunicación web proporciona un canal de comunicación full-duplex (canal de comunicación que permite el envió y recepción simultáneos), a través de una sola conexión TCP.

En otras palabras nos permite una interacción entre servidor y cliente con un esfuerzo mínimo, esto permite la creación de aplicaciones que se aprovechen de las ventajas de la comunicación en tiempo real.


<br>

<br>

## Porque hemos decidido usar Socket.IO

Hemos decidido utilizar Socket.IO porque nos permite transmitir mensajes a todos los clientes que están conectados de forma simultanea (una característica muy a tener en cuenta), además Socket.IO admite los proxies y balanceadores de carga ya listos para su utilización, además como explicamos en su definición Socket.IO permite su utilización en muchas ocasiones en las que WebSocket no podría utilizarse ya que cuenta con varias tecnologías a las que puede recurrir para solucionar este problema que WebSocket no puede solucionar, otra razón mas es que si por cualquier motivo se produce una desconexión, Socket.IO se vuelve a conectar de forma automática cosa que WebSocket no hace.

Todos estos motivos y razones hacen que nos hayamos decantado por Socket.IO, aun así para saber sus diferencias mas en detalle puede continuar con nuestro apartado "Diferencias entre Socket.IO y WebSocket".

<br>


#  Socket.io frente a WebScoket



![WebSocket frente a Socket.io](https://cdn.educba.com/academy/wp-content/uploads/2018/11/WebSocket-vs-Socket.io_-2.png)


<br>


## Diferencia entre Socket.IO y WebSocket

Tanto WebSocket como Socketio son opciones populares en el mercado, discutamos algunas de las principales diferencias entre WebSocket y Socketio:


| **WebSocket**                                                | **Socketio**                                                |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| Es el protocolo que se establece sobre la conexión TCP.      | Es la biblioteca para trabajar con WebSocket.                |
| Proporciona comunicación full duplex en conexiones TCP.      | Proporciona la comunicación basada en eventos entre el navegador y el servidor. |
| El proxy y el equilibrador de carga no son compatibles con WebSocket. | Se puede establecer una conexión en presencia de proxies y balanceadores de carga. |
| No es compatible con la transmisión.                         | Es compatible con la transmisión.                            |
| No tiene una opción de respaldo.                             | Admite opciones de respaldo.                                 |

<br>

En conclusión hemos optado por Socket.io principalmente por estas diferencias:

- Websocket proporciona la conexión sobre TCP, mientras que Socket.io es una biblioteca para abstraer las conexiones de WebSocket.
- WebSocket no tiene opciones de respaldo, mientras que Socket.io admite respaldo.
- WebSocket es tecnología, mientras que Socket.io es una biblioteca para WebSockets.

<br>
<br>

## Modelado de peticiones en Postman para el tablero de Among Us

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/eb5bdb69536f79a6c182)

