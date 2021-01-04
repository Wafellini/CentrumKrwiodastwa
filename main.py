from Baza import Baza
from ToolsWindowCopy import Ui_TechWindow
from SearchScreenCopy import Ui_SearchScreen
from LoginScreenCopy import Ui_LoginScreen

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


if __name__ == "__main__":
    name = 'testdb'
    dtbase = Baza.connect("localhost", "root", "debilkox",name)


    app = QtWidgets.QApplication(sys.argv)

    LoginWindow = QtWidgets.QMainWindow()

    ui2 = Ui_LoginScreen(dtbase)
    ui2.setupUi(LoginWindow)

    LoginWindow.show()


    sys.exit(app.exec_())

