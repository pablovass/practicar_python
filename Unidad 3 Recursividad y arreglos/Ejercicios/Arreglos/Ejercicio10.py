'''
Crear una matriz de tamaño 5x5 y rellenarla de la siguiente forma: la posición M[n,m]
debe contener n+m. Después se debe mostrar su contenido.
'''

import numpy as np

# A mano
def rellenar(matriz, n, m):
    matriz[n-1][m-1]=n+m
    return matriz


if __name__ == '__main__':
    matriz = np.zeros((5,5), int)
    posicion_a=3
    posicion_b=2
    print("A mano")

    print(rellenar(matriz, posicion_a, posicion_b))
    print("===============")
    print("Con numpy")
    posicion_c=4
    posicion_d=2
    np.add.at(matriz, (posicion_c,posicion_d), posicion_c+posicion_d)
    print(matriz)