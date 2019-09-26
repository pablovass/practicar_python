'''
Escribir un programa que pida un numero natural n al usuario e imprima por pantalla
los n primeros numeros triangulares y su indice. El numero triangular de indice n se
define como la suma de los numeros naturales de 1 hasta n. Por ejemplo para n = 5,
la salida debe ser:
1 – 1
2 – 3
3 – 6
4 – 10
5 – 15

Nota: Hacerlo de dos formas, usando y sin usar la ecuacion:

        n
T(n)=   ∑i=(n(n+ 1))/2
       i=1

'''

def coso(n):
    for i in range(1,n+1):
        print("%d - %d" %(i,(i*(i+1))/2))

coso(5)