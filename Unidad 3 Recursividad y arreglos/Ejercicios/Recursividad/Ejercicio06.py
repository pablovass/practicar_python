'''
Escribir una función recursiva que calcule las combinaciones de N elementos tomados
de a M, usando la siguiente expresión:

            {            N              si M = 1 }
C = (N M) = {            1              si N = M }
            { C(N-1 M-1) + C(N-1 M)     si N>M>1 }

'''
def combinaciones(N, M):
    if M==1:
        return N
    if N == M:
        return 1
    return combinaciones(N-1, M-1) + combinaciones(N-1, M) 

if __name__ == '__main__':
    print('Tengo sueño, no lo entiendo')