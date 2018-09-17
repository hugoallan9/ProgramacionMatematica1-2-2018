

class Persona():


    def __init__(self, CUI, nombre, apellido):
        self.CUI = CUI
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return "%s: %s, %s " % (str(self.CUI), self.apellido, self.nombre)


class Estudiante(Persona):

    def __init__(self,CUI, nombre, apellido, registro_personal, carrera):
        Persona.__init__(self,CUI,nombre, apellido)
        self.registro_personal = registro_personal
        self.carrera = carrera

    def inscribirse_en_curso(self, curso):
        print("El estudiante se ha inscrito en el curso ", curso)

    def __str__(self):
        return "%s: %s, %s, %s " % (str(self.registro_personal), self.apellido, self.nombre, self.carrera)


Flor = Estudiante(2521052340101, "Pérez", "Flor", 201314574,"Licenciatura en Matemática Aplicada")
Flor.inscribirse_en_curso("Programación Matemática 1")
print(Flor)

Luciano = Persona(2512053241307,"Luciano","Delgado")
print(Luciano)

