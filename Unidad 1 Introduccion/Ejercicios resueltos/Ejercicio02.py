'''
Escribir un programa que cargue en una variable un número entero e imprima por
pantalla su tabla de multiplicar (del 1 al 12)
'''

numero = int(input("Ingrese numero: "))
x=1
while(x<=12):
    print(numero*x)
    x+=1

print(list(map(lambda x: x*numero,range(1,13))))

'''
coso = lambda x: x*3
coso(3)
'''
