'''
Desarrollar una función que inserte un elemento en un arreglo de enteros, ordenado
en forma ascendente, de forma de no alterar el orden.
'''

def insercionOrdenada(lista, numero):
    x=0
    while x!=len(lista):
        if(numero>lista[x]):
            x+=1
        else:
            laux=lista[0:x]
            laux.append(numero) 
            return laux+lista[x:]
    lista.append(numero)
    return lista


if __name__ == '__main__':
    lista = [1,6,8]
    print(lista)
    lista = insercionOrdenada(lista, 0)
    print(lista)
    lista = insercionOrdenada(lista, 3)
    print(lista)
    lista = insercionOrdenada(lista, 9)
    print(lista)