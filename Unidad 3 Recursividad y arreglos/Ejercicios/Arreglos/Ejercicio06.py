'''
Desarrollar una función que elimine el elemento que ocupa una determinada posición
de un arreglo de enteros. Al eliminar se debe mantener la continuidad, es decir, los
elementos a la derecha del eliminado, deben desplazarse a la izquierda un lugar.
'''

def eliminar(lista, posicion):
    if posicion != len(lista)-1:
        laux=lista[:posicion]
        return laux +lista[posicion+1:]
    else:
        return lista[:posicion]

if __name__ == '__main__':
    lista=[1,2,3,4,5,6]
    print(eliminar(lista,1))