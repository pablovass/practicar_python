'''
Escribir un programa que calcule el factorial de un numero natural introducido por el
usuario. La operación factorial (!) se define de la siguiente manera:

N!={N si N=0, (N1−1)! si N>0} = N(N−1)(N−2)...3.2.1


Python tiene una librería para graficar que se llama MatPlotLib
referencia: http://www.iac.es/sieinvens/python-course/source/matplotlib.html

Supongamos que queremos graficar el factorial de una serie de números...
'''

# importar el módulo pyplot
import matplotlib.pyplot as plt
# importar la funcion del coso anterior
from Ejercicio19 import factorialFor as fct

# vamos a poner puntos del gráfico primero, cada punto del eje X es un número
# el eje Y será el factorial de se punto X

# esta instrucción arma una figura donde se van a graficar los puntos
plt.figure()

""" 
Probar cambiar la cantidad de puntos y ver qué pasa.
No usar números muy grandes. O si...?
"""

cantidadDePuntos=10
for x in range(cantidadDePuntos+1):
    # función factorial
    y = fct(x)
    
    # ahora le decimos a la librería que vaya graficando puntos 
    plt.plot(x,y, 'o')

# esto pone las etiquetas
plt.xlabel('normales')
plt.ylabel('factorizados')

# y aca lo mostramos
plt.show()