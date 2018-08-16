''' Las palabras reservadas break y continue 
break:  dentro de un blucle lo que hace es terminarlo entero, es decir,\
 si se ejecuta dentro de un blucle sale por completo de él.
continue: al ejecutarlo dentro de un bucle termina la iteración
en la que estaba, pero permanece en el bucle.
'''

suma = 0
for i in range(10):
    if i>7:
        break
    suma = suma + i
print("La suma con break ha sido ", suma)

suma = 0
for i in range(10):
    suma = suma + i
print("La suma sin break ha sido ", suma)


suma = 0 
print("El programa irá pidiendo números y los irá sumando "+ 
"hasta que la suma supere el valor de cien")

while(True):
    numero = eval(input("Escriba un número \n"))
    suma = suma + numero
    if suma > 100:
        break
print("La suma de los números ingresados ha superado 100")


#Programa que suma del 1 al 100 excepto el 3, 19 y 32
suma = 0
for i in range(101):
    if i == 3 or i == 19 or i == 32:
        continue
    suma = suma + i 
print("La suma deseada es: ", suma)