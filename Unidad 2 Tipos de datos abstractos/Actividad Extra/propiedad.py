#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 17:21:07 2019


"""

""" Crear el TAD Propiedad 

-tipo (por defecto un ‘terreno’)
-calle
-altura
-año de construcción (por defecto 0, hasta que se construya)
-ancho del terrno
-largo del terreno
-superficie de construcción (este dato se completa al construir 
   una ‘casa’)

--------

Operaciones:
    
    * Las interfaces para obtener cada dato:  Get....
    * construir en un terreno. En ese momento se registra el año de la construcción,
        la superficie construida y el tipo de construcción (‘casa’ u ‘otro’).
    * Se desea saber para cada propiedad el sentido de circulación de la calle
        - O --> E
        - E --> O
    * Obtener el valor de la propiedad sabiendo que el mt2 tiene un valor de:
             $ 5.000 si es terreno
             $ 10.000 si es casa
             $ 8.000 si es “otro”
    * Indicar si al estar parado en una calle determinada, la propiedad:
            - Está hacia el NORTE, hacia el SUR
            - o en la misma calle
"""

