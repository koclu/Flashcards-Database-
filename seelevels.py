
from PyQt5 import QtCore, QtWidgets, uic
import db
import addlevel


class See_levels_Window(QtWidgets.QMainWindow):

    def __init__(self, user):
        self.user = user
        super(See_levels_Window, self).__init__()
        uic.loadUi('Ui/custom_levels.ui', self)
        self.quitbutton2.clicked.connect(self.backtoaddlevel)
        self.getlevelnames()

    def backtoaddlevel(self):
        self.cams = addlevel.Addlevel_Window(self.user)
        self.cams.show()
        self.close()

    def getlevelnames(self):
        _translate = QtCore.QCoreApplication.translate
        levelnames = db.getcustomlevelname(self.user)

        for i in levelnames:
            item = QtWidgets.QListWidgetItem(i[0])
            self.listWidget.addItem(item)
