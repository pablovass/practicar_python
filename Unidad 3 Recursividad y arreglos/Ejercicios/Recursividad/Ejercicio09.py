'''
Escribir un programa que reciba dos enteros positivos n y b y devuelva True si n es
potencia de b y False en caso contrario:
esPotencia(8 , 2) = True
esPotencia(64 , 4) = True
esPotencia(16 , 3) = False
esPotencia(2 , 8) = False
'''

def esPotencia(n, b):
    if n%b==0:
        return True if n//b==1 else esPotencia(n//b, b)
    return False

if __name__ == '__main__':
    print(esPotencia(8 , 2))
    print(esPotencia(64 , 4))
    print(esPotencia(16 , 3))
    print(esPotencia(2 , 8))