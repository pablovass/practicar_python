'''
Escribir un programa que recibe como entrada desde el usuario dos numeros enteros
e informa por pantalla todos los numeros pares entre ellos.
'''

def ingreso():
    a = int(input("Numero 1: "))
    b = int(input("Numero 2: "))
    return a, b

def pares(a, b):
    x,y = (a,b) if a<b else (b,a)
    return list(filter(lambda x: x%2==0, range(x,y+1)))

def main():
    a,b = ingreso()
    print(pares(a,b))

main()