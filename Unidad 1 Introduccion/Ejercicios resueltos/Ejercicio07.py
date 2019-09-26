'''
Escribir un programa que declare un numero entero con cualquier valor e indique si
dicho número es par o impar.
'''
def coso(n):
    return 'Par' if n%2 ==0 else 'Impar'

print('2: ' + coso(2))
print('3: ' + coso(3))