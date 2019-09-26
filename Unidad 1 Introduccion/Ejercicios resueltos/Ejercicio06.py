'''
Declarar dos variables enteras (con cualquier valor) e informar por pantalla cual es
menor de las dos, si son iguales, indicarlo por separado. Cambiar el orden de los
valores para comprobar el funcionamiento.
'''

def menor(a, b):
    print("variable 1" if a<b else ("variable 2" if b<a else "Iguales"))

b=2
a=2
menor(a,b)
