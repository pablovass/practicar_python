'''
Desarrollar una función que determine si una cadena de caracteres es un palíndromo.
'''

def palindromo(cadena):
    i=0
    j=len(cadena)-1
    while i<j:
        if cadena[i]!=cadena[j]:
            return False
        i+=1
        j-=1
    return True


if __name__ == "__main__":
    print(palindromo('abccba'))
    print(palindromo('abcfcba'))
    print(palindromo('abcfba'))
    print(palindromo('abccbf'))
    print(palindromo('afccba'))