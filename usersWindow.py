from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, \
    QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import *

class usersWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(270, 160, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Пользователи')

        self.add_btn = QPushButton('Добавить пользователя', self)
        self.add_btn.move(20, 460)
        self.add_btn.resize(200, 30)
        self.add_btn.clicked.connect(self.add_clicked)

        self.delete_btn = QPushButton('Удалить пользователя', self)
        self.delete_btn.move(310, 460)
        self.delete_btn.resize(200, 30)
        self.delete_btn.clicked.connect(self.delete_clicked)

        self.title_label = QLabel('', self)
        self.title_label.move(570, 30)
        self.title_label.setFont(QFont('Helvetica', 14))

        self.title_label_delete = QLabel('', self)
        self.title_label_delete.move(570, 30)
        self.title_label_delete.setFont(QFont('Helvetica', 14))

        self.login_label = QLabel('Логин', self)
        self.login_label.move(570, 100)

        self.password_label = QLabel('Пароль', self)
        self.password_label.move(570, 150)

        self.login_combobox = QComboBox(self)
        self.login_combobox.move(675, 100)
        self.login_combobox.resize(163, 20)
        self.login_edit = QLineEdit(self)
        self.login_edit.move(680, 300)
        self.login_edit.resize(150, 20)

        self.password = QLineEdit(self)
        self.password.move(680, 150)
        self.password.resize(150, 20)

        self.login = QLineEdit(self)
        self.login.move(680, 100)
        self.login.resize(150, 20)

        self.apply_btn1 = QPushButton('', self)
        self.apply_btn1.move(673, 200)
        self.apply_btn1.resize(165, 30)

        self.commit_btn = QPushButton('Сохранить', self)
        self.commit_btn.move(570, 460)
        self.commit_btn.resize(150, 30)
        self.commit_btn.clicked.connect(self.commit_clicked)

        self.rollback_btn = QPushButton('Отменить', self)
        self.rollback_btn.move(740, 460)
        self.rollback_btn.resize(150, 30)
        self.rollback_btn.clicked.connect(self.rollback_clicked)
        self.apply_btn1.clicked.connect(self.apply1_clicked)

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(520, 450)
        self.table.setColumnWidth(0, 250)
        self.table.setColumnWidth(1, 250)

        self.update_table()
        self.update_combobox()
        self.hide_all()

    def update_table(self):
        cur = self.con.cursor()
        cur.execute('select count(*) from logins')
        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['Логин', 'Хешированный пароль'])
        cur.execute('select * from logins order by userlog')

        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 2):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

    def add_clicked(self):
        self.hide_all()

        self.title_label.setText('Введите данные нового пользователя')
        self.title_label.show()
        self.login_label.show()
        self.password_label.show()

        self.login.show()
        self.password.show()

        self.apply_btn1.setText('Добавить')
        self.rollback_btn.setText('Отменить')
        self.apply_btn1.show()
        self.rollback_btn.show()
        self.commit_btn.show()
        ##self.update_combobox()

    def delete_clicked(self):
        self.login.clear()
        self.password.clear()
        self.hide_all()

        self.title_label_delete.setText('Удалите пользователя')

        self.title_label_delete.show()

        self.login_label.show()

        self.login_combobox.show()

        self.apply_btn1.setText('Удалить')
        self.rollback_btn.setText('Отменить')

        self.apply_btn1.show()

        self.rollback_btn.show()
        self.commit_btn.show()
        self.update_combobox()

    def update_combobox(self):
        cur = self.con.cursor()
        self.login_combobox.clear()
        cur.execute("select userlog from logins order by userlog")
        l = cur.fetchall()
        for id in l:
            self.login_combobox.addItem('{}'.format(id[0]))

        self.login_combobox.setCurrentIndex(0)

    def hide_all(self):
        self.title_label.setVisible(False)
        self.title_label_delete.setVisible(False)

        self.login_label.setVisible(False)
        self.password_label.setVisible(False)

        self.login_combobox.hide()
        self.password.hide()
        self.login.hide()
        self.login_edit.hide()

        self.apply_btn1.hide()
        self.rollback_btn.hide()
        self.commit_btn.hide()
       ##self.update_table()

    def apply1_clicked(self):
        if self.apply_btn1.text() == 'Добавить':
            self.add_user()
            self.login.clear()
            self.password.clear()
        elif self.apply_btn1.text() == 'Удалить':
            self.delete_user()


    def commit_clicked(self):
        self.con.commit()

    def rollback_clicked(self):
        self.con.rollback()
        self.update_table()
        self.update_combobox()

    def delete_user(self):
        try:
            cur = self.con.cursor()
            query = r"delete from logins where userlog = '{}'".format(self.login_combobox.currentText())
            cur.execute(query)
            self.update_table()
            self.update_combobox()
            self.update_table()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setText("Ошибка удаления данных!")

    def add_user(self):
        try:
            if self.login.text() and self.password.text():
                curs = self.con.cursor()
                query =r"INSERT INTO logins (userlog, userpass) " \
                       r"VALUES ('{}', ORA_HASH('{}'))".format(self.login.text(), self.password.text())

                curs.execute(query)
                self.update_table()
            else:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setText("Заполните все поля!")
                error_d.setWindowTitle("Ошибка!")
                error_d.exec_()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Пользователь с таким именем уже существует!")
            error_d.exec_()
            return
