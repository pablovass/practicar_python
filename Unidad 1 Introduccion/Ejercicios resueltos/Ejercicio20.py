'''
Escribir un programa que calcule el numero combinatorio de dos numeros naturales
m y n. El numero combinatorio de m agrupados de a n se calcula de la siguiente
manera:

C=(m n)= m!/(n!(m-n)!)

Implementar dentro del programa, una funcion que calcule el factorial de un numero.
Nota: Se debe controlar que ambos numeros sean naturales y mostrar por pantalla un
error en caso contrario.
'''

def factorial(numero:int) -> int:
    r = numero
    for i in range(numero-1,1,-1):
        r*=i
    return r if numero>0 else 1

def combinatorio(numeroN:int , numeroM:int)->float:
    return factorial(numeroM) / (factorial(numeroN)*factorial(numeroM-numeroN))


print(combinatorio(6,8))
