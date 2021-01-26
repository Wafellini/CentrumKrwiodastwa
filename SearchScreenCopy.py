# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SearchScreen.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Baza import Baza

class Ui_SearchScreen(object):
    def __init__(self, base):
        self.dtbase = base

    def setupUi(self, SearchScreen):
        SearchScreen.setObjectName("SearchScreen")
        SearchScreen.resize(900, 500)
        self.centralwidget = QtWidgets.QWidget(SearchScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.label_Relacja = QtWidgets.QLabel(self.centralwidget)
        self.label_Relacja.setGeometry(QtCore.QRect(30, 20, 47, 13))
        self.label_Relacja.setObjectName("label_Relacja")
        self.wybor_Relacji = QtWidgets.QListWidget(self.centralwidget)
        self.wybor_Relacji.setGeometry(QtCore.QRect(20, 40, 200, 120))
        self.wybor_Relacji.setObjectName("wybor_Relacji")
        self.Tablica_Wyszukiwan = QtWidgets.QTableWidget(self.centralwidget)
        self.Tablica_Wyszukiwan.setGeometry(QtCore.QRect(10, 200, 280, 221))
        self.Tablica_Wyszukiwan.setObjectName("Tablica_Wyszukiwan")
        self.Tablica_Wyszukiwan.setColumnCount(1)
        # self.Tablica_Wyszukiwan.setRowCount(3)

        self.Tablica_Wyszukiwan.setRowCount(20)
        for i in range(20):
            item = QtWidgets.QTableWidgetItem()
            self.Tablica_Wyszukiwan.setVerticalHeaderItem(i, item)

        # okienko do wyświetlania powiadomień
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(290, 430, 500, 50))
        self.textBrowser.setObjectName("textBrowser")

        self.Tablica_Wyszukiwan.setHorizontalHeaderItem(0, item)
        self.label_Wyszukiwanie = QtWidgets.QLabel(self.centralwidget)
        self.label_Wyszukiwanie.setGeometry(QtCore.QRect(30, 170, 91, 16))
        self.label_Wyszukiwanie.setObjectName("label_Wyszukiwanie")
        self.Tablica_Wynikow = QtWidgets.QTableWidget(self.centralwidget)
        self.Tablica_Wynikow.setGeometry(QtCore.QRect(300, 40, 600, 331))
        self.Tablica_Wynikow.setObjectName("Tablica_Wynikow")


        self.Tablica_Wynikow.setColumnCount(10)
        for i in range(10):
            item = QtWidgets.QTableWidgetItem()
            self.Tablica_Wynikow.setHorizontalHeaderItem(i, item)


        self.Tablica_Wynikow.setRowCount(30)
        for i in range(30):
            item = QtWidgets.QTableWidgetItem()
            self.Tablica_Wynikow.setVerticalHeaderItem(i, item)

        self.Guzik_Zatwierdzajacy = QtWidgets.QPushButton(self.centralwidget)
        self.Guzik_Zatwierdzajacy.setGeometry(QtCore.QRect(700, 400, 75, 23))
        self.Guzik_Zatwierdzajacy.setObjectName("Guzik_Zatwierdzajacy")





        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setStrikeOut(False)
        item.setFont(font)
        # self.Tablica_Wynikow.setVerticalHeaderItem(6, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.Tablica_Wynikow.setHorizontalHeaderItem(0, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.Tablica_Wynikow.setHorizontalHeaderItem(1, item)
        # item = QtWidgets.QTableWidgetItem()
        # self.Tablica_Wynikow.setHorizontalHeaderItem(2, item)
        self.label_Wynik = QtWidgets.QLabel(self.centralwidget)
        self.label_Wynik.setGeometry(QtCore.QRect(320, 20, 151, 16))
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


        amount = len(Baza.getTableNamesFromDb('testdb'))
        for i in range(amount):
            item = QtWidgets.QListWidgetItem()
            self.wybor_Relacji.addItem(item)

        # Ustawienie listy relacji do wyboru
        tables = Baza.getTableNamesFromDb('testdb')
        it = 0
        print(tables)
        for i in tables:
            print(i)
            item = self.wybor_Relacji.item(it)
            item.setText(_translate("SearchScreen", tables[it]))
            it += 1

        self.Guzik_Zatwierdzajacy.setText(_translate("TechWindow", "Zatwierdź"))


        self.wybor_Relacji.setSortingEnabled(__sortingEnabled)
        item = self.Tablica_Wyszukiwan.verticalHeaderItem(0)
        item.setText(_translate("SearchScreen", "typ_krwi"))
        item = self.Tablica_Wyszukiwan.verticalHeaderItem(1)
        item.setText(_translate("SearchScreen", "ilosc"))
        item = self.Tablica_Wyszukiwan.verticalHeaderItem(2)
        item.setText(_translate("SearchScreen", "id_plac"))
        item = self.Tablica_Wyszukiwan.horizontalHeaderItem(0)
        item.setText(_translate("SearchScreen", "Wzór danych"))
        self.label_Wyszukiwanie.setText(_translate("SearchScreen", "Wyszukiwanie:"))

        self.label_Wynik.setText(_translate("SearchScreen", "Wynik wyszukiwania:"))


        self.Guzik_Zatwierdzajacy.clicked.connect(self.GetResults)
        self.wybor_Relacji.clicked.connect(self.UpdateRelacje)

    def GetResults(self):
        print('test wypisywania info w Oknie wydzukiwania')
        item2 = self.wybor_Relacji.currentItem()
        print('item2======',item2, item2.text())
        if item2 is None:
            self.textBrowser.setText('Wybierz relecję i akcję jaką '
                                     'chcesz przeprowadzić przed potwierdzeniem przyciskiem')
        else:
            item2 = item2.text()
            items = []

            it = len(Baza.getColumnNamesFromTable(self.dtbase, item2))
            for i in range(it):
                if (self.Tablica_Wyszukiwan.item(i, 0) is not None):
                    if self.Tablica_Wyszukiwan.item(i, 0).text() == '':
                        items.append(None)
                    else:
                        items.append(self.Tablica_Wyszukiwan.item(i, 0).text())
                else:
                    items.append(None)
            print('items: ', items)
            err = Baza.select(self.dtbase, item2, items)




            if type(err) is int:
                if err == 1364 or err == 1064:
                    self.textBrowser.setText('Nie pozostawaij żadnych pól pustych!')
                    _translate = QtCore.QCoreApplication.translate

                    for c in range(10):
                        for r in range(30):
                            item1 = QtWidgets.QTableWidgetItem()
                            self.Tablica_Wynikow.setItem(r, c, item1)
                            item = self.Tablica_Wynikow.item(r, c)
                            item.setText(_translate("TechWindow", ''))
                elif err == 1292:
                    self.textBrowser.setText('Podawaj datę w formacie YYYY-MM-DD')
                elif err == 1366:
                    self.textBrowser.setText('Wpisano inna wartość w pole, w którym '
                                             'powinna byc wpisana liczba')
                elif err == 1406:
                    self.textBrowser.setText('Przeroczono maksymalną liczbę znaków przy'
                                             ' podawaniu danych')

                elif err == 1525:
                    self.textBrowser.setText('Podawaj datę w formacie YYYY-MM-DD')

                else:
                    self.textBrowser.setText('Wystąpił błąd!')
            elif err is not None:
                self.UpdateWyniki(item2, err)
            elif err is None:
                self.textBrowser.setText('Nie znaleziono żadnych pasujących danych')
                _translate = QtCore.QCoreApplication.translate

                for c in range(10):
                    for r in range(30):
                        item1 = QtWidgets.QTableWidgetItem()
                        self.Tablica_Wynikow.setItem(r, c, item1)
                        item = self.Tablica_Wynikow.item(r, c)
                        item.setText(_translate("TechWindow", ''))


            print(err)

    def UpdateWyniki(self,table, selects):
        columns = Baza.getColumnNamesFromTable(self.dtbase,table)

        _translate = QtCore.QCoreApplication.translate
        print('SELECTS:  ',selects,len(selects))
        print('SELECTS:  ', selects[0],len(selects[0]))

        # Wypełnianie tabeli... implementacja
        for c in range(len(columns)):
            item = self.Tablica_Wynikow.horizontalHeaderItem(c)
            item.setText(_translate("TechWindow", columns[c]))
            for r in range(len(selects)):
                item = self.Tablica_Wynikow.verticalHeaderItem(r)
                item.setText(_translate("TechWindow", 'wynik{}'.format(r + 1)))
                item1 = QtWidgets.QTableWidgetItem()
                self.Tablica_Wynikow.setItem(r,c,item1)
                item = self.Tablica_Wynikow.item(r,c)
                # item.setText(selects[r][c])
                item.setText(_translate("TechWindow", str(selects[r][c])))



    def UpdateRelacje(self):
        item1 = self.wybor_Relacji.currentItem()
        item1 = item1.text()

        columns = Baza.getColumnNamesFromTable(self.dtbase, item1)
        numC = len(columns)

        _translate = QtCore.QCoreApplication.translate



        for i in range(20):
            # item = self.Tablica_Wyszukiwan.horizontalHeaderItem(i)
            # item.setText(_translate("TechWindow", "Wzór danych"))
            if (numC - i) > 0:
                item = self.Tablica_Wyszukiwan.verticalHeaderItem(i)
                item.setText(_translate("SearchScreen", columns[i]))
            else:
                item = self.Tablica_Wyszukiwan.verticalHeaderItem(i)
                item.setText(_translate("SearchScreen", ""))
        item = self.Tablica_Wyszukiwan.horizontalHeaderItem(0)
        item.setText(_translate("SearchScreen", "Wzór danych"))
        print('po teście "Modyfikuj dane"')