#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 14:10:09 2019

@author: fernandopuricelli
"""

""" Ej 8: Escribir un programa que declare un numero entero del 1 al 7 y 
muestre por pantalla el dia de la semana correspondiente. 
Controlar que el numero se encuentre en el rango correcto, 
si no es asi, informar un error. Si el numero es 2 el dia es martes."""

def diaDeLaSemana(numeroDeDia):
    return('martes' if numeroDeDia==2 else ('miércoles' if numeroDeDia==3 else (
            ('jueves' if numeroDeDia==4 else('viernes' if numeroDeDia==5 else
                ('viernes' if numeroDeDia==6 else('sábado' if numeroDeDia==7 else
                    ('domingo' if numeroDeDia==1 else 'ERROR' ))))))))

unDia=6
print(diaDeLaSemana(unDia))