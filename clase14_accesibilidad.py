

class Prueba():


    def __init__(self):
        self.nombre_prueba = "Mi primera prueba"

    @staticmethod
    def _finalizar():
        print("Prueba concluida!!!!!!!")

    def _ingresar_pregunta(self,pregunta):
        print(pregunta)

    def imprimir(self):
        self._ingresar_pregunta("Hola Mundo")

Prueba._finalizar()




