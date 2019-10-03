#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 17:31:15 2019

@author: fernandopuricelli
"""

import math

class Complejo:
    def __init__(self, r=0, i=0):
        self.real = r
        self.img = i

    def getReal(self):
        return self.real

    def getImg(self):
        return self.img

    def modReal(self, r):
        self.real = r
    
    def modImg(self, i):
        self.img = i

    def mostrar(self):
        if self.img >= 0:
            print("%s + %s i" % (self.real, self.img))
        else:
            print("%s - %s i" % (self.real, abs(self.img)))    

    def sumar(self, c):
        return Complejo(self.real+c.real,self.img+c.img)

    def restar(self, c):
        return Complejo(self.real-c.real,self.img-c.img)
    
    def modulo(self):
        return math.sqrt(self.real**2 + self.img**2)
    
    def fase(self):
        return math.atan(self.img/self.real)

    def conjugado(self):
        return Complejo(self.real, (-1)*self.img)

    def multiplicar(self, c):
        return Complejo(self.real*c.real-self.img*c.img , self.real*c.img+c.real*self.img)

    def dividir(self, c):
        salida = self.multiplicar(c.conjugado())
        salida.real = salida.real / (c.modulo()**2)
        salida.img = salida.img / (c.modulo()**2)
        return salida
