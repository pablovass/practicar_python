'''
Escribir un programa que pida por teclado un numero natural N y devuelva los
primeros N números de la serie de Fibonacci. Implementar la serie de Fibonacci de
forma recursiva
'''

def fibonacci(n:int)->int:
    return n if n<=1 else fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    f = []
    for i in range(10):
        f.append(fibonacci(i))
    print(f'Fibonacci de orden 10: {f}')