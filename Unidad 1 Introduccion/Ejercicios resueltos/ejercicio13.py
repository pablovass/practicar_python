#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:26:14 2019

@author: fernandopuricelli
"""

def esPar(numero):
    return(numero%2==0)

def sumarParesHastaN(n):
    suma=0
    for i in range(n):
        if esPar(i):
            suma=suma+i
    return(suma)

""" Otra forma de definir la función , por eso en el nombre tiene un 2 al final """

def sumarParesHastaN2(n):
    suma=0
    for i in range(n):
        suma=suma+(i if esPar(i) else 0)
    return(suma)



numeroHasta=int(input('número natural:'))
print('Suma:','\t',sumarParesHastaN(numeroHasta))
print('Suma (otra forma):','\t',sumarParesHastaN2(numeroHasta))

