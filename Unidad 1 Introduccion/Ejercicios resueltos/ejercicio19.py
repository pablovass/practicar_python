#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:50:12 2019

@author: fernandopuricelli
"""

""" Esta implementación de Factorial es una forma de resolverlo
No es la mejor...más adelante en la materia vamos a ver otra
"""

def serieFactorial(numero):
    cuenta=numero
    for i in range(numero-1,1,-1):
        cuenta=cuenta*i
    return(cuenta)

def factorial(numero):
    factorial=0
    if (numero==0):
        factorial=1
    else:
        factorial=serieFactorial(numero)
    return(factorial)
    

""" Para jugar un rato......
Python tiene una librería para graficar que se llama 
MatPlotLib
referencia: http://www.iac.es/sieinvens/python-course/source/matplotlib.html

Supongamos que queremos graficar el factorial de una serie de números...

Acá va el ejemplo:
    
"""

# importar el módulo pyplot
import matplotlib.pyplot as plt

# vamos a poner puntos del gráfico primero, cada punto del eje X es un número
# el eje Y será el factorial de se punto X

# esta instrucción arma una figura donde se van a graficar los puntos
plt.figure()

""" prueben cambiar la cantidad de puntos y vean qué pasa.
No usar números muy grandes porque el factorial se dispara !!! y como es un
gráfico simple las escalas quedan mal...
es para que vean otras cosas....
"""

cantidadDePuntos=4
for x in range(cantidadDePuntos+1):
    # función factorial (que la definimos arriba)
    y=factorial(x)
    
    #ahora le decimos a la librería que vaya graficando puntos
    plt.plot(x,y,'rs')
    
