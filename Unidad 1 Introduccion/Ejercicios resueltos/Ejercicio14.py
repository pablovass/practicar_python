'''
Escribir un programa que recibe como entrada desde el usuario los valores de a, b y
c de un polinomio de grado 2, e informa las raices (reales y complejas).
'''
import math

def recibirValores():
    a = int(input("Valor 1: "))
    b = int(input("Valor 2: "))
    c = int(input("Valor 3: "))
    return a, b, c

def raiz(b, c):
    return math.pow(b,2) - 4 * c

def calcularRaices():
    a,b,c = recibirValores()

    if a==0:
        return (0,0)
    centro = raiz(b,c)
    if centro>=0:
        return str(((-b + math.sqrt(centro))/2*a,(-b - math.sqrt(centro))/2*a))
    else:
        return ("(%.2f±%.2fi)" %((0-b)/2*a, math.sqrt(-centro)/2*a))

def main():
    print(calcularRaices())

main()