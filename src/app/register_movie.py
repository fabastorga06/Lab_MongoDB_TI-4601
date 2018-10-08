# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_movie.ui'
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

class Ui_RegisterMovie(object):
    def setupUi(self, RegisterMovie):
        RegisterMovie.setObjectName(_fromUtf8("RegisterMovie"))
        RegisterMovie.resize(575, 512)
        self.centralwidget = QtGui.QWidget(RegisterMovie)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 191, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(100, 80, 60, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(370, 80, 60, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.name_data = QtGui.QLineEdit(self.centralwidget)
        self.name_data.setGeometry(QtCore.QRect(170, 70, 113, 33))
        self.name_data.setObjectName(_fromUtf8("name_data"))
        self.genre_data = QtGui.QLineEdit(self.centralwidget)
        self.genre_data.setGeometry(QtCore.QRect(170, 120, 113, 33))
        self.genre_data.setObjectName(_fromUtf8("genre_data"))
        self.director_data = QtGui.QLineEdit(self.centralwidget)
        self.director_data.setGeometry(QtCore.QRect(170, 170, 113, 33))
        self.director_data.setObjectName(_fromUtf8("director_data"))
        self.franchise_data = QtGui.QLineEdit(self.centralwidget)
        self.franchise_data.setGeometry(QtCore.QRect(170, 220, 113, 33))
        self.franchise_data.setObjectName(_fromUtf8("franchise_data"))
        self.country_data = QtGui.QLineEdit(self.centralwidget)
        self.country_data.setGeometry(QtCore.QRect(170, 270, 113, 33))
        self.country_data.setObjectName(_fromUtf8("country_data"))
        self.year_data = QtGui.QLineEdit(self.centralwidget)
        self.year_data.setGeometry(QtCore.QRect(170, 320, 113, 33))
        self.year_data.setObjectName(_fromUtf8("year_data"))
        self.duration_data = QtGui.QLineEdit(self.centralwidget)
        self.duration_data.setGeometry(QtCore.QRect(170, 370, 113, 33))
        self.duration_data.setObjectName(_fromUtf8("duration_data"))
        self.company_data = QtGui.QLineEdit(self.centralwidget)
        self.company_data.setGeometry(QtCore.QRect(170, 420, 113, 33))
        self.company_data.setObjectName(_fromUtf8("company_data"))
        self.actor1_data = QtGui.QLineEdit(self.centralwidget)
        self.actor1_data.setGeometry(QtCore.QRect(440, 100, 113, 33))
        self.actor1_data.setObjectName(_fromUtf8("actor1_data"))
        self.actor2_data = QtGui.QLineEdit(self.centralwidget)
        self.actor2_data.setGeometry(QtCore.QRect(440, 140, 113, 33))
        self.actor2_data.setObjectName(_fromUtf8("actor2_data"))
        self.actor3_data = QtGui.QLineEdit(self.centralwidget)
        self.actor3_data.setGeometry(QtCore.QRect(440, 180, 113, 33))
        self.actor3_data.setObjectName(_fromUtf8("actor3_data"))
        self.label_11 = QtGui.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(460, 350, 121, 101))
        self.label_11.setText(_fromUtf8(""))
        self.label_11.setPixmap(QtGui.QPixmap(_fromUtf8("design/mov.png")))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(100, 130, 60, 19))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(79, 180, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(69, 230, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 280, 71, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(110, 330, 51, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(70, 380, 81, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(70, 420, 91, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(14)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.register_button = QtGui.QPushButton(self.centralwidget)
        self.register_button.setGeometry(QtCore.QRect(380, 270, 121, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.register_button.setFont(font)
        self.register_button.setObjectName(_fromUtf8("register_button"))
        RegisterMovie.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(RegisterMovie)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 575, 31))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        RegisterMovie.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(RegisterMovie)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        RegisterMovie.setStatusBar(self.statusbar)
        self.main = None
        self.retranslateUi(RegisterMovie)
        QtCore.QMetaObject.connectSlotsByName(RegisterMovie)

    def retranslateUi(self, RegisterMovie):
        RegisterMovie.setWindowTitle(_translate("RegisterMovie", "Register new movie", None))
        self.label.setText(_translate("RegisterMovie", "Register Movie:", None))
        self.label_2.setText(_translate("RegisterMovie", "Name:", None))
        self.label_10.setText(_translate("RegisterMovie", "Actors:", None))
        self.label_3.setText(_translate("RegisterMovie", "Genre:", None))
        self.label_4.setText(_translate("RegisterMovie", "Director:", None))
        self.label_5.setText(_translate("RegisterMovie", "Franchise:", None))
        self.label_6.setText(_translate("RegisterMovie", "Country:", None))
        self.label_7.setText(_translate("RegisterMovie", "Year:", None))
        self.label_8.setText(_translate("RegisterMovie", "Duration:", None))
        self.label_9.setText(_translate("RegisterMovie", "Company:", None))
        self.register_button.setText(_translate("RegisterMovie", "Register", None))
        self.register_button.clicked.connect(lambda: self.send_register_movie(RegisterMovie) )

    def set_main_module(self, pmodule):
        self.main = pmodule

    def fill_json(self):
        movie_json["name"] = unicode( self.name_data.text() )
        movie_json["genre"] = unicode( self.genre_data.text() )
        movie_json["director_name"] = unicode( self.director_data.text() )
        movie_json["franchise"] = unicode( self.franchise_data.text() )
        movie_json["country"] = unicode( self.country_data.text() )
        movie_json["year"] = int( self.year_data.text() )
        movie_json["duration"] = float( self.duration_data.text() )
        movie_json["company"] = unicode( self.company_data.text() )
        movie_json["actors"][0]["name"] = unicode(self.actor1_data.text() )
        movie_json["actors"][1]["name"] = unicode(self.actor2_data.text() )
        movie_json["actors"][2]["name"] = unicode(self.actor3_data.text() )

    def send_register_movie(self, module):
        if (self.name_data.text().isEmpty() or self.genre_data.text().isEmpty() or self.director_data.text().isEmpty() or
        self.country_data.text().isEmpty() or self.year_data.text().isEmpty() or self.duration_data.text().isEmpty() or
        self.company_data.text().isEmpty() or self.actor1_data.text().isEmpty() or self.actor2_data.text().isEmpty() or
        self.actor3_data.text().isEmpty()):
            show_message("Please insert the required information", "Warning", False)
        else:
            self.fill_json()
            insert_document(movie_json, "movies") 
            show_message("Movie has been registered successfully!", "Done", True)
            self.main.fill_tabs( self.main.franchises, self.main.franchise_data, 1 )
            module.hide()  
           

