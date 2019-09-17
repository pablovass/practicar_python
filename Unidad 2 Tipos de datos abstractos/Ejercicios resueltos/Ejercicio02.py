'''
Diseñar el TDA fraccion, para representar numeros fraccionarios. Implementar las
siguientes operaciones: Crear, obtener numerador, obtener denominador, modificar
numerador, modificar denominador, sumar, restar, multiplicar, dividir, simplificar e
iguales (recibe dos fracciones e informa si son iguales o distintas).
'''


class Fraccion:
    def __init__(self, numerador:int, denominador:int):
        self.numerador = numerador
        self.denominador = denominador if denominador!=0 else 1
        self.simplificar()

    def getNumerador(self)->int:
        return self.numerador
    
    def getDenominador(self)->int:
        return self.denominador

    def setNumerador(self, n:int):
        self.numerador = n
    
    def setDenominador(self, d:int):
        self.denominador = d
    
    def sumar(self, f):
        return Fraccion(self.numerador*f.denominador+f.numerador*self.denominador, self.denominador*f.denominador)
    
    def restar(self, f):
        return Fraccion(self.numerador*f.denominador-f.numerador*self.denominador,self.denominador*f.denominador)

    def multiplicar(self, f):
        return Fraccion(self.numerador*f.numerador, self.denominador*f.denominador)
        
    def inversa(self,f):
        return Fraccion(f.denominador, f.numerador)

    def dividir(self, f):
        return self.multiplicar(self.inversa(f))

    def simplificar(self):
        dividir = self.mcd()
        self.numerador=int(self.numerador/dividir)
        self.denominador=int(self.denominador/dividir)


    def mcd(self)->int:
        u=abs(self.numerador)
        v=abs(self.denominador)
        if(v==0):
            return u
        while(v!=0):
            r=u%v
            u=v
            v=r
        return u

    def iguales(self, f)->bool:
        return True if self.numerador == f.getNumerador and self.denominador == f.getDenominador else False

    def mostrar(self)->str:
        return str(self.numerador)+'/'+str(self.denominador)



f1=Fraccion(8,9)
f2=Fraccion(12,6)

print("F1: " + f1.mostrar())
print("F2: " + f2.mostrar())
print("F1 igual a F2: " + str(f1.iguales(f2)))
f2.setNumerador(3)
print("Nuevo F2: " + f2.mostrar())
f3=f1.multiplicar(f2)
print(f1.mostrar() + " * " + f2.mostrar() + " = " + f3.mostrar())
f4=f1.dividir(f2)
print(f1.mostrar() + " / " + f2.mostrar() + " = " +  f4.mostrar())
f5 = f1.sumar(f2)
print(f1.mostrar() + " + " + f2.mostrar() + " = " +  f5.mostrar())
f6 = f1.restar(f2)
print(f1.mostrar() + " - " + f2.mostrar() + " = " +  f6.mostrar())