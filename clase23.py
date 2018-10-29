import pickle

#crear y guardar archivo en binario

archivo  = open('texto_en_binario', 'wb')
archivo.write(b'Texto que se debera escribir en binario')
archivo.close()

archivo_nuevo = open('texto_en_binario', "rb")
print( archivo_nuevo.readline() )


#Serializar objetos arbitrarios

class Pizarron():


    def __init__(self):
        self.largo = 15
        self.alto = 35
        self.color = "blanco"
        self.texto = ""

    def escribir(self, texto):
        self.texto = self.texto + texto

    def leer(self):
        return self.texto

    def borrar(self):
        self.texto = ""


clase304 = Pizarron()
clase304.escribir("María es profesora de la ECFM")
vaciado_clase304 = pickle.dumps(clase304)
print(vaciado_clase304)
print( pickle.loads(vaciado_clase304))

archivo_binario = open("archivo_binario.bin", mode= 'wb')
vaciado_clase304 = pickle.dump(clase304, archivo_binario)
archivo_binario.close()

recuperacion_pizarron = pickle.load( open('archivo_binario.bin', 'rb') )
print( recuperacion_pizarron.leer() )
recuperacion_pizarron.escribir("Luciano es alumno de la ECFM")
print( recuperacion_pizarron.leer() )
