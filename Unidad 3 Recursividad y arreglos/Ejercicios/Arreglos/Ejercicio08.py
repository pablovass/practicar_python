'''
Desarrollar una función que elimine todas las apariciones de un determinado
elemento de un arreglo de enteros.
'''

def eliminar(lista, dato):
    while dato in lista:
        lista.remove(dato)
    return lista

if __name__ == '__main__':
    lista= [1,2,3,3,4,6,3,9]
    lista = eliminar(lista,3)
    print(lista)