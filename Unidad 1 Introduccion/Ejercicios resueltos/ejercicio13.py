'''
Construir un programa que lea un número natural N y calcule la suma de los primeros
N números pares.
'''

def calculo(N):
    r = 0
    for i in range(N+1):
        if(i%2==0):
            r+=i
    return r

def calculo2(N):
       r=0
       for i in range(N+1):
           r+= i if i%2==0 else 0
       return r

print(calculo(7))
print(calculo2(5))