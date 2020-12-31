from Baza import Baza
from ToolsWindowCopy import Ui_TechWindow
from SearchScreenCopy import Ui_SearchScreen
from LoginScreen import Ui_LoginScreen

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


if __name__ == "__main__":
    name = 'testdb'
    dtbase = Baza.connect("localhost", "root", "debilkox",name)


    app = QtWidgets.QApplication(sys.argv)
    TechWindow1 = QtWidgets.QMainWindow()
    TechWindow2 = QtWidgets.QMainWindow()
    TechWindow3 = QtWidgets.QMainWindow()
    ui1 = Ui_TechWindow(dtbase)
    ui2 = Ui_LoginScreen()
    ui3 = Ui_SearchScreen()
    ui1.setupUi(TechWindow1)
    ui2.setupUi(TechWindow2)
    ui3.setupUi(TechWindow3)
    TechWindow1.show()
    TechWindow2.show()
    TechWindow3.show()


    sys.exit(app.exec_())

