

import sys
from PyQt5.QtCore import  Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox


class PrimeraInterfaz(QWidget):
    def __init__(self, parent = None):
        QWidget.__init__(self, parent = None)
        self.setGeometry(0,0,300,600)
        self.setWindowTitle("Mi primera ventana")
        salir = QPushButton("Salir", self)
        salir.setToolTip("Salir de la aplicación")
        salir.clicked.connect(self.closeEvent )
        salir.setGeometry(100,100,100,100)

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Salir",
                                     "Está seguro que quiere cerrar el programa?",
                                     QMessageBox.Save | QMessageBox.Cancel | QMessageBox.Close,
                                     QMessageBox.Save)

        if reply == QMessageBox.Cancel:
            print("No salir")
        else:
            self.close()


    def salir_al_presionar_escape(self,event):
        if event.key() == Qt.Key_Escape:
            self.close()





app = QApplication(sys.argv)
mi_app = PrimeraInterfaz()
mi_app.show()
sys.exit(app.exec())