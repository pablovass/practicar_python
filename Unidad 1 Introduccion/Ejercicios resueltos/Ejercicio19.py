'''
Escribir un programa que calcule el factorial de un numero natural introducido por el
usuario. La operación factorial (!) se define de la siguiente manera:

N!={N si N=0, (N1−1)! si N>0} = N(N−1)(N−2)...3.2.1
'''

def factorialWhile(numero):
    n=numero-1
    r=numero
    while n>1:
        r*=n
        n-=1
    return r if numero>0 else 1


def factorialFor(numero):
    r=numero
    for i in range(numero-1,1,-1):
        r*=i
    return r if numero>0 else 1

def main():
    print("Con while: %d" %(factorialWhile(12)))
    print("Con for y range: %d" %(factorialFor(12)))

if __name__ == "__main__":
    main()
