import numpy as np

'''
Crear y cargar dos matrices de tamaño 3x3, sumarlas y mostrar su suma.
A mano y con numpy
'''


# A mano
def suma(matriz_1, matriz_2):
    matriz = []
    for i in range(3):
        matriz.append([0]*3)
    for j in range(3):
        for k in range(3):
            matriz[j][k] = matriz_1[j][k] + matriz_2[j][k]
    return matriz

def mostrar_matriz(matriz):
    for i in range(3):
        print(matriz[i])
# fin A mano
################




if __name__ == "__main__":
    print("A mano")
    matriz_1 =[[1,2,3],[4,5,6],[7,8,9]]
    matriz_2 =[[4,5,6],[7,8,9],[1,2,3]]
    mostrar_matriz(matriz_1)
    print()
    mostrar_matriz(matriz_2)
    print()
    matriz_3 = suma(matriz_1, matriz_2)
    mostrar_matriz(matriz_3)
    print("======================")

    print("Con numpy")
    matriz_a = np.array([[1,2,3],[4,5,6],[7,8,9]])
    matriz_b = np.array([[4,5,6],[7,8,9],[1,2,3]])
    print(matriz_a)
    print()
    print(matriz_b)
    print()
    print(matriz_a + matriz_b)
    print("======================")
