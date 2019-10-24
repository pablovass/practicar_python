'''
Una canilla de una casa pierde agua de forma que todos los dias pierde dos gotas mas que el dia anterior. Escribir una función recursiva que calcule
cuantas gotas perdera la canilla luego de N días, sabiendo que el primer dia solo perdia 2 gotas.
'''

def gotas(dias:int)->int:
    return 2 if dias == 1 else gotas(dias-1)+2


if __name__ == '__main__':
    print(f'Gotas en 500 dias: {gotas(500)}')