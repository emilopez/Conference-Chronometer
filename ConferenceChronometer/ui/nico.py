# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nico.ui'
#
# Created: Tue Sep 16 01:40:30 2014
#      by: PyQt4 UI code generator 4.11.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(428, 264)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.SaveBtn = QtGui.QPushButton(self.centralwidget)
        self.SaveBtn.setGeometry(QtCore.QRect(78, 155, 111, 21))
        self.SaveBtn.setObjectName(_fromUtf8("SaveBtn"))
        self.GreenEdit = QtGui.QLineEdit(self.centralwidget)
        self.GreenEdit.setGeometry(QtCore.QRect(78, 35, 113, 20))
        self.GreenEdit.setObjectName(_fromUtf8("GreenEdit"))
        self.YellowEdit = QtGui.QLineEdit(self.centralwidget)
        self.YellowEdit.setGeometry(QtCore.QRect(78, 65, 113, 20))
        self.YellowEdit.setObjectName(_fromUtf8("YellowEdit"))
        self.RedEdit = QtGui.QLineEdit(self.centralwidget)
        self.RedEdit.setGeometry(QtCore.QRect(78, 95, 113, 20))
        self.RedEdit.setObjectName(_fromUtf8("RedEdit"))
        self.LabelEdit = QtGui.QLineEdit(self.centralwidget)
        self.LabelEdit.setGeometry(QtCore.QRect(78, 125, 113, 20))
        self.LabelEdit.setObjectName(_fromUtf8("LabelEdit"))
        self.LaunchBtn = QtGui.QPushButton(self.centralwidget)
        self.LaunchBtn.setGeometry(QtCore.QRect(228, 191, 91, 24))
        self.LaunchBtn.setObjectName(_fromUtf8("LaunchBtn"))
        self.SavedList = QtGui.QListWidget(self.centralwidget)
        self.SavedList.setGeometry(QtCore.QRect(228, 35, 181, 141))
        self.SavedList.setObjectName(_fromUtf8("SavedList"))
        self.CloseBtn = QtGui.QPushButton(self.centralwidget)
        self.CloseBtn.setGeometry(QtCore.QRect(328, 191, 83, 24))
        self.CloseBtn.setObjectName(_fromUtf8("CloseBtn"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(28, 35, 41, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(28, 65, 41, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(28, 95, 31, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(28, 125, 41, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 7, 101, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 7, 101, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 428, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName(_fromUtf8("menuAbout"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setObjectName(_fromUtf8("actionHelp"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.GreenEdit, self.YellowEdit)
        MainWindow.setTabOrder(self.YellowEdit, self.RedEdit)
        MainWindow.setTabOrder(self.RedEdit, self.LabelEdit)
        MainWindow.setTabOrder(self.LabelEdit, self.SaveBtn)
        MainWindow.setTabOrder(self.SaveBtn, self.SavedList)
        MainWindow.setTabOrder(self.SavedList, self.LaunchBtn)
        MainWindow.setTabOrder(self.LaunchBtn, self.CloseBtn)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.SaveBtn.setText(_translate("MainWindow", "Save", None))
        self.LaunchBtn.setText(_translate("MainWindow", "Launch Timer", None))
        self.CloseBtn.setText(_translate("MainWindow", "Close", None))
        self.label.setText(_translate("MainWindow", "Green", None))
        self.label_2.setText(_translate("MainWindow", "Yellow", None))
        self.label_3.setText(_translate("MainWindow", "Red", None))
        self.label_4.setText(_translate("MainWindow", "Label", None))
        self.label_5.setText(_translate("MainWindow", "Time Settings", None))
        self.label_6.setText(_translate("MainWindow", "Saved Timers", None))
        self.menuAbout.setTitle(_translate("MainWindow", "Help", None))
        self.actionHelp.setText(_translate("MainWindow", "Help", None))
        self.actionAbout.setText(_translate("MainWindow", "About", None))

