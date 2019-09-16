'''
Escribir un programa que declare un numero entero del 1 al 7 y muestre por pantalla
el dia de la semana correspondiente. Controlar que el numero se encuentre en el
rango correcto, si no es asi, informar un error. Si el numero es 2 el dia es martes
'''
dicccionario = { 1:'lunes',2:'martes',3:'miercoles',4:'jueves',5:'viernes',6:'sabado',7:'domingo'}

print(dicccionario.get(2))