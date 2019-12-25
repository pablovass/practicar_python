#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

###Lectura del archivo en la matriz#####
felix = np.genfromtxt('D:\\Unahur\\1 año\\Estructura de datos\\practicar_python\\Unidad 3 Recursividad y arreglos\\Ejercicios\\Arreglos\\felix.csv', delimiter=',')
########################################
print(felix)
######Para mostrar matriz como imagen###########
plt.imshow(felix)
plt.show()
########################################


######Completar procesamiento en matriz felix para obtener imagenes################
