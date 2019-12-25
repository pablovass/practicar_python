'''
Tomar los archivos del webcampus, llamados felix.py y felix.csv y a partir de procesar
la matriz felix, obtener las siguientes imagenes:
[ver pdf]
'''

import numpy as np
import csv
import matplotlib.pyplot as plt

'''
# lo queria hacer a mano pero... meh...

matriz = []

# leer archivo
with open(archivo, newline='') as coso:
    lector = csv.reader(coso)
    # cargar en matriz
    for linea in lector:
        matriz.append(linea)

archivo_b = "D:\\Unahur\\1 año\\Estructura de datos\\practicar_python\\Unidad 3 Recursividad y arreglos\\Ejercicios\\Arreglos\\felixb.csv"

datos = np.asarray(matriz)
np.savetxt(archivo_b,matriz, fmt="%s", delimiter=",")

'''
archivo =  'D:\\Unahur\\1 año\\Estructura de datos\\practicar_python\\Unidad 3 Recursividad y arreglos\\Ejercicios\\Arreglos\\felix.csv'

felix = np.genfromtxt(archivo, delimiter=',')

# A
plt.imshow(felix)
plt.show()
# B
plt.imshow(felix.T)
plt.show()
# C
plt.imshow(np.flip(felix,1))
plt.show()
# D
plt.imshow(np.flip(np.flip(felix),1))
plt.show()
# E
plt.imshow(np.flip(felix))
plt.show()
# F
plt.imshow(felix)
plt.show()
# G
plt.imshow(np.flip(felix.T,1))
plt.show()
# H
plt.imshow(np.flipud(felix.T))
plt.show()