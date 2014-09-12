from PyQt4 import QtGui, QtCore
import os
import nico

class chrono(QtGui.QMainWindow, nico.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.ventana = nico.Ui_MainWindow()
        self.ventana.setupUi(self)

        # GUI events
        self.ventana.CloseBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.ventana.LaunchBtn.clicked.connect(self.LaunchChrono)
        self.ventana.SaveBtn.clicked.connect(self.SaveChrono)
        self.ventana.SavedList.itemDoubleClicked.connect(self.LaunchChrono)

    # Implementados
    def SaveChrono(self):
        green_time = self.ventana.GreenEdit.text()
        yellow_time = self.ventana.YellowEdit.text()
        red_time = self.ventana.RedEdit.text()
        chron_label = self.ventana.LabelEdit.text()
        self.ventana.SavedList.addItem(chron_label+':'+green_time+','+yellow_time+','+red_time)

    def LaunchChrono(self):
        os.system("./chronometer.py 1")
