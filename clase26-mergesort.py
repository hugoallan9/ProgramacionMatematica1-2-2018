import time
import numpy as np

def mergeSort(lista):
    n = len(lista)
    if (n > 1):
        mitad = n // 2
        lizquierda = lista[:mitad]
        lderecha = lista[mitad:]

        mergeSort(lizquierda) #Aplicación de recurrencia en ambas listas
        mergeSort(lderecha)



        i = j = k =  0
        while i < len(lizquierda) and j < len(lderecha):
            if lizquierda[i] < lderecha[j]:
                lista[k] = lizquierda[i]
                i = i + 1
            else:
                lista[k] = lderecha[j]
                j = j + 1
            k = k + 1

        #Verfico si se salio del ciclo por izquierda o por derecha
        while i < len(lizquierda):
            #Hacer el append
            lista[k] = lizquierda[i]
            i += 1
            k += 1

        while j < len(lderecha):
            #Hacer el append
            lista[k] = lderecha[j]
            j += 1
            k += 1




A = np.random.rand(1,10000)
inicio = time.time()
A = A[0]
mergeSort(A)
fin = time.time()
print(fin - inicio)