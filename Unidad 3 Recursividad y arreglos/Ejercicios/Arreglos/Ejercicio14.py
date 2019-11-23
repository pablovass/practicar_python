'''
Desarrollar una función que determine si una matriz cuadrada de enteros de orden N
es simétrica.
'''
import numpy as np

def esSimetrica(matriz):
    orden = matriz.shape[0]
    # for i in range(orden):
    #     for j in range(orden):
    #         if matriz[i][j]!=matriz[j][i]:
    #             return False
    # return True


    i=1
    while i<orden:
        for j in range(i,orden):
            if matriz[i][j]!=matriz[j][i]:
                return False
        i+=1
    return True


if __name__ == "__main__":
    matrizSimetrica = np.array([[1,2,3],[2,1,4],[3,4,1]])
    matrizNoSimetrica = np.array([[1,2,3],[1,2,3],[3,4,1]])
    print(esSimetrica(matrizSimetrica))
    print(esSimetrica(matrizNoSimetrica))