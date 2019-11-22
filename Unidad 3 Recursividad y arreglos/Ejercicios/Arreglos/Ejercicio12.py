'''
Desarrollar una función para que, dada una matriz cuadrada de enteros de orden N,
obtenga la traza de la misma (sumatoria de los elementos de la diagonal principal). Lo
mismo pero con la diagonal secundaria. Ambas funciones debes ser recursivas
'''

import numpy as np

def sumaDiagonalPrincipal(matriz, posicion=0):
    orden = matriz.shape[0] - 1
    return matriz[posicion][posicion] if posicion == orden else matriz[posicion][posicion] + sumaDiagonalPrincipal(matriz, posicion+1)

def sumaDiagonalSecundaria(matriz, posicion=0):
    orden = matriz.shape[0] - 1
    return matriz[posicion][orden-posicion] if posicion == orden else matriz[posicion][orden-posicion] + sumaDiagonalSecundaria(matriz, posicion+1)


if __name__ == "__main__":
    matriz = np.arange(16).reshape(4,4)
    print(matriz)
    print(sumaDiagonalPrincipal(matriz))
    print(sumaDiagonalSecundaria(matriz))
