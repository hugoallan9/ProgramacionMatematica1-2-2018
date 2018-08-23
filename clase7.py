
'''Programa que calcula el factorial de dos formas:
1. Usando un ciclo
2. Usando una función recursiva
'''

import sys 
import time as t

sys.setrecursionlimit(1500000)

def factorial1(n):
    resultado = 1
    for i in range(n):
        resultado = resultado * (i +1 )
    return(resultado)

def factorial2(n):
    if n == 1:
        return(1)
    else:
        return( n * factorial2(n-1) )

def main():
    n = eval(input("Ingrese un número: \n"))
    inicio_f1 =  t.time()
    print(factorial1(n))
    fin_f1 = t.time()
    print("El tiempo de ejecución del ciclo ha sido, ", fin_f1 - inicio_f1)
    inicio_f2 = t.time()    
    print(factorial2(n))
    fin_f2 = t.time()
    print("El tiempo de ejecución del ciclo ha sido, ", fin_f2 - inicio_f2)
    if (fin_f1 - inicio_f1) > (fin_f2 - inicio_f2):
        print("El ciclo es más lento que la recursión")
    elif (fin_f1 - inicio_f1) < (fin_f2 - inicio_f2):
        print("La recursión es más lento que el ciclo")
main()