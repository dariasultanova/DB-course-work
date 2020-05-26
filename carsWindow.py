import PyQt5
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, \
    QMessageBox, QCheckBox
from PyQt5.QtGui import *


class carsWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(270, 160, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Автомобили')

        self.add_btn = QPushButton('Добавить', self)
        self.add_btn.move(20, 460)
        self.add_btn.resize(150, 30)
        self.add_btn.clicked.connect(self.add_clicked)

        self.modify_btn = QPushButton('Изменить', self)
        self.modify_btn.move(190, 460)
        self.modify_btn.resize(150, 30)
        self.modify_btn.clicked.connect(self.modify_clicked)

        self.delete_btn = QPushButton('Удалить', self)
        self.delete_btn.move(360, 460)
        self.delete_btn.resize(150, 30)
        self.delete_btn.clicked.connect(self.delete_clicked)

        self.title_label = QLabel('', self)
        self.title_label.resize(300, 30)
        self.title_label.move(545, 30)
        self.title_label.setFont(QFont('Helvetica', 14))

        self.id_label = QLabel('ID', self)
        self.id_label.move(545, 100)

        self.num_label = QLabel('Номер', self)
        self.num_label.move(545, 150)

        self.color_label = QLabel('Цвет', self)
        self.color_label.move(545, 200)

        self.mark_label = QLabel('Марка', self)
        self.mark_label.move(545, 250)

        self.isforeign_label = QLabel('Иностранная', self)
        self.isforeign_label.move(545, 300)

        self.id_combobox = QComboBox(self)
        self.id_combobox.move(660, 100)
        self.id_combobox.resize(203, 20)
        self.id_combobox.currentIndexChanged.connect(self.id_changed)

        self.num_edit = QLineEdit(self)
        self.num_edit.move(665, 150)
        self.num_edit.resize(192, 20)

        self.color_edit = QLineEdit(self)
        self.color_edit.move(665, 200)
        self.color_edit.resize(192, 20)

        self.mark_edit = QLineEdit(self)
        self.mark_edit.move(665, 250)
        self.mark_edit.resize(192, 20)

        self.isforeign_box = QLineEdit(self)
        self.isforeign_box.move(665, 300)
        self.isforeign_box.resize(192, 20)

        self.apply_btn = QPushButton('', self)
        self.apply_btn.move(740, 420)
        self.apply_btn.resize(150, 30)
        self.apply_btn.clicked.connect(self.apply_clicked)

        self.commit_btn = QPushButton('Сохранить', self)
        self.commit_btn.move(570, 460)
        self.commit_btn.resize(150, 30)
        self.commit_btn.clicked.connect(self.commit_clicked)

        self.rollback_btn = QPushButton('Отменить', self)
        self.rollback_btn.move(740, 460)
        self.rollback_btn.resize(150, 30)
        self.rollback_btn.clicked.connect(self.rollback_clicked)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.resize(520, 450)

        self.table.setColumnWidth(0, 50)
        self.table.setColumnWidth(1, 120)
        self.table.setColumnWidth(2, 120)
        self.table.setColumnWidth(3, 110)

        self.update_table()
        self.update_combobox()
        self.hide_all()

    def add_car(self):
        try:
            if self.num_edit.text() and self.color_edit.text() and self.mark_edit.text() and self.isforeign_box.text():

                cur = self.con.cursor()
                query =r"INSERT INTO cars(num, color, mark, is_foreign)" \
                       r" VALUES ('{}', '{}', '{}', {})".format(self.num_edit.text(),
                                                                  self.color_edit.text(),
                                                                  self.mark_edit.text(),
                                                                  int(self.isforeign_box.text()))
                cur.execute(query)
                self.update_table()
                self.clear_all()
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
            error_d.setText("Невозможно добавить новый автомобиль")
            error_d.exec_()

    def delete_car(self):
        try:
            cur = self.con.cursor()
            query = r"DELETE from cars where ID = {}".format(int(self.id_combobox.currentText()))
            cur.execute(query)
            self.update_table()
            self.update_combobox()
            self.update_table()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка удаления данных")
            error_d.setText("Невозможно удалить автомобиль!")
            error_d.exec_()

    def update_car(self):
        try:
            cur = self.con.cursor()
            query = r"Update cars set num = '{}'," \
                    r"color = '{}'," \
                    r"mark = '{}'," \
                    r"is_foreign = {} " \
                    r"where id = {} ".format(self.num_edit.text(),
                                            self.color_edit.text(),
                                            self.mark_edit.text(),
                                            self.isforeign_box.text(),
                                            int(self.id_combobox.currentText()))
            cur.execute(query)

            self.update_combobox()
            self.update_table()
            self.clear_all()
            self.update_edits()
        except:
            error_d = PyQt5.QtWidgets.QMessageBox()
            error_d.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
            error_d.setText("Ошибка обновления данных!\n Повторите попытку позднее")
            error_d.setWindowTitle("Ошибка!")
            error_d.exec_()

    def update_combobox(self):
        cur = self.con.cursor()
        self.id_combobox.clear()
        cur.execute("select id from cars order by id")
        l = cur.fetchall()
        for id in l:
            self.id_combobox.addItem(str(id[0]))

        self.id_combobox.setCurrentIndex(0)

    def update_table(self):
        cur = self.con.cursor()
        cur.execute('select count(*) from cars')
        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Номер', 'Цвет', 'Марка', 'И/О'])
        cur.execute("select ID, num, color, mark, is_foreign from cars order by id")

        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 5):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

    def update_edits(self):
        cur = self.con.cursor()
        if self.apply_btn.text() == 'Изменить':
            cur.execute('select * from cars order by id')
            l = cur.fetchall()
            self.num_edit.setText(l[int(self.id_combobox.currentIndex())][1])
            self.color_edit.setText(l[int(self.id_combobox.currentIndex())][2])
            self.mark_edit.setText(l[int(self.id_combobox.currentIndex())][3])
            self.isforeign_box.setText(str(l[int(self.id_combobox.currentIndex())][4]))

    def id_changed(self):
        self.update_edits()

    def add_clicked(self):
        self.hide_all()
        self.clear_all()

        self.title_label.setText('Введите новый автомобиль')
        self.title_label.show()

        self.num_label.show()
        self.color_label.show()
        self.mark_label.show()
        self.isforeign_label.show()

        self.num_edit.show()
        self.color_edit.show()
        self.mark_edit.show()
        self.isforeign_box.show()

        self.apply_btn.setText('Добавить')
        self.rollback_btn.setText('Отменить')
        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def modify_clicked(self):
        self.hide_all()
        self.clear_all()

        self.title_label.setText('Измените данные автомобиля')
        self.title_label.show()

        self.id_label.show()
        self.num_label.show()
        self.color_label.show()
        # self.mark_label.show()
        # self.isforeign_label.show()

        self.id_combobox.show()
        self.num_edit.show()
        self.color_edit.show()
        # self.mark_edit.show()
        # self.isforeign_box.show()
        self.update_combobox()

        self.apply_btn.setText('Изменить')
        self.rollback_btn.setText('Отменить')

        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def delete_clicked(self):
        self.hide_all()

        self.title_label.setText('Выберите ID автомобиля, чтобы удалить его')
        self.title_label.show()

        self.id_combobox.show()
        self.id_label.show()
        self.update_combobox()

        self.apply_btn.setText('Удалить')
        self.rollback_btn.setText('Отменить')

        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def apply_clicked(self):
        if self.apply_btn.text() == 'Добавить':
            self.add_car()
        elif self.apply_btn.text() == 'Удалить':
            self.delete_car()
        elif self.apply_btn.text() == 'Изменить':
            self.update_car()
        self.update_combobox()
        self.update_edits()
        self.update_table()

    def commit_clicked(self):
        self.con.commit()
        self.update_combobox()
        self.update_edits()

    def rollback_clicked(self):
        self.con.rollback()
        self.update_table()
        self.update_combobox()

    def hide_all(self):
        self.title_label.hide()
        self.id_label.hide()
        self.num_label.hide()
        self.color_label.hide()
        self.mark_label.hide()
        self.isforeign_label.hide()

        self.id_combobox.hide()
        self.num_edit.hide()
        self.color_edit.hide()
        self.mark_edit.hide()
        self.isforeign_box.hide()

        self.apply_btn.hide()
        self.rollback_btn.hide()
        self.commit_btn.hide()

    def clear_all(self):
        self.num_edit.clear()
        self.color_edit.clear()
        self.mark_edit.clear()
        self.isforeign_box.clear()
