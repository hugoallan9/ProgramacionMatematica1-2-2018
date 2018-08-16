'''By considering the terms in the Fibonacci sequence whose 
values do not exceed four million, find the sum of the even-valued 
terms'''

fib1 = 1
fib2 = 2
temp = 0
suma_pares = 0

while temp < 4000000:
    temp = fib2
    if temp % 2 == 0:
        suma_pares += temp # suma_pares = suma_pares + temp 
    temp = fib1 + fib2
    fib1 = fib2
    fib2 = temp

print("La suma de los F_n pares menores a 4e6 es ", suma_pares)