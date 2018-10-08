# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_company.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from message import *
from data_handler import *
from controller import *

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

class Ui_RegisterCompany(object):
    def setupUi(self, RegisterCompany):
        RegisterCompany.setObjectName(_fromUtf8("RegisterCompany"))
        RegisterCompany.resize(530, 286)
        self.centralwidget = QtGui.QWidget(RegisterCompany)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(110, 70, 61, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 120, 51, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 180, 241, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.name_data = QtGui.QLineEdit(self.centralwidget)
        self.name_data.setGeometry(QtCore.QRect(190, 80, 113, 33))
        self.name_data.setObjectName(_fromUtf8("name_data"))
        self.year_data = QtGui.QLineEdit(self.centralwidget)
        self.year_data.setGeometry(QtCore.QRect(190, 130, 113, 33))
        self.year_data.setObjectName(_fromUtf8("year_data"))
        self.address_data = QtGui.QLineEdit(self.centralwidget)
        self.address_data.setGeometry(QtCore.QRect(190, 190, 113, 31))
        self.address_data.setObjectName(_fromUtf8("address_data"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 140, 101, 101))
        self.label_5.setText(_fromUtf8(""))
        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8("design/comp.png")))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.register_button = QtGui.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(370, 80, 121, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.register_button.setFont(font)
        self.register_button.setObjectName(_fromUtf8("register_button"))
        RegisterCompany.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RegisterCompany)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 530, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RegisterCompany.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RegisterCompany)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RegisterCompany.setStatusBar(self.statusbar)
        self.main = None
        self.retranslateUi(RegisterCompany)
        QtCore.QMetaObject.connectSlotsByName(RegisterCompany)

    def retranslateUi(self, RegisterCompany):
        RegisterCompany.setWindowTitle(_translate("RegisterCompany", "Register new company", None))
        self.label.setText(_translate("RegisterCompany", "Register company:", None))
        self.label_2.setText(_translate("RegisterCompany", "Name:", None))
        self.label_3.setText(_translate("RegisterCompany", "Year:", None))
        self.label_4.setText(_translate("RegisterCompany", "Web Address:", None))
        self.register_button.setText(_translate("RegisterCompany", "Register", None))
        self.register_button.clicked.connect(lambda: self.send_register_company(RegisterCompany) )

    def set_main_module(self, pmodule):
        self.main = pmodule

    def fill_json(self):
        company_json["name"] = unicode( self.name_data.text() )
        company_json["year"] = int( self.year_data.text() )
        company_json["web_address"] = unicode( self.address_data.text() )

    def send_register_company(self, module):
        if (self.name_data.text().isEmpty() or self.year_data.text().isEmpty() or 
        self.address_data.text().isEmpty()):            
            show_message("Please insert the required information", "Warning", False)
        else:
            self.fill_json()
            insert_document(company_json, "companies") 
            show_message("User has been registered successfully!", "Done", True)
            self.main.fill_tabs( self.main.companies, self.main.producer_data, 0 )
            module.hide()  
           

