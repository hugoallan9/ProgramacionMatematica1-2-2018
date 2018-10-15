

'''Implementación de un hilo sencillo
donde se hacen conteos de números '''

import threading

def conteo():
    i = 0
    while( i <= 10):
        print('Hilo: ', threading.current_thread().getName(),
              'con identificador: ', threading.current_thread().ident,
              'contador: ', i)
        i = i + 1



hilo1 = threading.Thread(target= conteo)
hilo2 = threading.Thread(target= conteo)
#Llama al método start para comenzar el hilo
hilo1.start()
hilo2.start()