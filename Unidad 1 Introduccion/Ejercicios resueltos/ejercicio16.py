#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:17:05 2019

@author: fernandopuricelli
"""

""" Ej. 16: Escribir un programa que pida un numero entero 
y muestre por pantalla la cantidad de cifras de dicho numero."""

def cifras(num):
    cifras=1
    while(num//10>0):
        num=num/10
        cifras+=1
    return(cifras)

numero=int(input('número: '))
print('el número: ',numero,' tiene ',cifras(numero),' cifras')
