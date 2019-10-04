#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Definir el TDA “fecha”, con los atributos: dia, mes y año. Desarrollar:
a) Una función que determine si una fecha es formalmente correcta, una fecha se
define como correcta, teniendo en cuenta la cantidad de dias correctos de cada
mes y que el año debe ser anterior o igual al 2019.
b) Una función que a partir de una fecha obtenga la correspondiente al día siguiente o
al dia anterior.
c) Una función que a partir de una fecha obtenga la que resulte de sumarle N días.
d) Una función que a partir de una fecha obtenga la que resulte de restarle N días.
e) Una función que a partir de dos fechas obtenga la cantidad de días que hay entre
ellas.
'''

class Fecha:
    def __init__(self, dia, mes, anio):
        self.dia=dia
        self.mes=mes
        self.anio=anio
        if(not self.fechaCorrecta()):
            print("Fecha Erronea")
            self.dia=1
            self.mes=1
            self.anio=2019

    

    def fechaCorrecta(self):
        dias = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
                [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

        if self.anio > 2019:
            return False
        if self.mes not in range(1, 13):
            return False
        if self.dia<1 or self.dia>dias[self.esBisiesto()][self.mes-1]:
            return False
        
        return True


    def esBisiesto(self):
        return 1 if self.anio%4 == 0 and self.anio%100 != 0 or self.anio%400 == 0 else 0

    def anterior(self):
        pass

    def siguiente(self):
        pass

    def sumaDias(self,dias):
        pass
    
    def restaDias(self,dias):
        pass

    def diasEntre(self, fecha2):
        pass

    def __str__(self):
        return f'{self.dia}/{self.mes}/{self.anio}'


a = Fecha(2,31,1980)
print(a)
