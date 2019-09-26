'''
Escribir un programa que pida un numero entero y muestre por pantalla la cantidad de
cifras de dicho numero.
'''
def pedirNumero() -> str:
    return input("numero: ")

def contarCifras(numero: str) -> int:
    return len(numero)

def main():
    a = pedirNumero()
    print("Cantidad de cifras de %s:  %d" %(a,contarCifras(a)))

main()