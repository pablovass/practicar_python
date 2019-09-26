'''
Escribir un programa que imprima por pantalla todas las fichas del domino, una por
linea, sin repetir.
'''

def bordeFicha():
    return'||'

def separadorFicha():
    return '|'

def ficha(n): 
    for i in range (n,7):
        print('%s%d%s%d%s ' %(bordeFicha(),n,separadorFicha(),i,bordeFicha()), end='')
    return n+1
        
def fichasDomino():
    n=1
    while n<7:
        n=ficha(n)
        print()

fichasDomino()