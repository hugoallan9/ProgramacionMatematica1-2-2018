#-*-coding:utf8 -*-

''' Este programa resuelve una ecuación cuadrática
Entradas: a, b y c los coeficientes de X^2, x y el término independiente
Salidas: Las raíces de la ecuación cuadrática
'''

a = eval( input("Ingresa el coeficiente de X^2 \n") )
b = eval( input("Ingresa el coeficiente de X \n") )
c = eval( input("Ingresa el término independiente \n") )

x1 = -b / 2 +  (b**2 - 4 * a * c)**(0.5) / 2
x2 = -b / 2 -  (b**2 - 4 * a * c)**(0.5) / 2

print(x1,x2)
print( "Una de las raíces es ", x1 )
print("La otra raíz es :", x2 )