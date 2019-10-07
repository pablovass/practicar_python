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
    dias = [[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
            [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

    def __init__(self, dia, mes, anio):
        self.dia=dia
        self.mes=mes
        self.anio=anio
        if(not self.fechaCorrecta()):
            print("Fecha Erronea")
            self.dia=1
            self.mes=1
            self.anio=2019

    

    def fechaCorrecta(self)->bool:
        '''
        Una función que determine si una fecha es formalmente correcta, una fecha se
        define como correcta, teniendo en cuenta la cantidad de dias correctos de cada
        mes y que el año debe ser anterior o igual al 2019.
        '''
        if self.anio > 2019:
            return False
        if self.mes not in range(1, 13):
            return False
        if self.dia<1 or self.dia>self.dias[self.esBisiesto()][self.mes-1]:
            return False
        return True


    def esBisiesto(self)->bool:
        '''
        funcion auxiliar para comprobar si es bisiesto el año
        '''
        return 1 if self.anio%4 == 0 and self.anio%100 != 0 or self.anio%400 == 0 else 0

    def anterior(self):
        '''
        Una función que a partir de una fecha obtenga la correspondiente al día anterior
        '''
        if self.dia == 1:
            if self.mes == 3:
                self.dia = 29 if self.esBisiesto() else 28
                self.mes = 2
            elif self.mes == 1:
                self.dia = 31
                self.mes = 12
                self.anio -= 1
            elif self.mes in [2,4,6,8,9,11]:
                self.dia = 31
                self.mes -=1
            else:
                self.dia = 30
                self.mes -=1
        else:
            self.dia -= 1



    def siguiente(self):
        '''
        Una función que a partir de una fecha obtenga la correspondiente al día siguiente
        '''
        ##############################
        # MAL - ¡Modifica el objeto! #
        ##############################

        if self.mes == 2:
            if self.dia == 28 and self.esBisiesto():
                self.dia, self.mes = 29, 2
            elif self.dia == 28 or self.dia == 29:
                self.dia, self.mes = 1, 3
        elif self.dia == 30:
            if self.mes in [4,6,9,11]:
                self.dia = 1
                self.mes +=1
            else:
                # if self.mes in [1,3,5,78,10,12]:
                self.dia=31
        elif self.dia == 31:
            if self.mes != 12:
                self.dia = 1
                self.mes +=1
            else:
                self.dia = 1
                self.mes = 1
                self.anio += 1
        else:
            self.dia+=1



    def sumaDias(self,dias:int)->object:
        '''
        Una función que a partir de una fecha obtenga la que resulte de sumarle N días.
        '''
        fNueva = Fecha(self.dia, self.mes, self.anio)

        while dias>0:
            fNueva.siguiente()
            dias-=1
        return fNueva

    def restaDias(self,dias:int)->object:
        '''
        Una función que a partir de una fecha obtenga la que resulte de restarle N días.
        '''
        fNueva = Fecha(self.dia, self.mes, self.anio)
        while dias>0:
            fNueva.anterior()
            dias-=1
        return fNueva

    def diasEntre(self, fecha2:object)->int:
        '''
        Una función que a partir de dos fechas obtenga la cantidad de días que hay entre
        ellas.
        '''
        dias = 0

        fechaAux = self 
        fechaAux2 = fecha2

        if self.mayor(fecha2) < 0:
            fechaAux = fecha2
            fechaAux2 = self

        while not fechaAux==fechaAux2:
            fechaAux.anterior()
            dias+=1

        return dias


    
    def mayor(self, fecha:object)->int:
        '''
        Indica cual es mayor
        1   ->  self mayor
        0   ->  iguales
        -1  ->  fecha mayor
        '''
        if self==fecha:
            return 0
        else:    
            if self.anio == fecha.anio:
                if self.mes == fecha.mes:
                    return 1 if self.dia>fecha.dia else -1
                else:
                    return 1 if self.mes>fecha.mes else -1
            else:
                return 1 if self.anio>fecha.anio else -1
        


    def __eq__(self, fecha:object)->bool:
        ''' comparador '''
        return self.dia == fecha.dia and self.mes == fecha.mes and self.anio == fecha.anio


    def __str__(self)->str:
        ''' imprime objeto '''
        return f'{self.dia}/{self.mes}/{self.anio}'


a = Fecha(6,10,2019)
a2 = a
a3 = a
b = a.sumaDias(2)
c = a.restaDias(2)
d = Fecha(12,10,2019)
e = Fecha(2,2,1980)
print(f"Fecha origen: {a}")
print(f"Fecha anterior a origen: {a2.anterior()}")
print(f"Fecha posterior a origen: {a3.siguiente()}")
print(f"Sumo 2 dias a fecha origen: {b}")
print(f"Resto 2 dias a fecha origen: {c}")
print(f"Otra fecha: {d}")
print(f"Dias entre {a} y {d}: {a.diasEntre(d)}")
print(f"Dias entre {a} y {e}: {a.diasEntre(e)}")
