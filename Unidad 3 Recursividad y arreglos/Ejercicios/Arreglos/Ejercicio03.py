'''
Crear un programa que lea por teclado N números enteros y los desplace una
posición hacia la derecha: el primero pasa a ser el segundo, el segundo pasa a ser el
tercero y así sucesivamente. El último pasa a ser el primero. Guardar los numeros
ingresados en un arreglo en el orden original y luego correrlos dentro del mismo
arreglo. Mostrarlos antes y despues por pantalla.
'''

def coso(lista):
    aux = lista[0]
    posicion = 1
    while posicion<len(lista):
        aux2 = lista[posicion]
        lista[posicion] = aux
        aux = aux2
        posicion+=1
    lista[0]=aux
    return lista
  
  
  if __name__ == '__main__':
    print(coso([1,2,3,4]))
