#Escribir una función que tenga múltiples retornos

def suma_y_producto(a,b):
    suma = a + b
    producto = a * b
    return suma, producto

def main():
    a = eval(input("Ingrese un número \n"))
    b = eval(input("Ingrese otro número \n"))
    print("La suma y el producto de ", a, " con ", b, " es ", suma_y_producto(a,b))


'''Función recursiva que pide un número entero, 
imprime los pares menores o iguales que el y dice cuantas
veces entró a la recursión'''


def numeros_pares(n,contador=0):
    if n == 2:
        print("El número de veces que se ingresó a la función fue", contador)
        print(2)
    else:
        contador += 1
        numeros_pares(n-1, contador)
        if n % 2 == 0:
            print(n)

numeros_pares(11)