# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EP\Check_Cadet_2\ui\menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from inbatt import Ui_InbattWindow
from outbatt import Ui_OutbattWindow
from show import Ui_ShowWindow

class Ui_MenwWindow(object):
    def openinbatt(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InbattWindow()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()
        
    def openoutbatt(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_OutbattWindow()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()
 

    def openshowbatt(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ShowWindow()
        self.ui.setupUi(self.window)
        # MainWindow.hide()
        self.window.show()    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(470, 375)
        MainWindow.setStyleSheet("background-color: rgb(255, 98, 98);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(190, 90, 87, 147))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.button_inbatt = QtWidgets.QPushButton(self.layoutWidget)
        self.button_inbatt.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.button_inbatt.setObjectName("button_inbatt")
        self.gridLayout.addWidget(self.button_inbatt, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.button_outbatt = QtWidgets.QPushButton(self.layoutWidget)
        self.button_outbatt.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.button_outbatt.setObjectName("button_outbatt")
        self.gridLayout.addWidget(self.button_outbatt, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 0, 1, 1)
        self.button_show = QtWidgets.QPushButton(self.layoutWidget)
        self.button_show.setStyleSheet("background-color: rgb(255, 255, 0);")
        self.button_show.setObjectName("button_show")
        self.gridLayout.addWidget(self.button_show, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 470, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.button_inbatt.clicked.connect(self.openinbatt)
        self.button_outbatt.clicked.connect(self.openoutbatt)
        self.button_show.clicked.connect(self.openshowbatt)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button_inbatt.setText(_translate("MainWindow", "??????????????????????????????"))
        self.button_outbatt.setText(_translate("MainWindow", "???????????????????????????"))
        self.button_show.setText(_translate("MainWindow", "?????????????????????"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MenwWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())