'''
Desarrollar una función que determine si una matriz cuadrada de enteros de orden N
es matriz diagonal (ceros en todos sus elementos excepto en la diagonal principal).
'''

import numpy as np

def esDiagonal(matriz):
    orden = matriz.shape[0]
    i=0
    while i<orden:
        if matriz[i][i] != 0:
            return False
        i+=1
    return True

if __name__ == "__main__":
    matrizVerdadera = np.array([[0,1,2],[1,1,2],[1,2,0]])
    matrizFalsa = np.array([[0,1,2,4],[1,0,2,4],[1,2,0,4],[1,2,4,0]])
    print(esDiagonal(matrizVerdadera))
    print(esDiagonal(matrizFalsa))