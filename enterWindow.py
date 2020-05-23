import PyQt5.QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import connect
import startWindow
import sys


class EnterWindow(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(550, 300, 300, 160)
        self.setFixedSize(self.size())
        self.setWindowTitle('Авторизация')

        self.l1 = PyQt5.QtWidgets.QLabel('Логин:', self)
        self.l1.move(20, 30)
        self.l1 = PyQt5.QtWidgets.QLabel('Пароль:', self)
        self.l1.move(20, 60)

        self.lgnEdit = PyQt5.QtWidgets.QLineEdit(self)
        self.lgnEdit.move(100, 30)
        self.pswEdit = PyQt5.QtWidgets.QLineEdit(self)
        self.pswEdit.move(100, 60)
        self.pswEdit.setEchoMode(PyQt5.QtWidgets.QLineEdit.Password)

        self.btn = PyQt5.QtWidgets.QPushButton('Вход', self)
        self.btn.move(93, 100)
        self.btn.resize(140, 30)
        self.btn.clicked.connect(self.enterClicked)

        self.show()

    def enterClicked(self):
        login = self.lgnEdit.text()
        password = self.pswEdit.text()
        if len(login) == 0 or len(password) == 0:
            error_d = PyQt5.QtWidgets.QMessageBox()
            error_d.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
            error_d.setText("Введите логин и пароль")
            error_d.setWindowTitle("Ошибка!")
            error_d.exec_()
            return
        else:
            # try:
            con = connect.getDBconnection('c##daria', 'MyPass')
            curs = con.cursor()
            query = r"SELECT userpass from logins " \
                        r"where userlog = '{}'".format(login)
            curs.execute(query)
            l = curs.fetchall()
            check_pass = l[0][0]
            query = r"SELECT ORA_HASH('{}') from dual ".format(password)
            curs.execute(query)
            l = curs.fetchall()
            check_pass2 = l[0][0]
            if check_pass == str(check_pass2):
                self.startWindow = startWindow.StartWindow(con)
                self.close()
            else:
                error_d = PyQt5.QtWidgets.QMessageBox()
                error_d.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
                error_d.setText("Неверный логин/пароль!")
                error_d.setWindowTitle("Ошибка!")
                error_d.exec_()
                return

            # except:
            #     error_d = PyQt5.QtWidgets.QMessageBox()
            #     error_d.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
            #     error_d.setText("Ошибка! Что-то пошло не так...")
            #     error_d.setWindowTitle("Ошибка!")
            #     error_d.exec_()
            #     return
            print("Connection is successful")


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    enterWindow = EnterWindow()
    sys.exit(app.exec_())
