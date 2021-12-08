from PyQt5 import QtWidgets, uic, QtCore
from user import Users
from menu import Menuscreen_window


class Welcomescreen_window(QtWidgets.QMainWindow):

    user = Users()

    def __init__(self):
        super(Welcomescreen_window, self).__init__()
        uic.loadUi('Ui/welcomescreen.ui', self)

        self.signup_button.clicked.connect(self.signup)
        self.login_button.clicked.connect(self.login)

        self.show()

    def signup(self):
        _translate = QtCore.QCoreApplication.translate
        self.user = Users(self.lineEdit_2.text())
        Users.readjson_user()
        if self.user.checkname():
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You have an account already.Login"))
        else:
            self.user.save_to_json(self.user)
            self.error_label.setStyleSheet(
                "color: rgb(255, 255, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "Congrats ! Try login now"))

    def login(self):
        _translate = QtCore.QCoreApplication.translate
        self.user.readjson_user()
        name = self.lineEdit_2.text()
        for i, j in self.user.users_dict.items():
            if name == i:
                level = j["level"]
                totaltime = j["totaltime"]
                self.user.name = name
                self.user.level = level
                self.user.totaltime = totaltime
                break

        if self.user.checkname():
            self.cams = Menuscreen_window(self.user)
            self.cams.show()
            self.close()

        else:
            self.error_label.setStyleSheet(
                "color: rgb(195, 0, 0);font: 10pt \"Berlin Sans FB;\"\n")
            self.error_label.setText(_translate(
                "MainWindow", "You Dont Have Account , Signin first."))
