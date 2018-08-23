'''Programa que calcula el n-esimo número de fibbonacci 
de manera recursiva, tomando f_0 =1 y f_1 = 1'''


def fibbonacci(n): 
    if n == 1 or n==2:
        return(1)
    elif n <0:
        return(0)
    else:
        return( fibbonacci(n-1) + fibbonacci(n-2) )

def main():
    n = eval(input("Ingrese la posición del número de fibbonacci que"+ 
    "desea conocer: \n"))
    print( fibbonacci(n) )

main()