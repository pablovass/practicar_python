'''
Escribir un programa que pida por teclado una lista de N numeros y los imprima en
forma inversa, es decir, que muestre por pantalla, al finalizar en ingreso de los N
numeros, desde el ultimo hasta el primero. Implementarlo con una funcion recursiva
'''

def inversador(numeros):
    if len(numeros) == 1:
        return numeros
    return inversador(numeros[1:len(numeros)]) + numeros[0:1]

if __name__ == '__main__':
    lista = [1,2,3,4]
    print(inversador(lista))