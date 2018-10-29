# Lectura y escritura de un archivo json

import json
from pprint import  pprint


with open("maps.json", "r") as archivo:
    datos = json.load(archivo)

pprint(datos)

print(datos["markers"][2]["name"])


# Escribiendo un archivo json de notas de estudiantes con campos
# nombre
# Carnet
# Nota
# Curso


# Definicion de la estructura de datos
notas_curso = {'notas': [ {"nombre": "Flor Pérez",
                           "carnet": "201314574",
                           "nota": 100,
                           "curso": "Programación Matemática 1"
                           },
                          {
                           "nombre": "Mack Gay",
                           "carnet": "201314574",
                           "nota": 98,
                           "curso": "Programación Matemática 1"
                          }
                          ] }

with open("notas.json", "w") as archivo:
    json.dump(notas_curso, archivo)