# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SearchScreen(object):
    def setupUi(self, SearchScreen):
        SearchScreen.setObjectName("SearchScreen")
        SearchScreen.resize(549, 418)
        self.centralwidget = QtWidgets.QWidget(SearchScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Relacja = QtWidgets.QLabel(self.centralwidget)
        self.label_Relacja.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.label_Relacja.setObjectName("label_Relacja")
        self.wybor_Relacji = QtWidgets.QListWidget(self.centralwidget)
        self.wybor_Relacji.setGeometry(QtCore.QRect(20, 40, 151, 71))
        self.wybor_Relacji.setObjectName("wybor_Relacji")
        item = QtWidgets.QListWidgetItem()
        self.wybor_Relacji.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wybor_Relacji.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.wybor_Relacji.addItem(item)
        self.Tablica_Wyszukiwan = QtWidgets.QTableWidget(self.centralwidget)
        self.Tablica_Wyszukiwan.setGeometry(QtCore.QRect(10, 150, 171, 221))
        self.Tablica_Wyszukiwan.setObjectName("Tablica_Wyszukiwan")
        self.Tablica_Wyszukiwan.setColumnCount(1)
        self.Tablica_Wyszukiwan.setRowCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wyszukiwan.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wyszukiwan.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wyszukiwan.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wyszukiwan.setHorizontalHeaderItem(0, item)
        self.label_Wyszukiwanie = QtWidgets.QLabel(self.centralwidget)
        self.label_Wyszukiwanie.setGeometry(QtCore.QRect(30, 130, 91, 16))
        self.label_Wyszukiwanie.setObjectName("label_Wyszukiwanie")
        self.Tablica_Wynikow = QtWidgets.QTableWidget(self.centralwidget)
        self.Tablica_Wynikow.setGeometry(QtCore.QRect(200, 40, 331, 331))
        self.Tablica_Wynikow.setObjectName("Tablica_Wynikow")
        self.Tablica_Wynikow.setColumnCount(3)
        self.Tablica_Wynikow.setRowCount(7)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStrikeOut(False)
        item.setFont(font)
        self.Tablica_Wynikow.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Tablica_Wynikow.setHorizontalHeaderItem(2, item)
        self.label_Wynik = QtWidgets.QLabel(self.centralwidget)
        self.label_Wynik.setGeometry(QtCore.QRect(210, 20, 151, 16))
        self.label_Wynik.setObjectName("label_Wynik")
        SearchScreen.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SearchScreen)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 549, 21))
        self.menubar.setObjectName("menubar")
        SearchScreen.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SearchScreen)
        self.statusbar.setObjectName("statusbar")
        SearchScreen.setStatusBar(self.statusbar)

        self.retranslateUi(SearchScreen)
        QtCore.QMetaObject.connectSlotsByName(SearchScreen)

    def retranslateUi(self, SearchScreen):
        _translate = QtCore.QCoreApplication.translate
        SearchScreen.setWindowTitle(_translate("SearchScreen", "MainWindow"))
        self.label_Relacja.setText(_translate("SearchScreen", "Relacja:"))
        __sortingEnabled = self.wybor_Relacji.isSortingEnabled()
        self.wybor_Relacji.setSortingEnabled(False)
        item = self.wybor_Relacji.item(0)
        item.setText(_translate("SearchScreen", "Placowki"))
        item = self.wybor_Relacji.item(1)
        item.setText(_translate("SearchScreen", "Laboratoria"))
        item = self.wybor_Relacji.item(2)
        item.setText(_translate("SearchScreen", "Bilansy_Krwi"))
        self.wybor_Relacji.setSortingEnabled(__sortingEnabled)
        item = self.Tablica_Wyszukiwan.verticalHeaderItem(0)
        item.setText(_translate("SearchScreen", "typ_krwi"))
        item = self.Tablica_Wyszukiwan.verticalHeaderItem(1)
        item.setText(_translate("SearchScreen", "ilosc"))
        item = self.Tablica_Wyszukiwan.verticalHeaderItem(2)
        item.setText(_translate("SearchScreen", "id_plac"))
        item = self.Tablica_Wyszukiwan.horizontalHeaderItem(0)
        item.setText(_translate("SearchScreen", "Podaj cechy:"))
        self.label_Wyszukiwanie.setText(_translate("SearchScreen", "Wyszukiwanie:"))
        item = self.Tablica_Wynikow.verticalHeaderItem(0)
        item.setText(_translate("SearchScreen", "wynik1"))
        item = self.Tablica_Wynikow.verticalHeaderItem(1)
        item.setText(_translate("SearchScreen", "wynik2"))
        item = self.Tablica_Wynikow.verticalHeaderItem(2)
        item.setText(_translate("SearchScreen", "wynik3"))
        item = self.Tablica_Wynikow.verticalHeaderItem(3)
        item.setText(_translate("SearchScreen", "wynik4"))
        item = self.Tablica_Wynikow.verticalHeaderItem(4)
        item.setText(_translate("SearchScreen", "wynik5"))
        item = self.Tablica_Wynikow.verticalHeaderItem(5)
        item.setText(_translate("SearchScreen", "wynik6"))
        item = self.Tablica_Wynikow.verticalHeaderItem(6)
        item.setText(_translate("SearchScreen", "wynik7"))
        item = self.Tablica_Wynikow.horizontalHeaderItem(0)
        item.setText(_translate("SearchScreen", "typ_krwi"))
        item = self.Tablica_Wynikow.horizontalHeaderItem(1)
        item.setText(_translate("SearchScreen", "ilosc"))
        item = self.Tablica_Wynikow.horizontalHeaderItem(2)
        item.setText(_translate("SearchScreen", "id_plac"))
        self.label_Wynik.setText(_translate("SearchScreen", "Wynik wyszukiwania:"))
