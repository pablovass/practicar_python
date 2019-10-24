'''
Implementar una funcion que calcule el factorial de un numero de forma recursiva
'''

def factorial(numero:int)->int:
    return 1 if numero == 1 else factorial(numero-1) * numero


if __name__ == '__main__':
    print(f'Factorial de 5: {factorial(5)}')