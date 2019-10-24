'''
Escribir una funcion recursiva que calcule el numero triangular de indice N (Suma de
los primeros N números enteros). Recordar que:
T(N)=N+T(N−1)
'''


def triangular(N:int)->int:
    return 1 if N==1 else N+triangular(N-1)


if __name__ == "__main__":
    print(triangular(7))