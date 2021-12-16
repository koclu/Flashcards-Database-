from PyQt5 import QtWidgets, uic
from user import Users
from word_screen import Wordscreen_window
from addlevel import Addlevel_Window
import os
from statistics import Statistics_Window
from addlevel import Addlevel_Window
import db


class Menuscreen_window(QtWidgets.QMainWindow):

    def __init__(self, user):
        self.user = user
        super(Menuscreen_window, self).__init__()
        uic.loadUi('Ui/menuscreen.ui', self)

        self.username_label.setText(self.user.name.upper())
        self.level_label.setText(
            "Level : {}".format(self.user.level))
        self.progressBar_menu_3.setProperty(
            "value", db.calculate_totalprogress(self.user))
        self.playbutton.clicked.connect(self.play)
        self.quitbutton.clicked.connect(self.quit)
        self.resetbutton.clicked.connect(self.push_resetbutton)
        self.playbutton_2.clicked.connect(self.showstatistics)
        self.addlevelbutton.clicked.connect(self.showaddlevel)
        self.show()

    def push_resetbutton(self):
        self.user.level = 1
        db.updatelevel(self.user)
        self.level_label.setText(
            "Level : {}".format(self.user.level))
        self.progressBar_menu_3.setProperty(
            "value", db.calculate_totalprogress(self.user))

    def play(self):
        self.cams = Wordscreen_window(self.user)
        self.cams.show()
        self.close()
        
    def showstatistics(self):
        self.cams = Statistics_Window(self.user)
        self.cams.show()
        self.close()


    def quit(self):
        # Users.save_to_json(self.user)
        db.save_user(self.user)
        os._exit(1)
    def showaddlevel(self):
        self.cams = Addlevel_Window(self.user)
        self.cams.show()
        self.close()

    def golevel(self):
        golevel=self.golevel.text()
        db.checkgolevel()
        
    