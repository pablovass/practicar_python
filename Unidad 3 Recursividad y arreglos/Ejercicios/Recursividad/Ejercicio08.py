'''
Escribir una función recursiva que reciba un numero positivo N y calcule la cantidad
de digitos que tiene
'''

def digitos(numero):
    return 1 if numero//10 == 0 else 1 + digitos(numero//10)

if __name__ == '__main__':
    print(digitos(1))
    print(digitos(123))
    print(digitos(1234567890))