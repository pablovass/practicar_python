'''
Problema del trigo y el tablero de ajedrez:

Si se colocase sobre un tablero de ajedrez, un grano de trigo en el primer casillero, dos en el segundo, cuatro en el tercero y asi sucesivamente, doblando la cantidad de
granos en cada casilla ¿Cuantos granos de trigo habria en el tablero al final? 

Resolver el problema con una función recursiva.

Nota: Pueden pensar la solucion en dos funciones, primero una que calcule la cantidad de granos de trigo en un casillero determinado y luego otra con el total.
'''

def doble(numero:int )->int:
    return numero *2

def tablero(posicion:int)->int:
    return 1 if posicion == 1 else doble(tablero(posicion-1))

if __name__ == '__main__':
    print(f'Semillas en el tablero: {tablero(64)}')