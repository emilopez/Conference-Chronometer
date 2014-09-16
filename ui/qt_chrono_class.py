# -*- encoding: utf8 -*-
from PyQt4 import QtGui, QtCore
import os
import nico
import json

class chrono(QtGui.QMainWindow, nico.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self,parent)
        self.ventana = nico.Ui_MainWindow()
        self.ventana.setupUi(self)

        # Load saved chronos
        self.chronos_fn = 'chronos.json'
        with open(self.chronos_fn) as json_data:
            self.chronos = json.load(json_data)
        for t in self.chronos.keys():
            self.ventana.SavedList.addItem(t+':'+str(self.chronos[t][0])+
            ','+str(self.chronos[t][1])+','+str(self.chronos[t][2]))

        # GUI events
        self.ventana.CloseBtn.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.ventana.LaunchBtn.clicked.connect(self.LaunchChrono)
        self.ventana.SaveBtn.clicked.connect(self.SaveChrono)
        self.ventana.SavedList.itemDoubleClicked.connect(self.LaunchChrono)
        #QtGui.QShortcut(QtGui.QKeySequence("F"), self.ventana.SavedList, self.LaunchChrono)
        QtGui.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Delete), self.ventana.SavedList, self.DelChrono)
        self.ventana.actionAbout.triggered.connect(self.ShowAbout)
        self.ventana.actionHelp.triggered.connect(self.ShowHelp)



    # Implementados
    def SaveChrono(self):
        green_time = self.ventana.GreenEdit.text()
        yellow_time = self.ventana.YellowEdit.text()
        red_time = self.ventana.RedEdit.text()
        chron_label = self.ventana.LabelEdit.text()
        ok = False
        try:
            int(green_time)
            int(yellow_time)
            int(red_time)
            ok = True
        except Exception:
            QtGui.QMessageBox.about(self, 'Error','Input can only be a number')

        if ok and chron_label not in list(self.chronos.keys()):
            self.ventana.SavedList.addItem(chron_label+':'+green_time+','+yellow_time+','+red_time)
            self.chronos[str(chron_label)]=[int(green_time),int(yellow_time),int(red_time)]

            # Save json files with chronos
            with open(self.chronos_fn, 'wb') as json_data:
                json.dump(self.chronos, json_data)


    def LaunchChrono(self):
        ok = False
        try:
            chron_label, color_times = self.ventana.SavedList.currentItem().text().split(':')
            g,y,r = color_times.split(',')
            ok = True
        except Exception:
            QtGui.QMessageBox.about(self, 'Error','Choose an item')
        if ok:
            os.system("./chronometer.py "+str(g)+' '+str(y)+' '+str(r))

    def DelChrono(self):
        '''
        Se invoca al presionar DEL sobre un item y
        elimina item seleccionado
        '''
        chron_label, color_times = self.ventana.SavedList.currentItem().text().split(':')
        del self.chronos[str(chron_label)]
        self.ventana.SavedList.takeItem(self.ventana.SavedList.currentRow())
        # Save json files with chronos
        with open(self.chronos_fn, 'wb') as json_data:
            json.dump(self.chronos, json_data)

    def ShowAbout(self):
        QtGui.QMessageBox.about(self, self.tr("About..."),
        self.tr("Project: https://github.com/emilopez/Conference-Chronometer \n\n"
                "GUI Author: Emiliano Lopez -  \n"
                "Email: emiliano [dot] lopez [at] gmail\n"
                "Version: 0.6 \n"
                "Last update: Sept 2014\n"
                "Original Project: http://rnt.cl/software/conference-chronometer/ \n"
                "License: Atribución-No Comercial-Licenciar Igual 2.0 Chile"))

    def ShowHelp(self):
        QtGui.QMessageBox.about(self, self.tr("About..."),
        self.tr("- Se debe ingresar el tiempo de progreso que durará cada color \n"
                "- La suma total de los tiempos es el tiempo total del cronómetro \n"
                "- Con Save, se agrega a la lista de cronómetros y queda almacenada \n"
                "- El reloj se lanza haciendo doble click sobre un cronómetro o bien \n"
                "   seleccionándolo y presionando el botón Launch Timer \n"
                "- Para eliminar una charla de la lista, se la selecciona y oprime DEL \n\n"
                " Mas ayuda en https://github.com/emilopez/Conference-Chronometer"))