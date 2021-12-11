from PyQt5 import QtWidgets, uic
from user import Users
from word_screen import Wordscreen_window
from addlevel import Addlevel_Window
import os
from statistics import Statistics_Window

class Menuscreen_window(QtWidgets.QMainWindow):

    def __init__(self, user):
        self.user = user
        super(Menuscreen_window, self).__init__()
        uic.loadUi('Ui/menuscreen.ui', self)

        self.username_label.setText(user.name.upper())
        self.level_label.setText(
            "Level : {}".format(user.level))
        self.progress_progressBar.setProperty(
            "value", user.totalprogress())

        self.playbutton.clicked.connect(self.play)
        self.quitbutton.clicked.connect(self.quit)
        self.resetbutton.clicked.connect(self.push_resetbutton)
        self.playbutton_2.clicked.connect(self.showstatistics)
        self.addlevelbutton.clicked.connect(self.showaddlevel)
        self.show()

    def push_resetbutton(self):
        self.user.level = 1
        self.level_label.setText(
            "Level : {}".format(self.user.level))
        self.progress_progressBar.setProperty(
            "value", self.user.totalprogress())

    def play(self):
        self.cams = Wordscreen_window(self.user)
        self.cams.show()
        self.close()
        
    def showstatistics(self):
        self.cams = Statistics_Window(self.user)
        self.cams.show()
        self.close()


    def quit(self):
        Users.save_to_json(self.user)
        os._exit(1)
    def showaddlevel(self):
        self.cams = Addlevel_Window(self.user)
        self.cams.show()
        self.close()