#!/usr/bin/python

import math 

b = 5
h = 6
r = 3
co = 10.0
ca = 10.0

pr = 2*b + 2*h
ar = b * h

pc = 2 * math.pi * r
ac = math.pi * (r ** 2)

ae = 4 * math.pi * (r ** 2) 
ve = (4.0/3.0) * math.pi * (r ** 3) 

ht = math.sqrt(co ** 2 + ca ** 2)
at = math.atan(co / ca)* 360 / (2 * math.pi)

print("Perimetro del rectangulo =" , pr)
print("Area del rectangulo =" , ar)
print("Perimetro del circulo =" , pc)
print("Area del circulo =" , ac)
print("Area de esfera =" , ae)
print("Volumen de esfera =" , ve)
print("Hipotenusa del triangulo =" , ht)
print("Angulo del triangulo =" , at)
