''' Manejo de ficheros en python
'''

import os

#Creando o abriendo un archivo en el wd con nombre clase11.txt y con permisos de escritura
mi_archivo = open("clase11.txt", "w")
mi_archivo.write("Esta es mi primera linea \n")
mi_archivo.write("Esta es la segunda linea \n")
#Es importante cerrar el archivo
mi_archivo.close()

#Abriendo el fichero con permisos de lectura
archivo = open("clase11.txt", "r")
#cadena_leida = archivo.read()
#print(cadena_leida[::-1])

print(os.path.abspath(__file__))

#Leyendo linea por linea
#print(  archivo.readline(5))
#print(  archivo.readline())
#print(  archivo.readline())

#read se puede emular con un ciclo

for line in archivo:
    print(line)



#Cerrando el archivo aunque solo sea de lectura
archivo.close()
