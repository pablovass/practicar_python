#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 15:30:06 2019

@author: fernandopuricelli
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

def termino(xi,n):
    return(xi**n/factorial(n))

def polinomioTaylor(x,tol):
    sumatoria=1
    indice=1
    while(termino(x,indice)>=tol):
        sumatoria=sumatoria+termino(x,indice)
        indice+=1
    return(sumatoria)

x=6
tol=0.00004

ex=polinomioTaylor(x,tol)
print('Ex - siendo x=',x,' es aprox:', ex)

