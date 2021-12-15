from PyQt5 import QtCore, QtWidgets, uic
from user import Users
import menu
import db


class Wordscreen_window(QtWidgets.QMainWindow):

    def __init__(self, user):
        self.user = user
        self.count = user.totaltime
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
        while len(self.user.word_of_levels) >= 0:
            if len(self.user.word_of_levels) == 0:
                self.user.level += 1
                db.updatelevel(self.user)
                self.user.word_of_levels = db.getleveltable(self.user)
                continue
            else:
                self.level_label.setText("Level : " + str(self.user.level))
                self.remaining_word_label.setText(
                    "Remaining Words : " + str(len(self.user.word_of_levels)))
                self.green_button.setEnabled(False)
                self.red_button.setEnabled(False)
                for word_id, dutch, english in self.user.word_of_levels:
                    self.word_id = word_id
                    self.dutch = dutch
                    self.english = english
                    self.wordcard_label.setText(dutch)
                    self.wordcard_label.setStyleSheet("border-radius:20px;font: 25pt \"Berlin Sans FB\";\n"
                                                      "color:rgb(255, 255, 255) ;\n"
                                                      "background-color: rgb(85, 85, 255);")
                    self.counter_on3()
                    self.wordcard_label.setText(english)
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
        self.user.word_of_levels.remove(
            (self.word_id, self.dutch, self.english))
        self.remaining_word_label.setText(
            "Remaining Words : " + str(len(self.user.word_of_levels)))
        self.lineEditTitles.setText("       Current Level Success Rate : " + str(self.user.atOnce)+"/"+str(self.user.Attempts))
        
        

    def push_red_button(self):
        self.user.Attempts+=1
        self.lineEditTitles.setText("       Current Level Success Rate : " + str(self.user.atOnce)+"/"+str(self.user.Attempts))
      
        

    def back(self):
        self.q_timer.stop()
        self.user.totaltime = self.count
        db.save_user(self.user)
        self.cams = menu.Menuscreen_window(self.user)
        self.cams.show()
        self.close()
