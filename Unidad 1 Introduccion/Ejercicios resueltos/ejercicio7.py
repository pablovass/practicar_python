#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 16:57:09 2019

@author: fernandopuricelli
"""

numero=19

if(numero%2==0):
    print('par')
else:
    print('impar')


""" OTRA FORMA: usando funciones """

def esParOImpar(numero):
    return('par' if numero%2==0 else 'impar')
