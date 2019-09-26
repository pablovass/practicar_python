#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

###Lectura del archivo en la matriz#####
felix = np.genfromtxt('felix.csv', delimiter=',')
########################################

######Para mostrar matriz como imagen###########
plt.imshow(felix)
plt.show()
########################################


######Completar procesamiento en matriz felix para obtener imagenes################
