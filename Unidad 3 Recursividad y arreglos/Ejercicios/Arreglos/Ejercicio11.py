'''
Desarrollar una función para que, dada una matriz cuadrada de reales de orden N,
obtenga la sumatoria de los elementos que están por encima de la diagonal principal
(excluida ésta).
'''
import numpy as np

def suma(matriz)->int:
    orden = matriz.shape[0] 
    columna = 1
    suma = 0
    for i in range(0,orden):
        suma += sum(matriz[i][columna:orden])
        columna += 1
    return suma


if __name__ == "__main__":
    matriz = np.arange(16).reshape(4,4)
    print(matriz)
    print(f"Resultado de la suma: {suma(matriz)}")
