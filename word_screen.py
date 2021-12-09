from PyQt5 import QtCore, QtWidgets, uic
from user import Users
import menu
import threading


class Wordscreen_window(QtWidgets.QMainWindow):

    def __init__(self, user):
        self.user = user
        self.user.atOnce=0
        self.user.Attempts=0
        super(Wordscreen_window, self).__init__()
        uic.loadUi('Ui/wordscreen.ui', self)

        self.pushButton.clicked.connect(self.back)
        self.green_button.clicked.connect(self.push_green_button)
        self.red_button.clicked.connect(self.push_red_button)
        self.green_button.setCheckable(True)
        self.red_button.setCheckable(True)

        self.show()

        try:
            threading.Thread(target=self.playgame).start()
            threading.Thread(target=self.totaltime).start()

        except RuntimeError:
            Users.save_to_json(user)
            self.back()

    def sleeptime(self, n):
        loop = QtCore.QEventLoop()
        QtCore.QTimer.singleShot(n*1000, loop.quit)
        loop.exec_()

    def counter_on3(self):
        self.timer.setText(str(3))
        self.sleeptime(1)
        self.timer.setText(str(2))
        self.sleeptime(1)
        self.timer.setText(str(1))
        self.sleeptime(1)
        self.timer.setText("---")

    def totaltime(self):
        m = self.user.totaltime//60
        s = self.user.totaltime % 60

        while s <= 60:
            self.total_time_label.setText(
                "Minute : %d Second : %d " % (m, s))
            self.sleeptime(1)
            s += 1
            self.user.totaltime += 1
            if s == 60:
                m += 1
                self.user.totaltime += 60*m
                s = 0

    def playgame(self):
        self.user.get_level_id()
        self.index = 0
        while len(self.user.levelid) >= 0:
            if len(self.user.levelid) == 0:
                self.user.levelcheck()
            else:
                self.level_label.setText("Level : " + str(self.user.level))
                self.remaining_word_label.setText(
                    "Remaining Words : " + str(len(self.user.levelid)))

                try:
                    self.id = self.user.levelid[self.index]
                except IndexError:
                    self.index = 0
                    continue
                self.green_button.setEnabled(False)
                self.red_button.setEnabled(False)

                self.wordcard_label.setText(
                    self.user.wordsdata[str(self.id)]["Dutch"])
                self.wordcard_label.setStyleSheet("border-radius:20px;font: 25pt \"Berlin Sans FB\";\n"
                                                  "color:rgb(255, 255, 255) ;\n"
                                                  "background-color: rgb(85, 85, 255);")
                self.counter_on3()
                self.wordcard_label.setText(
                    self.user.wordsdata[str(self.id)]["ENG"])
                self.wordcard_label.setStyleSheet("border-radius:20px;font: 25pt \"Berlin Sans FB\";\n"
                                                  "color:rgb(255, 255, 255) ;\n"
                                                  "background-color: rgb(38, 180, 182);")
                self.green_button.setEnabled(True)
                self.red_button.setEnabled(True)
                while True:
                    self.sleeptime(0.1)
                    if self.green_button.isChecked():
                        self.green_button.setChecked(False)
                        break
                    elif self.red_button.isChecked():
                        self.red_button.setChecked(False)
                        break
    
    def push_green_button(self):
        self.user.atOnce+=1
        self.user.Attempts+=1
        self.user.levelid.remove(self.id)
        self.remaining_word_label.setText(
            "Remaining Words : " + str(len(self.user.levelid)))
        
        self.lineEditTitles.setText("      Current Level Success Rate : " + str(self.user.atOnce)+"/"+str(self.user.Attempts))
        
        

    def push_red_button(self):
        self.user.Attempts+=1
        self.index += 1
        self.lineEditTitles.setText("      Current Level Success Rate : " + str(self.user.atOnce)+"/"+str(self.user.Attempts))
        self.user.Attempts+=1

    def back(self):
        Users.save_to_json(self.user)
        self.cams = menu.Menuscreen_window(self.user)
        self.cams.show()
        self.close()
