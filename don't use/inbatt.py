# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EP\Check_Cadet_2\inbatt.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector

class Ui_InbattWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 218)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.in_title = QtWidgets.QLabel(self.centralwidget)
        self.in_title.setGeometry(QtCore.QRect(30, 10, 141, 16))
        self.in_title.setObjectName("in_title")
        self.in_send = QtWidgets.QPushButton(self.centralwidget)
        self.in_send.setGeometry(QtCore.QRect(600, 70, 91, 41))
        self.in_send.setObjectName("in_send")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 40, 551, 98))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.sname_in = QtWidgets.QLabel(self.layoutWidget)
        self.sname_in.setObjectName("sname_in")
        self.gridLayout_2.addWidget(self.sname_in, 0, 2, 1, 1)
        self.uname_in = QtWidgets.QLabel(self.layoutWidget)
        self.uname_in.setObjectName("uname_in")
        self.gridLayout_2.addWidget(self.uname_in, 0, 1, 1, 1)
        self.ucom_in = QtWidgets.QLabel(self.layoutWidget)
        self.ucom_in.setObjectName("ucom_in")
        self.gridLayout_2.addWidget(self.ucom_in, 0, 3, 1, 1)
        self.uid_in = QtWidgets.QLabel(self.layoutWidget)
        self.uid_in.setObjectName("uid_in")
        self.gridLayout_2.addWidget(self.uid_in, 0, 0, 1, 1)
        self.uname_in_show = QtWidgets.QTextEdit(self.layoutWidget)
        self.uname_in_show.setObjectName("uname_in_show")
        self.gridLayout_2.addWidget(self.uname_in_show, 1, 1, 1, 1)
        self.uid_in_show = QtWidgets.QTextEdit(self.layoutWidget)
        self.uid_in_show.setObjectName("uid_in_show")
        self.gridLayout_2.addWidget(self.uid_in_show, 1, 0, 1, 1)
        self.sname_in_show = QtWidgets.QTextEdit(self.layoutWidget)
        self.sname_in_show.setObjectName("sname_in_show")
        self.gridLayout_2.addWidget(self.sname_in_show, 1, 2, 1, 1)
        self.ucom_in_show = QtWidgets.QTextEdit(self.layoutWidget)
        self.ucom_in_show.setObjectName("ucom_in_show")
        self.gridLayout_2.addWidget(self.ucom_in_show, 1, 3, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 707, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.in_title.setText(_translate("MainWindow", "?????????.????????????"))
        self.in_send.setText(_translate("MainWindow", "send"))
        self.sname_in.setText(_translate("MainWindow", "????????????"))
        self.uname_in.setText(_translate("MainWindow", "????????????"))
        self.ucom_in.setText(_translate("MainWindow", "?????????????????????"))
        self.uid_in.setText(_translate("MainWindow", "?????????????????????"))


        ### Click Button
        self.in_send.clicked.connect(self.clickin)
        
    def clickin(self):
        print("click in")
        id = self.uid_in_show.toPlainText()
        uname = self.uname_in_show.toPlainText()
        lname = self.sname_in_show.toPlainText()
        com = self.ucom_in_show.toPlainText()
        print(id + uname + lname + com)
        insertorup(id,uname,lname,com)
 

def ConnectorMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="12341234",
        database="testdb",
        # auth_plugin='mysql_native_password'
    )
    print('Connect Database Successful')
    return mydb

        
def insertorup(id,uname,lname,com):
    print(id,uname,lname,com)
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT * FROM batt WHERE id="{id}"'
    print("dump databasesuccess!!")
    print(sql)
    cur.execute(sql)
    myresult = cur.fetchall()
    
    print(myresult)
    if len(myresult) != 0 :
        print("send to inbatt fn")
        inbatt(id)
    else:
        print("send to insert fn")
        insertin(id, uname, lname, com)  
 
def inbatt(id):
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'UPDATE `batt` SET `stay`=1,`outc`=0 WHERE id="{id}"'
    print("Check in success!!")
    cur.execute(sql)
    db.commit()
    db.close()    
           
def insertin(id,uname,lname,com):
    print("insert in")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'INSERT INTO `batt`(`id`, `name`, `lname`, `com`, `stay`, `outc`) VALUES ({id},"{uname}","{lname}",{com},1,0);'
    print(sql)
    print("Insert into success!!")
    cur.execute(sql)
    db.commit()
    db.close()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InbattWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
