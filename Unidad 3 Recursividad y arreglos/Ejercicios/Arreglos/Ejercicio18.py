'''
Escribir una funcion que dada una cadena de caracteres devuelva solamente las
letras consonantes. Por ejemplo, si recibe 'algoritmos' o 'logaritmos' debe devolver
'lgrtms'.
'''

def vocalesAfuera(cadena):
    return ''.join(list(filter(lambda x: x not in ['a','e','i','o','u'], cadena)))


if __name__ == "__main__":
    print(vocalesAfuera('sebastian'))