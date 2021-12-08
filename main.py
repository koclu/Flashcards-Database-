import sys
from PyQt5 import QtWidgets
from welcome import Welcomescreen_window

app = QtWidgets.QApplication(sys.argv)
window = Welcomescreen_window()
app.exec_()