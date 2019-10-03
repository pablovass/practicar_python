'''
Diseñar el TDA polinomio de segundo grado (con coeficientes reales) e implementar las operaciones: Crear, modificar coeficientes (por separado a, b y c), obtener
coeficientes (por separado a, b y c), evaluar en un valor de x = X, suma, resta, obtener raices (reales y complejas), obtener vertice y pertenece (recibe un punto 
p = (X, Y) e informa si el punto pertenece o no al polinomio).
Nota: Utilizar el TDA complejo construido en el Ejercicio 1.
'''
import math
from Ejercicio01 import Complejo

class Poliniomio:
    """Clase para trabajar con polinomios"""

    # Crear
    def __init__(self, a=1, b=1, c=1):
        self.a = a
        self.b = b
        self.c = c

    
    # modificar coeficientes (por separado a, b y c)
    def setA(self, a):
        self.a = a
    
    def setB(self, b):
        self.b = b

    def setC(self, c):
        self.c = c


    # obtener coeficientes (por separado a, b y c)
    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getC(self):
        return self.c

    # suma
    def suma(self, poli):
        return Poliniomio(self.a + poli.getA(), self.b + poli.getB(), self.c + poli.getC())

    # resta
    def resta(self, poli):
        return Poliniomio(self.a - poli.getA(), self.b - poli.getB(), self.c - poli.getC())
    
    # obtener raices (reales y complejas) Nota: Utilizar el TDA complejo construido en el Ejercicio 1.
    def raices(self):
        if a==0:
            return (-(self.c)/self.b, -(self.c)/self.b)

        d = self.b**2 - 4*self.a*self.b 
        
        if d>=0:
            return ((-b+math.sqrt(d))/2*self.a, (-b-math.sqrt(d))/2*self.a)

        r1 = -(self.b)/2*self.a
        r2 =  math.sqrt(4*self.a*self.b - self.b**2)/2*self.a
        return (Complejo(r1, r2), Complejo(r1, -r2))


    # obtener vertice
    def vertice(self):
        return (-self.b)/2*self.a

    # pertenece (recibe un punto p = (X, Y) e informa si el punto pertenece o no al polinomio)
    def pertenece(self, x, y):
        return y == self.a*(x**2)+self.b*x+self.c
