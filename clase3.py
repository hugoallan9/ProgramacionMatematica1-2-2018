''' Función format. Tiene dos parámetros
valor :  valor o tipo de dato que se desea formatear
formato: Se tiene formas de definir los formatos, del estilo
[[fill]align][sign][#][0][width][,][.precision][type]
'''

# Algunos ejemplos
print( format(111235) ) 
#Fijando la anchura
print( format(1212343, "5") )
print ( format(15, "5") )
print ( format(150, "a>+5") )

#Formateo con punto flotante
formato = ",.1f"
print( format(1523135135135.15465, formato ) )

# Condicionales

while True:
    a  = eval( input("Ingrese un número \n") ) 
    if a < 3:
        print("El número a es mas pequeño que 3")
    elif a > 3:
        print("El número a es mas grande que 3")
    else:
        print("El número a es igual a 3")