# -*- coding: utf-8 -*-
from PyQt4 import QtCore, QtGui
import sys
from register_movie import *
from register_company import *
from controller import *
from message import *
from data_handler import *

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

class Ui_MovieModule(QtGui.QWidget):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

    def setupUi(self, MovieModule):
        MovieModule.setObjectName(_fromUtf8("MovieModule"))
        MovieModule.resize(945, 671)
        self.label_logo = QtGui.QLabel(MovieModule)
        self.label_logo.setGeometry(QtCore.QRect(10, 20, 281, 61))
        self.label_logo.setText(_fromUtf8(""))
        self.label_logo.setPixmap(QtGui.QPixmap(_fromUtf8("design/logo.png")))
        self.label_logo.setObjectName(_fromUtf8("label_logo"))
        self.label_movie_title = QtGui.QLabel(MovieModule)
        self.label_movie_title.setGeometry(QtCore.QRect(30, 110, 91, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.label_movie_title.setFont(font)
        self.label_movie_title.setObjectName(_fromUtf8("label_movie_title"))
        self.label_franchise = QtGui.QLabel(MovieModule)
        self.label_franchise.setGeometry(QtCore.QRect(30, 160, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.label_franchise.setFont(font)
        self.label_franchise.setObjectName(_fromUtf8("label_franchise"))
        self.label_among_movies = QtGui.QLabel(MovieModule)
        self.label_among_movies.setGeometry(QtCore.QRect(30, 230, 411, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.label_among_movies.setFont(font)
        self.label_among_movies.setObjectName(_fromUtf8("label_among_movies"))
        self.movie_data = QtGui.QLineEdit(MovieModule)
        self.movie_data.setGeometry(QtCore.QRect(130, 100, 251, 33))
        self.movie_data.setObjectName(_fromUtf8("movie_data"))
        self.start_year_data = QtGui.QLineEdit(MovieModule)
        self.start_year_data.setGeometry(QtCore.QRect(150, 220, 91, 31))
        self.start_year_data.setObjectName(_fromUtf8("start_year_data"))
        self.final_year_data = QtGui.QLineEdit(MovieModule)
        self.final_year_data.setGeometry(QtCore.QRect(290, 220, 91, 31))
        self.final_year_data.setObjectName(_fromUtf8("final_year_data"))
        self.franchise_data = QtGui.QComboBox(MovieModule)
        self.franchise_data.setGeometry(QtCore.QRect(120, 160, 171, 33))
        self.franchise_data.setObjectName(_fromUtf8("franchise_data"))
        
        self.movie_button = QtGui.QPushButton(MovieModule)
        self.movie_button.setGeometry(QtCore.QRect(400, 100, 121, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.movie_button.setFont(font)
        self.movie_button.setObjectName(_fromUtf8("movie_button"))
        self.franchise_button = QtGui.QPushButton(MovieModule)
        self.franchise_button.setGeometry(QtCore.QRect(400, 160, 121, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.franchise_button.setFont(font)
        self.franchise_button.setObjectName(_fromUtf8("franchise_button"))
        self.movies_among_years_data = QtGui.QPushButton(MovieModule)
        self.movies_among_years_data.setGeometry(QtCore.QRect(400, 220, 121, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.movies_among_years_data.setFont(font)
        self.movies_among_years_data.setObjectName(_fromUtf8("movies_among_years_data"))
        self.label_producer = QtGui.QLabel(MovieModule)
        self.label_producer.setGeometry(QtCore.QRect(620, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.label_producer.setFont(font)
        self.label_producer.setObjectName(_fromUtf8("label_producer"))
        self.producer_data = QtGui.QComboBox(MovieModule)
        self.producer_data.setGeometry(QtCore.QRect(700, 90, 211, 33))
        self.producer_data.setObjectName(_fromUtf8("producer_data"))
        
        self.movies_producer_button = QtGui.QPushButton(MovieModule)
        self.movies_producer_button.setGeometry(QtCore.QRect(770, 130, 141, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.movies_producer_button.setFont(font)
        self.movies_producer_button.setObjectName(_fromUtf8("movies_producer_button"))
        self.movies_table = QtGui.QTableWidget(MovieModule)
        self.movies_table.setGeometry(QtCore.QRect(30, 270, 521, 211))
        self.movies_table.setObjectName(_fromUtf8("movies_table"))
        self.movies_table.setColumnCount(9)
        self.movies_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.movies_table.setHorizontalHeaderItem(8, item)
        self.movies_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.movies_table.setDragDropOverwriteMode(False)
        self.movies_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.movies_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.movies_table.setWordWrap(False)
        self.movies_table.setSortingEnabled(False)
        self.movies_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|
                                                                          QtCore.Qt.AlignVCenter|
                                                                          QtCore.Qt.AlignCenter)
        self.movies_table.horizontalHeader().setHighlightSections(False)
        self.movies_table.horizontalHeader().setStretchLastSection(True)
        self.movies_table.verticalHeader().setVisible(False)
        self.movies_table.setAlternatingRowColors(True)
        self.movies_table.verticalHeader().setDefaultSectionSize(20)
        self.movies_producer_table = QtGui.QTableWidget(MovieModule)
        self.movies_producer_table.setGeometry(QtCore.QRect(620, 170, 301, 141))
        self.movies_producer_table.setObjectName(_fromUtf8("movies_producer_table"))
        self.movies_producer_table.setColumnCount(3)
        self.movies_producer_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.movies_producer_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.movies_producer_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.movies_producer_table.setHorizontalHeaderItem(2, item)
        self.movies_producer_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.movies_producer_table.setDragDropOverwriteMode(False)
        self.movies_producer_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.movies_producer_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.movies_producer_table.setWordWrap(False)
        self.movies_producer_table.setSortingEnabled(False)
        self.movies_producer_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|
                                                                          QtCore.Qt.AlignVCenter|
                                                                          QtCore.Qt.AlignCenter)
        self.movies_producer_table.horizontalHeader().setHighlightSections(False)
        self.movies_producer_table.horizontalHeader().setStretchLastSection(True)
        self.movies_producer_table.verticalHeader().setVisible(False)
        self.movies_producer_table.setAlternatingRowColors(True)
        self.movies_producer_table.verticalHeader().setDefaultSectionSize(20)

        self.avg_producer_table = QtGui.QTableWidget(MovieModule)
        self.avg_producer_table.setGeometry(QtCore.QRect(710, 420, 201, 231))
        self.avg_producer_table.setObjectName(_fromUtf8("avg_producer_table"))
        self.avg_producer_table.setColumnCount(2)
        self.avg_producer_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.avg_producer_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.avg_producer_table.setHorizontalHeaderItem(1, item)
        self.avg_producer_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.avg_producer_table.setDragDropOverwriteMode(False)
        self.avg_producer_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.avg_producer_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.avg_producer_table.setWordWrap(False)
        self.avg_producer_table.setSortingEnabled(False)
        self.avg_producer_table.horizontalHeader().setDefaultAlignment(QtCore.Qt.AlignHCenter|
                                                                          QtCore.Qt.AlignVCenter|
                                                                          QtCore.Qt.AlignCenter)
        self.avg_producer_table.horizontalHeader().setHighlightSections(False)
        self.avg_producer_table.horizontalHeader().setStretchLastSection(True)
        self.avg_producer_table.verticalHeader().setVisible(False)
        self.avg_producer_table.setAlternatingRowColors(True)
        self.avg_producer_table.verticalHeader().setDefaultSectionSize(20)

        self.label_average = QtGui.QLabel(MovieModule)
        self.label_average.setGeometry(QtCore.QRect(630, 340, 131, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.label_average.setFont(font)
        self.label_average.setObjectName(_fromUtf8("label_average"))
        self.avg_duration_producer_button = QtGui.QPushButton(MovieModule)
        self.avg_duration_producer_button.setGeometry(QtCore.QRect(770, 380, 141, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.avg_duration_producer_button.setFont(font)
        self.avg_duration_producer_button.setObjectName(_fromUtf8("avg_duration_producer_button"))
        self.line = QtGui.QLabel(MovieModule)
        self.line.setGeometry(QtCore.QRect(30, 490, 541, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.line.setFont(font)
        self.line.setObjectName(_fromUtf8("line"))
        self.less_duration_button = QtGui.QPushButton(MovieModule)
        self.less_duration_button.setGeometry(QtCore.QRect(30, 540, 131, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.less_duration_button.setFont(font)
        self.less_duration_button.setObjectName(_fromUtf8("less_duration_button"))
        self.high_duration_button = QtGui.QPushButton(MovieModule)
        self.high_duration_button.setGeometry(QtCore.QRect(30, 590, 131, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.high_duration_button.setFont(font)
        self.high_duration_button.setObjectName(_fromUtf8("high_duration_button"))
        self.amount_movies_button = QtGui.QPushButton(MovieModule)
        self.amount_movies_button.setGeometry(QtCore.QRect(410, 540, 131, 35))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu"))
        font.setPointSize(12)
        self.amount_movies_button.setFont(font)
        self.amount_movies_button.setObjectName(_fromUtf8("amount_movies_button"))
        self.amount_movies_data = QtGui.QLineEdit(MovieModule)
        self.amount_movies_data.setGeometry(QtCore.QRect(470, 580, 71, 41))
        self.amount_movies_data.setObjectName(_fromUtf8("amount_movies_data"))
        self.amount_movies_data.setReadOnly(True)
        self.high_duration_data = QtGui.QLineEdit(MovieModule)
        self.high_duration_data.setGeometry(QtCore.QRect(170, 590, 171, 41))
        self.high_duration_data.setObjectName(_fromUtf8("high_duration_data"))
        self.high_duration_data.setReadOnly(True)
        self.less_duration_data = QtGui.QLineEdit(MovieModule)
        self.less_duration_data.setGeometry(QtCore.QRect(170, 540, 171, 41))
        self.less_duration_data.setObjectName(_fromUtf8("less_duration_data"))
        self.less_duration_data.setReadOnly(True)
        self.register_button = QtGui.QPushButton(MovieModule)
        self.register_button.setGeometry(QtCore.QRect(625, 20, 130, 35))
        self.register_button.setFont(font)
        self.register_button.setObjectName(_fromUtf8("register_button"))
        self.company_button = QtGui.QPushButton(MovieModule)
        self.company_button.setGeometry(QtCore.QRect(750, 20, 150, 35))
        self.company_button.setFont(font)
        self.company_button.setObjectName(_fromUtf8("company_button"))
        self.franchises = None
        self.companies = None
        self.fill_tabs(self.franchises, self.franchise_data, 1)
        self.fill_tabs(self.companies, self.producer_data, 0)
        self.retranslateUi(MovieModule)
        QtCore.QMetaObject.connectSlotsByName(MovieModule)
    
    def fill_tabs(self, pdata, pthing, pflag):
        if (pflag):
            _franchises = ask_field("movies", "franchise")
            arr_franchises = serialize_data(_franchises, "franchise")
            pdata = order_array(arr_franchises)
        else:
            _companies = ask_field("companies", "name")
            pdata = serialize_data(_companies, "name")
        pthing.clear()
        for i in range( len(pdata) ):            
            pthing.addItem(_fromUtf8(""))
            pthing.setItemText(i, _translate("MovieModule", pdata[i], None))

    def retranslateUi(self, MovieModule):
        MovieModule.setWindowTitle(_translate("MovieModule", "Movieland", None))
        self.label_movie_title.setText(_translate("MovieModule", "Movie Title:", None))
        self.label_franchise.setText(_translate("MovieModule", "Franchise:", None))
        self.label_among_movies.setText(_translate("MovieModule", "Movies among                                and                               ", None))
        self.movie_button.setText(_translate("MovieModule", "Consult", None))
        self.register_button.setText(_translate("MovieModule", "Register Movie", None))
        self.company_button.setText(_translate("MovieModule", "Register Company", None))
        self.franchise_button.setText(_translate("MovieModule", "Consult", None))
        self.movies_among_years_data.setText(_translate("MovieModule", "Consult", None))
        self.label_producer.setText(_translate("MovieModule", "Producer:", None))
        self.movies_producer_button.setText(_translate("MovieModule", "Consult", None))
        item = self.movies_table.horizontalHeaderItem(0)
        item.setText(_translate("MovieModule", "NAME", None))
        item = self.movies_table.horizontalHeaderItem(1)
        item.setText(_translate("MovieModule", "GENRE", None))
        item = self.movies_table.horizontalHeaderItem(2)
        item.setText(_translate("MovieModule", "DIRECTOR", None))
        item = self.movies_table.horizontalHeaderItem(3)
        item.setText(_translate("MovieModule", "FRANCHISE", None))
        item = self.movies_table.horizontalHeaderItem(4)
        item.setText(_translate("MovieModule", "COUNTRY", None))
        item = self.movies_table.horizontalHeaderItem(5)
        item.setText(_translate("MovieModule", "YEAR", None))
        item = self.movies_table.horizontalHeaderItem(6)
        item.setText(_translate("MovieModule", "DURATION(min)", None))
        item = self.movies_table.horizontalHeaderItem(7)
        item.setText(_translate("MovieModule", "COMPANY", None))
        item = self.movies_table.horizontalHeaderItem(8)
        item.setText(_translate("MovieModule", "ACTORS", None))
        item = self.movies_producer_table.horizontalHeaderItem(0)
        item.setText(_translate("MovieModule", "NAME", None))
        item = self.movies_producer_table.horizontalHeaderItem(1)
        item.setText(_translate("MovieModule", "GENRE", None))
        item = self.movies_producer_table.horizontalHeaderItem(2)
        item.setText(_translate("MovieModule", "YEAR", None))
        item = self.avg_producer_table.horizontalHeaderItem(0)
        item.setText(_translate("MovieModule", "PRODUCER", None))
        item = self.avg_producer_table.horizontalHeaderItem(1)
        item.setText(_translate("MovieModule", "AVERAGE", None))
        self.label_average.setText(_translate("MovieModule", "Average Duration:", None))
        self.avg_duration_producer_button.setText(_translate("MovieModule", "Consult", None))
        self.line.setText(_translate("MovieModule", "_________________________________________________________________", None))
        self.less_duration_button.setText(_translate("MovieModule", "Less Duration", None))
        self.high_duration_button.setText(_translate("MovieModule", "High Duration", None))
        self.amount_movies_button.setText(_translate("MovieModule", "Amount Movies", None))
        self.movie_button.clicked.connect(self.ask_movie_data)
        self.franchise_button.clicked.connect(self.ask_movies_per_franchise)
        self.movies_among_years_data.clicked.connect(self.ask_movies_among_years)
        self.movies_producer_button.clicked.connect(self.ask_movies_producer)
        self.less_duration_button.clicked.connect(self.ask_less_movie)
        self.high_duration_button.clicked.connect(self.ask_high_movie)
        self.amount_movies_button.clicked.connect(self.ask_amount_movies)
        self.avg_duration_producer_button.clicked.connect(self.ask_averages)
        self.register_button.clicked.connect(lambda: self.register_screen(Ui_RegisterMovie(), MovieModule) )
        self.company_button.clicked.connect(lambda: self.register_screen(Ui_RegisterCompany(), MovieModule) )

    def register_screen(self, pscreen, pmain):
        self.window = QtGui.QMainWindow()
        self.ui = pscreen
        self.ui.setupUi(self.window)
        self.ui.set_main_module(pmain)
        self.window.show()

    def clean_movies_table(self, ptable):
        ptable.setRowCount(0)

    def make_table(self, pinfo, ptable, pspaces, pcols):
        self.clean_movies_table(ptable)
        fill_table( ptable, serialize_table( pinfo, pspaces, pcols, True ),
                    pcols )
      
    def ask_movie_data(self):
        info_movie = movie_data_request( unicode(self.movie_data.text()) )
        if isinstance(info_movie[0], type(None)):
            show_message("Movie doesn't exist, try again...", "Error", False)
        else:
            self.make_table( info_movie, self.movies_table, movie_spaces, MOVIES_COLS )

    def ask_movies_per_franchise(self):
        franchise_movies = movies_franchise_request( unicode(self.franchise_data.currentText()) )
        self.make_table( franchise_movies, self.movies_table, movie_spaces, MOVIES_COLS )

    def ask_movies_among_years(self):
        if (self.start_year_data.text().isEmpty() or self.final_year_data.text().isEmpty()):
            show_message( "Please insert required data...","Warning",False )
        else:
            years_movies = years_movies_request( int(self.start_year_data.text()), int(self.final_year_data.text()) )
            if (len(years_movies) == 0):
                show_message( "There's no movies","Information",True )
            else: 
                self.make_table( years_movies, self.movies_table, movie_spaces, MOVIES_COLS )

    def ask_movies_producer(self):
        producer_movies = producer_movies_request( unicode(self.producer_data.currentText()) )
        self.make_table( producer_movies, self.movies_producer_table, producer_spaces, PROD_COLS )
    
    def ask_less_movie(self):
        self.less_duration_data.setText( less_movie_request() )

    def ask_high_movie(self):
        self.high_duration_data.setText( high_movie_request() )

    def ask_amount_movies(self):
        self.amount_movies_data.setText( amount_movies_request() )

    def ask_averages(self):
        producer_averages = producer_averages_request()
        self.make_table( producer_averages, self.avg_producer_table, ["_id","average"], AVG_COLS )


###########################   User Interface Window  #####################################


 #   Init ui application    #
def main():
    app = QtGui.QApplication(sys.argv)
    movie_window = Ui_MovieModule()
    movie_window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()