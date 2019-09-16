'''
Escribir un programa que pida un numero entero e informe si dicho numero es primo
o no primo. Nota: Ningun numero es divisible por un numero mayor a la raiz cuadrada
de si mismo
'''
import math

def pedirNumero() -> int:
    return int(input("numero: "))


def numeroPrimo(numero:int)->bool:
    i=2
    while i <math.sqrt(numero):
        if numero%i==0:
            return False
        i+=1
    return True

def main():
    a = pedirNumero()
    print(("%d es numero primo -> %s") %(a,numeroPrimo(a)))

main()
