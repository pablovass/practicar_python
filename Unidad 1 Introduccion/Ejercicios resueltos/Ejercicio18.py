'''
Escribir un programa que imprima por pantalla los numeros desde el 32 al 64, en
todas las bases desde 2 hasta 16. Se debe imprimir un numero por fila en las 15
bases distintas separados por el carácter tabular (“\t”). Nota: Los numeros se pueden
imprimir en orden inverso
'''

def cambioBase(decimal:int, base:int)->str:
    conversion = ''
    mayor10 = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while decimal // base != 0:
        r = decimal % base
        conversion = (str(r) + conversion if r<10  else mayor10.get(r) + conversion) 
        decimal = decimal // base
    return str(decimal) + conversion if decimal<10 else mayor10.get(decimal) + conversion


def cambioNumero():
    print(" ________________________________________________________________________________________________________________________")
    print("|2\t|3\t|4\t|5\t|6\t|7\t|8\t|9\t|10\t|11\t|12\t|13\t|14\t|15\t|16\t|")
    print("|-----------------------------------------------------------------------------------------------------------------------|")
    for i in range(32, 64):
        print("|", end='')
        for j in range(2,17):
            print(cambioBase(i, j)+"\t|", end='')
        print("")
    print("|"+cambioBase(64, 2)+"|", end='')
    for j in range(3,17):
        print(cambioBase(64, j)+"\t|", end='')
    print("")
    print("-------------------------------------------------------------------------------------------------------------------------")

cambioNumero()
