'''
Desarrollar una función que elimine la primera aparición de un elemento determinado
de un arreglo de enteros.
'''

def eliminar(lista, dato):
    x=0
    while dato != lista[x]:
        x+=1

    if x != len(lista)-1:
        laux=lista[:x]
        return laux +lista[x+1:]
    else:
        return lista[:x]

if __name__ == '__main__':
    lista=[1,2,3,4,3,5,6]
    print(eliminar(lista,3))