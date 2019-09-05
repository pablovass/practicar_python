#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:40:24 2019

@author: fernandopuricelli
"""

"""Escribir un programa que pida un numero natural n al usuario e imprima 
por pantalla los n primeros numeros triangulares y su indice. El numero triangular
 de indice n se define como la suma de los numeros naturales de 1 hasta n.
"""

""" Solución usando la ecuación"""

def triangular(n):
    return(int(n*(n+1)/2))

numero=int(input('Ingrese un número: '))
print('----------------------------------')
print('nùmeros trinagulares hasta ',numero)
print('----------------------------------')
for num in range(1,numero+1):
    print(num,'--> T(',num,')-->',triangular(num))
    
