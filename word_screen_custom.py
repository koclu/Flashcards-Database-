from PyQt5 import QtCore, QtWidgets, uic
import menu
import db


class Wordscreen_window_custom(QtWidgets.QMainWindow):

    def __init__(self, user):
        self.user = user
        self.count = user.totaltime
        self.remainingtime = 3
        super(Wordscreen_window_custom, self).__init__()
        uic.loadUi('Ui/wordscreen.ui', self)

        self.pushButton.clicked.connect(self.back)
        self.green_button.clicked.connect(self.push_green_button)
        self.red_button.clicked.connect(self.push_red_button)
        self.green_button.setCheckable(True)
        self.red_button.setCheckable(True)
        self.progressBar_menu_6.setProperty(
            "value", self.calculateprogressbar_menu_6())
        self.show()
        self.q_timer = QtCore.QTimer()
        self.q_timer.timeout.connect(self.showTime)
        self.q_timer.start(1000)

        self.playgame()

    def showTime(self):
        if self.remainingtime != 1:
            self.remainingtime -= 1
            self.timer.setText(str(self.remainingtime))
        else:
            self.timer.setText("---")
            self.green_button.setEnabled(True)
            self.red_button.setEnabled(True)
            self.wordcard_label.setText(self.english)
            self.wordcard_label.setStyleSheet("border-radius:20px;font: 25pt \"Berlin Sans FB\";\n"
                                              "color:rgb(255, 255, 255) ;\n"
                                              "background-color: rgb(38, 180, 182);")
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
        self.level_label.setText(str(self.user.customlevelname))
        self.user.word_of_levels = db.getcustomlevels(self.user)
        self.id = 0
        self.next_word()

    def push_green_button(self):
        self.user.atOnce += 1
        self.user.Attempts += 1
        self.remainingtime = 4
        self.lineEditTitles.setText(
            "       Current Level Success Rate : " + str(self.user.atOnce)+"/"+str(self.user.Attempts))
        self.progressBar_menu_6.setProperty(
            "value", self.calculateprogressbar_menu_6())
        self.id = self.id + 1
        self.next_word()

    def calculateprogressbar_menu_6(self):
        if self.user.atOnce == 0 or self.user.Attempts == 0:
            return 0
        else:
            return (self.user.atOnce/self.user.Attempts)*100

    def push_red_button(self):
        self.user.word_of_levels.append(
            (self.dutch, self.english))
        self.id = self.id + 1
        self.user.Attempts += 1
        self.remainingtime = 4
        self.lineEditTitles.setText(
            "       Current Level Success Rate : " + str(self.user.atOnce)+"/"+str(self.user.Attempts))
        self.progressBar_menu_6.setProperty(
            "value", self.calculateprogressbar_menu_6())
        self.next_word()

    def next_word(self):
        if self.id == len(self.user.word_of_levels):
            self.back()
        else:

            self.green_button.setEnabled(False)
            self.red_button.setEnabled(False)
            dutch, english = self.user.word_of_levels[self.id]
            self.dutch = dutch
            self.english = english
            self.remaining_word_label.setText(
                "Remaining Words : " + str(len(self.user.word_of_levels) - self.id))
            self.wordcard_label.setText(dutch)
            self.wordcard_label.setStyleSheet("border-radius:20px;font: 25pt \"Berlin Sans FB\";\n"
                                              "color:rgb(255, 255, 255) ;\n"
                                              "background-color: rgb(85, 85, 255);")

    def back(self):
        self.q_timer.stop()
        self.user.totaltime = self.count
        db.save_user(self.user)
        self.cams = menu.Menuscreen_window(self.user)
        self.cams.show()
        self.close()
