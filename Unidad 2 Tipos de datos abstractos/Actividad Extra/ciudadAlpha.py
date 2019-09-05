#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 31 20:50:20 2019

@author: fernandopuricelli
"""
## OJO: este import supone que el Tipo de Datos está guardado en propiedad.py 
## en el mismo directorio
import propiedad

""" ------------------- IMPORTANTE --- no cambiar nada desde acá"""
import matplotlib.pyplot as plt

def enPlanoDeCatastro(calle,altura):
    plt.plot(altura, calle, color='green', marker='o', linestyle='dashed',linewidth=2, markersize=24)

def ciudadAlphaEnPlano():
    plt.ylim(0,5)
    plt.xlim(0,10)
    plt.grid(True)
    plt.show()
"""  -----------------  hasta acá"""

# COMPLETAR (0): crear la función impuestoRenta que recibe una propiedad
# y retorna el impuesto a pagar . siguiendo la siguiente fórmula
# es el 10% del valor de la propiedad 

# ....

# hasta aquí completar (0)

""" ------------------- IMPORTANTE --- no cambiar nada desde acá"""
plt.figure()
"""  -----------------  hasta acá"""

# COMPLETAR (1): crear 3 propiedades

# ....

# Hasta aquí completar (1)

# COMPLETAR (2): construir en el año 1990 134mts en la propiedad 1
#  y construir en el año 2005 180mts en la propiedad 2

# ....

# hasta aquí completar (2)

# COMPLETAR (3): usar la primitiva de catastro (enPlanoDeCatastro) para ubicar en el mapa las
# 3 propiedades

# ....

# hasta aquí completar (3)


""" ------------------- IMPORTANTE --- no cambiar nada desde acá"""
ciudadAlphaEnPlano()
"""  -----------------  hasta acá"""

# COMPLETAR (4): imprimir el tipo, dirección y sentido de circulación de las 3 propiedades

# ....


# hasta aquí completar (4)

# COMPLETAR (5): imprimir la valuación de las 3 propiedades

# ....

# hasta aquí completar (5)

# COMPLETAR (6): partiendo de la calle 1 mostrar hacia qué dirección se debe ir
# para llegar a cada propiedad

# ....

# hasta aquí completar (6)

# COMPLETAR (7): con la función creada en COMPLETAR (0) imprimir los impuestos
# a cobrar a cada una de las propiedades

# ....

# hasta aquí completar (7)





