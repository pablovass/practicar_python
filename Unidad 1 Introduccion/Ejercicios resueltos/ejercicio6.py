#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:52:19 2019

@author: fernandopuricelli
"""

variable1=10
variable2=1

if (variable1>variable2):
    print('variable1')
elif (variable2>variable1):
    print('variable2')
else:
    print('iguales')


# pero hacerlo también así después de haber explicado definición de funciones en python
# es importante que retomen las buenas prácticas que tratan de introducirse en Intro


def mayorOIgual(numero1,numero2):
    return('var1' if numero1>numero2 else ('iguales' if numero1==numero2 else 'var2'))

print('otra forma de hacerlo al estilo Gobstones')
print(mayorOIgual(variable1,variable2))