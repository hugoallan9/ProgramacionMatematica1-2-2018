
from math import pi



class figuraGeometrica():

    def  area(self):
        pass

    def perimetro(self):
        pass

class circulo(figuraGeometrica):

    def __init__(self,radio):
        self.radio = radio

    def area(self):
        return  pi*self.radio**2

    def perimetro(self):
        return 2*pi*self.radio

class rectangulo(figuraGeometrica):

    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho

    def area(self):
        return  self.alto*self.ancho

    def perimetro(self):
        return 2*(self.alto + self.ancho)



c = circulo(2)
print(c.perimetro())
print(c.area())

rect = rectangulo(15,5)
print(rect.perimetro())
print(rect.area())




