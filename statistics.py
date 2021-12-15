# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'statistics.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from os import X_OK
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5 import QtCore, QtWidgets, uic
from user import Users
import menu
import psycopg2
import db


class Statistics_Window(QtWidgets.QMainWindow):
    def __init__(self, user):
        self.user = user
        super(Statistics_Window, self).__init__()
        uic.loadUi('Ui/statistics.ui', self)

        self.quitbutton.clicked.connect(self.backk)
        self.show()

        query = f"""select u.user_name,MAX(s.completed_level),ROW_NUMBER() OVER(order by MAX(s.completed_level) desc) as row_number from public."Users"  as u
join public."Statistics" as s on s.user_name = u.user_name
group by u.user_name"""
        info = db.cur.execute(query)
        info = db.cur.fetchall()
        print(info)
        #  info da kullanicilar (isim,maxlevel)

        for i in range(5):

            query2 = """select user_name , AVG(100*(knows/attemps::float))  as "ka" from public."Statistics"  
        where user_name ='%s'
        group by user_name""" % (info[i][0])
            info2 = db.cur.execute(query2)
            info2 = db.cur.fetchall()
            # info2 nin icine avaragelar (isim,oran) seklinde gelecek
            if i == 0:
                self.progressBar_menu_1.setProperty("value", (info2[0][1]))
            if i == 1:
                self.progressBar_menu_2.setProperty("value", (info2[0][1]))
            if i == 2:
                self.progressBar_menu_3.setProperty("value", (info2[0][1]))
            if i == 3:
                self.progressBar_menu_4.setProperty("value", (info2[0][1]))
            if i == 4:
                self.progressBar_menu_5.setProperty("value", (info2[0][1]))
            print(info2[0][1])
            i += 1

        self.linemax_1.setText(("    {}").format(info[0][1]))
        self.linemax_2.setText(("    {}").format(info[1][1]))
        self.linemax_3.setText(("    {}").format(info[2][1]))
        self.linemax_4.setText(("    {}").format(info[3][1]))
        self.linemax_5.setText(("    {}").format(info[4][1]))

        self.lineEdit_1.setText(("   1 st           {}").format(info[0][0]))
        self.lineEdit_2.setText(("   2 nd          {}").format(info[1][0]))
        self.lineEdit_3.setText(("   3 rd          {}").format(info[2][0]))
        self.lineEdit_4.setText(("   4 th          {}").format(info[3][0]))
        self.lineEdit_5.setText(("   5 th          {}").format(info[4][0]))
# anlik kullanici (vat yerine obje gelecek)
        for i in info:
            if i[0] == self.user.name:
                self.pushButton.setText(
                    ("You are in the  {} .  position.You  reached max. level  {}.").format(i[2], i[1]))
                if i[2] < 4:
                    self.pushButton.setText(
                        ("You are in the  {} .  position.You  reached max. level  {}. *** BRAVO! ***").format(i[2], i[1]))


# toplam kullanici
        query3 = """SELECT count(user_name)
FROM public."Users";"""
        info3 = db.cur.execute(query3)
        info3 = db.cur.fetchall()
        print(info3[0][0])
        self.mainmenu_label.setText(
            ("Numbers Of Players :   {} ".format(info3[0][0])))

    def backk(self):

        self.cams = menu.Menuscreen_window(self.user)
        self.cams.show()
        self.close()

    def total_procent():
        conn = psycopg2.connect(
            host="localhost",
            database="Flashcards",
            user='postgres',
            password="Alvo1.")
