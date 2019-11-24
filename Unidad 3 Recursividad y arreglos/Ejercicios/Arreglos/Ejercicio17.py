'''
Escribir una funcion que dada una cadena y un carácter inserte el caracter entre cada
letra de la cadena. Ej: 'separar' y ',' debería devolver 's,e,p,a,r,a,r
'''

def funcionCoso(cadena, separador):
    return separador.join(list(map(lambda x: x ,cadena)))

if __name__ == "__main__":
    print(funcionCoso('sebastian', '-'))