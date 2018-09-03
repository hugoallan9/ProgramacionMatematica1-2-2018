#-*-coding:utf8-*-
''' Creación de una clase en python. 
Uso de palabras reservadas e instancias'''


# Definición de clase
class escritorio():

    #Definición del constructor se debe llamar __init__
    def __init__(self,color, altura, numero_patas, orientacion = "diestro"):
        self.color = color
        self.orientacion = orientacion
        self.altura = altura
        self.numero_patas = numero_patas

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    @staticmethod
    def quebrar():
        print("Me quebré")

    def mover(self, x,y):
        print(x)
        print(y)

    def recibir_objeto(self, x):
        print("Se sentó en mí el objeto " ,  x)


class Persona():


    def __init__(self, nombre):
        self.nombre = nombre

    def get_name(self):
        return self.nombre


#Instanciar la clase -crear un objeto de la clase -
escritorio_azul = escritorio(color = "azul",
altura = "100", numero_patas = 2)
print( escritorio_azul.get_color() )
escritorio_azul.set_color("verde")
print( escritorio_azul.get_color() )
escritorio_azul.color = "rojo"
print( escritorio_azul.color )
escritorio_azul.quebrar()
escritorio.quebrar()
escritorio_azul.mover(10,10)
escritorio_azul.recibir_objeto("Pedro")
pedro = Persona("Peter")
escritorio_azul.recibir_objeto(pedro.get_name())



