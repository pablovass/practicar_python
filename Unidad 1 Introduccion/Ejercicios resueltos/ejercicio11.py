#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:18:34 2019

@author: fernandopuricelli
"""

""" Ej 11: Escribir un programa que imprima por pantalla todas las fichas
 del domino, una por linea, sin repetir."""
 
 
def muestraBordeFicha():
     print('||',end='')
 
def muestraNumeros(num1,num2):
    print(num1,'|',num2,end='')

def separaFicha():
    print(end=' ')
    
def armaFichasCon(numero):
    for num2 in range(numero,7):
        muestraBordeFicha()
        muestraNumeros(numero,num2)
        muestraBordeFicha()
        separaFicha()

def separaSiguienteSerieDeFichas():
    print('\n')

def fichasDomino():
    for num in range(1,7):
        armaFichasCon(num)
        separaSiguienteSerieDeFichas()
        

fichasDomino()