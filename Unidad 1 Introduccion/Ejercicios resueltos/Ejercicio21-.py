'''
La funcion f (x)=ex se puede aproximar con una determinada tolerancia de error
(TOL) a traves de un polinomio de Taylor de grado N, usando a siguiente formula:

       N    
e^x ≃  ∑ x^i/i! = 1 + x/1! + x^2/2! + x^3/3! + x^4/4! + ... + x^N/N! 
      i=1

El valor de N se obtiene cuando se suma un termino menor a la tolerencia (TOL).
Implementar un algoritmo que aproxime f(x)=e^x dados los valores de x y TOL. El
algoritmo debe informar el grado del polinomio utilizado (valor de N).
'''