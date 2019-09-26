'''
Implementar algoritmos que permitan:
a) Calcular el perímetro y el área de un rectángulo, dada su base y su altura.
b) Calcular el perímetro y el área de un círculo dado su radio.
c) Calcular el volumen y el área de una esfera dado su radio.
d) Dados los catetos de un triángulo rectángulo, calcular la hipotenusa y el ángulo
(expresado en grados).
Nota: Utilizar el paquete math
'''

import math

def rectangulo(lado1: int, lado2: int):
   perimetro = 2*(lado1+lado2)
   area = lado1*lado2
   return (perimetro, area)

def circulo(radio:int):
    perimetro = 2 * math.pi * radio
    area = math.pi * math.pow(radio,2)
    return (perimetro, area)

def esfera(radio:int):
    volumen = 4/3 * math.pi * math.pow(radio,3)
    area = 4 * math.pi * math.pow(radio,2)
    return (volumen, area)

def main():
    print("Rectangulo\n Perimetro: %d\n Area: %d" %(rectangulo(2,3))) 
    print("Circulo\n Perimetro: %.2f\n Area: %.2f" %(circulo(3))) 
    print("Esfera\n Volumen: %.2f\n Area: %.2f" %(esfera(3))) 


if __name__ == "__main__":
    main()