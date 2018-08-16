''' Uso de for y while con ejemplos '''

for x in range(10):
    print(" El saludo número ", x+1 )

sumatoria = 0 
for x in range(101):
    sumatoria = sumatoria  + x

print("La suma de los primeros 100 números naturales es: ", sumatoria)

sumatoria_par = 0

for x in range(101):
    if x % 2 == 0:
        sumatoria_par = sumatoria_par + x

print("La suma de los primeros 100 números naturales pares es: ", sumatoria_par)

sumatoria_impar = 0

for x in range(101):
    if x % 2 == 1:
        sumatoria_impar = sumatoria_impar + x

print("La suma de los primeros 100 números naturales impares es: ", sumatoria_impar)

# Otra forma de hacerlo
sumatoria_par = 0

for x in range(0,101,2):
        sumatoria_par = sumatoria_par + x

print("La suma de los primeros 100 números naturales pares es: ", sumatoria_par)

#Con un while la misma tarea

contador = 0
sumatoria_par = 0  
while contador <= 100:
    sumatoria_par  = sumatoria_par + contador
    contador = contador + 2 
print("La suma de los primeros 100 números naturales pares es: ", sumatoria_par)