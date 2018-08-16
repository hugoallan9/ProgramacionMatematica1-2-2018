''' Programación funcional y algunos ejemplos.
Debe tomar en cuenta que todos los programas necesitan una función
principal que se denotan por main '''

''' Sintáxis para definir una función.
Se utiliza la palabra reservada def, de la siguiente manera:
def nombre_de_la_funcion(parametro1,parametro2,parametro3, ...):
    Cuerpo de la función
'''

var_global = 5

def main():
    suma = suma_numeros( eval(input('Ingrese un número natural: \n')) )
    print(suma + var_global)

def suma_numeros(x):
    var_global = 0
    suma = 0
    for i in range(0,x+1):
        suma += i
    return(suma + var_global)

#if __name__ == '__main__':
#    main()

main()