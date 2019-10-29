'''
Escribir un programa que le pida al usuario que ingrese N números naturales (primero
uno, luego otro, y así hasta que el usuario ingrese N numeros). Al final, el programa
debe imprimir los números que fueron ingresados en orden inverso, la suma total de
los valores y el promedio.
'''

def prompt(N):
    lista = []
    c=1
    lista.append(int(input("Ingese un numero: ")))
    while c<N-1:
        lista.append(int(input("Ingese otro numero: ")))
        c+=1
    lista.append(int(input("Ingese el ultimo numero: ")))
    return lista

def inverso(lista):
    return list(map(lambda x: x, reversed(lista)))

def suma(lista):
    return sum(lista)

def promedio(lista):
    return suma(lista)/len(lista)    

if __name__ == '__main__':
    lista=prompt(3)
    print(lista)
    print(inverso(lista))
    print(sum(lista))
    print(promedio(lista))