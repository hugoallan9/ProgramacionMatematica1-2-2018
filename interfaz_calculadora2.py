# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz_calculadora.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(532, 472)
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 30, 421, 83))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.editor = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.editor.setObjectName("editor")
        self.verticalLayout.addWidget(self.editor)
        self.gridLayoutWidget = QtWidgets.QWidget(Form)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(69, 149, 364, 251))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.buton_punto = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buton_punto.setObjectName("buton_punto")
        self.gridLayout.addWidget(self.buton_punto, 4, 2, 1, 1)
        self.boton_multiplicar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton_multiplicar.setObjectName("boton_multiplicar")
        self.gridLayout.addWidget(self.boton_multiplicar, 0, 1, 1, 1)
        self.boton9 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton9.setObjectName("boton9")
        self.gridLayout.addWidget(self.boton9, 1, 2, 1, 1)
        self.boton2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton2.setObjectName("boton2")
        self.gridLayout.addWidget(self.boton2, 3, 1, 1, 1)
        self.boton1 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton1.setObjectName("boton1")
        self.gridLayout.addWidget(self.boton1, 3, 0, 1, 1)
        self.boton7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton7.setObjectName("boton7")
        self.gridLayout.addWidget(self.boton7, 1, 0, 1, 1)
        self.boton3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton3.setObjectName("boton3")
        self.gridLayout.addWidget(self.boton3, 3, 2, 1, 1)
        self.boton8 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton8.setObjectName("boton8")
        self.gridLayout.addWidget(self.boton8, 1, 1, 1, 1)
        self.boton5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton5.setObjectName("boton5")
        self.gridLayout.addWidget(self.boton5, 2, 1, 1, 1)
        self.buton0 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.buton0.setObjectName("buton0")
        self.gridLayout.addWidget(self.buton0, 4, 0, 1, 2)
        self.boton_menos = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton_menos.setObjectName("boton_menos")
        self.gridLayout.addWidget(self.boton_menos, 0, 2, 1, 1)
        self.boton6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton6.setObjectName("boton6")
        self.gridLayout.addWidget(self.boton6, 2, 2, 1, 1)
        self.boton4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton4.setObjectName("boton4")
        self.gridLayout.addWidget(self.boton4, 2, 0, 1, 1)
        self.boton_dividir = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton_dividir.setObjectName("boton_dividir")
        self.gridLayout.addWidget(self.boton_dividir, 0, 0, 1, 1)
        self.boton_mas = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton_mas.setEnabled(True)
        self.boton_mas.setObjectName("boton_mas")
        self.gridLayout.addWidget(self.boton_mas, 0, 3, 2, 1)
        self.boton_calcular = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton_calcular.setObjectName("boton_calcular")
        self.gridLayout.addWidget(self.boton_calcular, 2, 3, 2, 1)
        self.boton_limpiar = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.boton_limpiar.setObjectName("boton_limpiar")
        self.gridLayout.addWidget(self.boton_limpiar, 4, 3, 1, 1)
        self.label_ultimaop = QtWidgets.QLabel(Form)
        self.label_ultimaop.setGeometry(QtCore.QRect(0, 450, 171, 16))
        self.label_ultimaop.setObjectName("label_ultimaop")

        self.retranslateUi(Form)
        self.boton_limpiar.clicked.connect(self.editor.clear)
        self.boton7.clicked.connect(self.editor.update)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.buton_punto.setText(_translate("Form", "."))
        self.boton_multiplicar.setText(_translate("Form", "*"))
        self.boton9.setText(_translate("Form", "9"))
        self.boton2.setText(_translate("Form", "2"))
        self.boton1.setText(_translate("Form", "1"))
        self.boton7.setText(_translate("Form", "7"))
        self.boton3.setText(_translate("Form", "3"))
        self.boton8.setText(_translate("Form", "8"))
        self.boton5.setText(_translate("Form", "5"))
        self.buton0.setText(_translate("Form", "0"))
        self.boton_menos.setText(_translate("Form", "-"))
        self.boton6.setText(_translate("Form", "6"))
        self.boton4.setText(_translate("Form", "4"))
        self.boton_dividir.setText(_translate("Form", "/"))
        self.boton_mas.setText(_translate("Form", "+"))
        self.boton_calcular.setText(_translate("Form", "Calcular"))
        self.boton_limpiar.setText(_translate("Form", "Limpiar"))
        self.label_ultimaop.setText(_translate("Form", "Última operación: "))

