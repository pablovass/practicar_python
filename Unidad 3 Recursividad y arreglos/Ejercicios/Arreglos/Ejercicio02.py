'''
Escribir una función recursiva que multiplique todos los elementos de un vector de
enteros.
'''
def insertar(lista, dato, posicion):
    largo = len(lista)
    while posicion<largo and lista[posicion] != None:
        aux=lista[posicion]
        lista[posicion]= dato
        dato=aux
        posicion+=1
    if posicion<largo and lista[posicion] == None:
        lista[posicion]= dato
    return lista

if __name__=='__main__':
    lista=[1,None,None, 5,None, 6]
    print(len(lista))
    print(insertar(lista, 3, 2))
    print(insertar(lista, 4, 3))
    print(insertar(lista, 2, 1))
    print(insertar(lista, 0, 0))
