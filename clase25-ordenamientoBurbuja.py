
import numpy as np
import  time as time

def ordenamiento_burbuja(A):
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                temp = A[i]
                A[i] = A[j]
                A[j] = temp
    return A


if __name__ == "__main__":
    A = [20,7,2,23,8]
    print( ordenamiento_burbuja(A) )
    A = np.random.rand(1,10000)
    inicio = time.time()
    A = A[0]
    print( ordenamiento_burbuja(A))
    fin = time.time()
    print(fin - inicio)