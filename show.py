# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\EP\Check_Cadet_2\show.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector


class Ui_ShowWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(707, 217)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(90, 50, 631, 131))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.com1_title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.com1_title.setObjectName("com1_title")
        self.verticalLayout.addWidget(self.com1_title)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.all1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.all1.setObjectName("all1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.all1)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.active1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.active1.setObjectName("active1")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.active1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.remain1 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.remain1.setObjectName("remain1")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.remain1)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.com2_title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.com2_title.setObjectName("com2_title")
        self.verticalLayout_2.addWidget(self.com2_title)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.all2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.all2.setObjectName("all2")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.all2)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.active2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.active2.setObjectName("active2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.active2)
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.remain2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.remain2.setObjectName("remain2")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.remain2)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.com3_title = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.com3_title.setObjectName("com3_title")
        self.verticalLayout_3.addWidget(self.com3_title)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_11 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.all3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.all3.setObjectName("all3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.all3)
        self.label_12 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.active3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.active3.setObjectName("active3")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.active3)
        self.label_13 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.remain3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.remain3.setObjectName("remain3")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.remain3)
        self.verticalLayout_3.addLayout(self.formLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
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
        self.com1_title.setText(_translate("MainWindow", "ร้อย 1"))
        self.label_2.setText(_translate("MainWindow", "ยอดเดิม"))
        self.label_3.setText(_translate("MainWindow", "จำหน่าย"))
        self.label_4.setText(_translate("MainWindow", "คงเหลือ"))
        self.com2_title.setText(_translate("MainWindow", "ร้อย 2"))
        self.label_7.setText(_translate("MainWindow", "ยอดเดิม"))
        self.label_8.setText(_translate("MainWindow", "จำหน่าย"))
        self.label_9.setText(_translate("MainWindow", "คงเหลือ"))
        self.com3_title.setText(_translate("MainWindow", "ร้อย 3"))
        self.label_11.setText(_translate("MainWindow", "ยอดเดิม"))
        self.label_12.setText(_translate("MainWindow", "จำหน่าย"))
        self.label_13.setText(_translate("MainWindow", "คงเหลือ"))

    # Show data Company 1
        # Done
        self.all1.setPlaceholderText(com1all())
        self.active1.setPlaceholderText(com1out())
        self.remain1.setPlaceholderText(com1remain())

    # Show data Company 2
        # Done
        self.all2.setPlaceholderText(com2all())
        self.active2.setPlaceholderText(com2out())
        self.remain2.setPlaceholderText(com2remain())

    # Show data Company 3
        # Done
        self.all3.setPlaceholderText(com3all())
        self.active3.setPlaceholderText(com3out())
        self.remain3.setPlaceholderText(com3remain())
        
def ConnectorMysql():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="cadet",
        # auth_plugin='mysql_native_password'
    )
    print('Connect Database Successful')
    return mydb        

def com1all():
    print("com1 all")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay+outc) FROM `batt` WHERE com=1'
    print("com1_all success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com1stay():
    print("com1 stay")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay) FROM `batt` WHERE com=1'
    print("com1_stay success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com1out():
    print("com1 out")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(outc) FROM `batt` WHERE com=1'
    print("com1_out success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com1remain():
    print("com1 remain")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay) FROM `batt` WHERE com=1'
    print("com1_remain success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com2all():
    print("com2 all")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay+outc) FROM `batt` WHERE com=2'
    print("com2_all success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com2stay():
    print("com2 stay")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay) FROM `batt` WHERE com=2'
    print("com2_stay success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com2out():
    print("com2 out")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(outc) FROM `batt` WHERE com=2'
    print("com2_out success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com2remain():
    print("com2 remain")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay) FROM `batt` WHERE com=2'
    print("com2_remain success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com3all():
    print("com3 all")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay+outc) FROM `batt` WHERE com=3'
    print("com3_all success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com3stay():
    print("com3 stay")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay) FROM `batt` WHERE com=3'
    print("com3_stay success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com3out():
    print("com3 out")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(outc) FROM `batt` WHERE com=3'
    print("com3_out success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x

def com3remain():
    print("com3 remain")
    db = ConnectorMysql()
    cur = db.cursor()
    sql = f'SELECT SUM(stay) FROM `batt` WHERE com=3'
    print("com3_remain success!!")
    cur.execute(sql)
    myresult = cur.fetchall()
    x = str(myresult[0][0])
    return x        
        
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ShowWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
