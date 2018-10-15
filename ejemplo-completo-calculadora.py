from interfaz_calculadora import *
import sys


app = QApplication(sys.argv)
mi_app = MiFormulario()
mi_app.show()
sys.exit(app.exec())