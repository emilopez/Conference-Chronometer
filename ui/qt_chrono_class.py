from PyQt4 import QtGui, QtCore
import os
from ui import nico

class chrono(QtGui.QMainWindow, nico.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        # se crea la ventana principal vinculandola con la clase previa
        self.ventana = nico.Ui_MainWindow()
        self.ventana.setupUi(self)

        # Eventos GUI: pushButton clicked() -> self.putImage
        self.connect(self.ventana.CloseBtn,QtCore.SIGNAL("clicked()"),QtCore.QCoreApplication.instance().quit)
        self.connect(self.ventana.LaunchBtn,QtCore.SIGNAL("clicked()"),self.LaunchChrono)

    # Implementados
    def LaunchChrono(self):
        os.system("./chronometer.py 1")
