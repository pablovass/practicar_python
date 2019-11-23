'''
Escribir funciones que dada una cadena de caracteres:
a) Imprima los dos primeros caracteres.
b) Imprima los tres últimos caracteres.
c) Imprima dicha cadena cada dos caracteres. Ej.: 'recta' debería imprimir 'rca'
'''

def primeroDosCaracteres(cadena):
    return cadena[:2]

def ultimosTresCaracteres(cadena):
    return cadena[len(cadena)-3:len(cadena)]

def cadaDosCaracteres(cadena):
    aux=[]
    for i in range(0,len(cadena),2):
        aux.append(cadena[i])
    return ''.join(aux)

if __name__ == "__main__":
    print(primeroDosCaracteres('Sebastian'))
    print(ultimosTresCaracteres('Sebastian'))
    print(cadaDosCaracteres('Sebastian'))
