'''
Escribir una función recursiva que pase un numero decimal a base 2
'''
def binario(numero:int)->str:
    if numero == 1 or numero == 0:
        return str(numero)
    if numero//2 == 1:
        return '1' + str(numero%2)
    else:
        return binario(numero//2)+str(numero%2)



if __name__ == '__main__':
    print(binario(0))
    print(binario(1))
    print(binario(2))
    print(binario(5))
    print(binario(8))
    print(binario(17))
    print(binario(1953678422))