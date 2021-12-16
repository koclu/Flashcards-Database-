from PyQt5 import QtWidgets, uic
from word_screen import Wordscreen_window
from addlevel import Addlevel_Window
import os
from statistics import Statistics_Window
from addlevel import Addlevel_Window
from word_screen_for_selected_level import Wordscreen_window_temporarylevel
from word_screen_custom import Wordscreen_window_custom
import db


class Menuscreen_window(QtWidgets.QMainWindow):

    def __init__(self, user):
        self.user = user
        super(Menuscreen_window, self).__init__()
        uic.loadUi('Ui/menuscreen.ui', self)
        self.user.temporary_level = self.user.level

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
        self.getbuttonlevel.clicked.connect(self.changelevel)
        self.getbuttonlevel_2.clicked.connect(self.changecustomlevel)
        self.show()

    def changelevel(self):
        temporary_level = int(self.Get_Level1.text())
        if self.user.level < temporary_level:
            self.label.setText("You can't play this level")
            self.label.setStyleSheet("color: rgb(195, 0, 0)")
        else:
            self.user.temporary_level = temporary_level
            self.close()
            self.cams = Wordscreen_window_temporarylevel(self.user)

    def changecustomlevel(self):
        levelsname = db.getcustomlevelname(self.user)
        for i in levelsname:
            if str(self.Get_Level1_2.text()) == i[0]:
                self.user.customlevelname = self.Get_Level1_2.text()
                self.close()
                self.cams = Wordscreen_window_custom(self.user)
                break
            else:
                self.label.setText(
                    "You don't have this custom level.\nWrite level name correctly ")
                self.label.setStyleSheet(
                    "color: rgb(195, 0, 0)")

    def push_resetbutton(self):
        self.user.level = 1
        db.updatelevel(self.user)
        self.level_label.setText(
            "Level : {}".format(self.user.level))
        self.progressBar_menu_3.setProperty(
            "value", db.calculate_totalprogress(self.user))

    def play(self):
        self.close()
        self.cams = Wordscreen_window(self.user)

    def showstatistics(self):
        self.close()
        self.cams = Statistics_Window(self.user)

    def quit(self):
        db.save_user(self.user)
        os._exit(1)

    def showaddlevel(self):
        self.cams = Addlevel_Window(self.user)
        self.cams.show()
        self.close()
