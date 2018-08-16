
'''Programa que calcula el factorial de dos formas:
1. Usando un ciclo
2. Usando una función recursiva
'''

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
    print(factorial1(n))
    print(factorial2(n))

main()