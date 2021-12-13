from PyQt5 import QtWidgets, uic, QtCore
from user import Users
from menu import Menuscreen_window
import db


class Welcomescreen_window(QtWidgets.QMainWindow):

    user = Users()

    def __init__(self):
        super(Welcomescreen_window, self).__init__()
        uic.loadUi('Ui/welcomescreen.ui', self)

        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.login)
        self.checkusername_button.clicked.connect(self.check_username)
        self.show()

    def signup(self):
        _translate = QtCore.QCoreApplication.translate
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()

        if len(username) == 0 or len(password) == 0:
            self.error_label.setStyleSheet(
                "color: rgb(195, 0, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You must fill both spaces"))
            return
        self.user = Users(self.lineEdit_2.text())
        self.user.password = self.lineEdit_3.text()

        if db.checkname(self.user.name):

            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You have an account already.Login"))
        else:
            db.savename(self.user)
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "Congrats ! Try login now"))

        # Users.readjson_user()

        """  if self.user.checkname():
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You have an account already.Login"))
        else:
            self.user.save_to_json(self.user)
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "Congrats ! Try login now"))"""

    def login(self):
        _translate = QtCore.QCoreApplication.translate
        names = db.bringallnames()
        username = self.lineEdit_2.text()
        password = self.lineEdit_3.text()
        if not db.checkname(username):
            self.error_label.setStyleSheet(
                "color: rgb(195, 0, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You Dont Have Account , Signin first."))
            return

        for nametuple in names:
            if nametuple[0] == username and nametuple[1] == password:

                self.user = Users(nametuple[0], nametuple[3], nametuple[2])
                self.user.password = nametuple[1]

                self.cams = Menuscreen_window(self.user)
                self.cams.show()
                self.close()
                break
            elif nametuple[0] != username or nametuple[1] != password:
                self.error_label.setStyleSheet(
                    "color: rgb(195, 0, 0);font: 10pt \"Berlin Sans FB;\"\n")
                self.error_label.setText(_translate(
                    "MainWindow", "Wrong Password . Try Again "))

        """        _translate = QtCore.QCoreApplication.translate
        self.user.readjson_user()
        name = self.lineEdit_2.text()
        for i, j in self.user.users_dict.items():
            if name == i:
                level = j["level"]
                totaltime = j["totaltime"]
                self.user.name = name
                self.user.level = level
                self.user.totaltime = totaltime
                break"""

    def check_username(self):
        _translate = QtCore.QCoreApplication.translate
        if db.checkname(self.lineEdit_2.text()):

            self.error_label.setStyleSheet(
                "color: rgb(195, 0, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "Username already taken"))
        else:
            self.error_label.setStyleSheet(

                "color: rgb(85, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "Username is available"))
