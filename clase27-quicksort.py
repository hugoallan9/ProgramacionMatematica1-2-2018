import time
import numpy as np

def particion(lista, low, high):
    pivote = lista[high]
    i = low - 1

    for j in range(low, high):
        if lista[j] <= pivote:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i+1], lista[high] = lista[high], lista[i+1]

    return i+1

def quicksort(lista,low,high):
    if low < high:
        pi = particion(lista, low, high)
        quicksort(lista, low,  pi - 1)
        quicksort(lista, pi+1, high)


A = np.random.rand(1,10000)
inicio = time.time()
A = A[0]
quicksort(A, 0, len(A) - 1 )
fin = time.time()
print(fin - inicio)

