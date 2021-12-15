from PyQt5 import QtCore, QtWidgets, uic
from user import Users
import menu
import db


class Wordscreen_window(QtWidgets.QMainWindow):

    def __init__(self, user):
        self.user = user
        self.count = user.totaltime
        super(Wordscreen_window, self).__init__()
        uic.loadUi('Ui/wordscreen.ui', self)

        self.pushButton.clicked.connect(self.back)
        self.green_button.clicked.connect(self.push_green_button)
        self.red_button.clicked.connect(self.push_red_button)
        self.green_button.setCheckable(True)
        self.red_button.setCheckable(True)

        self.show()
        self.q_timer = QtCore.QTimer()
        self.q_timer.timeout.connect(self.showTime)
        self.q_timer.start(1000)

        self.playgame()

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

    def showTime(self):
        self.count += 1
        m = self.count//60
        s = self.count % 60
        if s <= 60:
            self.total_time_label.setText(
                "Minute : %d Second : %d " % (m, s))
            s += 1
            if s == 60:
                m += 1
                s = 0

    def playgame(self):
        self.user.word_of_levels = db.getleveltable(self.user)
        self.level_label.setText("Level : " + str(self.user.level))
        self.id = 0
        self.next_word()

    def push_green_button(self):
        self.id = self.id + 1
        self.next_word()

    def push_red_button(self):
        self.user.word_of_levels.append(
            (self.word_id, self.dutch, self.english))
        self.id = self.id + 1
        self.next_word()

    def next_word(self):
        if self.id == len(self.user.word_of_levels):
            self.user.level += 1
            db.updatelevel(self.user)
            self.user.word_of_levels = db.getleveltable(self.user)
            self.playgame()
        else:
            self.green_button.setEnabled(False)
            self.red_button.setEnabled(False)
            word_id, dutch, english = self.user.word_of_levels[self.id]
            self.word_id = word_id
            self.dutch = dutch
            self.english = english
            self.remaining_word_label.setText(
                "Remaining Words : " + str(len(self.user.word_of_levels) - self.id))
            self.wordcard_label.setText(dutch)
            self.wordcard_label.setStyleSheet("border-radius:20px;font: 25pt \"Berlin Sans FB\";\n"
                                              "color:rgb(255, 255, 255) ;\n"
                                              "background-color: rgb(85, 85, 255);")
            self.counter_on3()
            self.green_button.setEnabled(True)
            self.red_button.setEnabled(True)
            self.wordcard_label.setText(english)
            self.wordcard_label.setStyleSheet("border-radius:20px;font: 25pt \"Berlin Sans FB\";\n"
                                              "color:rgb(255, 255, 255) ;\n"
                                              "background-color: rgb(38, 180, 182);")

    def back(self):
        self.q_timer.stop()
        self.user.totaltime = self.count
        db.save_user(self.user)
        self.cams = menu.Menuscreen_window(self.user)
        self.cams.show()
        self.close()
