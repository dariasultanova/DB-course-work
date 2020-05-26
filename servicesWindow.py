import PyQt5
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, \
    QMessageBox, QCheckBox
from PyQt5.QtGui import *


class servicesWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(270, 160, 900, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Услуги')

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

        self.name_label = QLabel('Название', self)
        self.name_label.move(545, 150)

        self.costour_label = QLabel('Стоимость для\nотчественной', self)
        self.costour_label.move(545, 200)

        self.costforeign_label = QLabel('Стоимость для\nиномарки', self)
        self.costforeign_label.move(545, 250)

        self.id_combobox = QComboBox(self)
        self.id_combobox.move(660, 100)
        self.id_combobox.resize(203, 20)
        self.id_combobox.currentIndexChanged.connect(self.id_changed)

        self.name_edit = QLineEdit(self)
        self.name_edit.move(665, 150)
        self.name_edit.resize(192, 20)

        self.costour_edit = QLineEdit(self)
        self.costour_edit.move(665, 200)
        self.costour_edit.resize(192, 20)

        self.costforeign_edit = QLineEdit(self)
        self.costforeign_edit.move(665, 250)
        self.costforeign_edit.resize(192, 20)

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
        self.table.setColumnCount(4)
        self.table.resize(520, 450)

        self.table.setColumnWidth(0, 40)
        self.table.setColumnWidth(1, 260)
        self.table.setColumnWidth(2, 100)
        self.table.setColumnWidth(3, 100)

        self.update_table()
        self.update_combobox()
        self.hide_all()

    def add_service(self):
        try:
            if int(self.costour_edit.text()) < 0 or int(self.costforeign_edit.text()) < 0:
                error_d = QMessageBox()
                error_d.setIcon(QMessageBox.Critical)
                error_d.setWindowTitle("Ошибка!")
                error_d.setText("Cтоимость не может быть меньше нуля")
                error_d.exec_()
                return
            if self.name_edit.text() and self.costour_edit.text() and self.costforeign_edit.text():

                cur = self.con.cursor()
                query = r"INSERT INTO services(name, cost_our, cost_foreign)" \
                        r" VALUES ('{}', '{}', '{}')".format(self.name_edit.text(),
                                                             float(self.costour_edit.text()),
                                                             float(self.costforeign_edit.text()))
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
            # print("Неизвестная ошибка!")
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Невозможно добавить новый автомобиль")
            error_d.exec_()

    def delete_service(self):
        try:
            cur = self.con.cursor()
            query = r"DELETE from services where ID = {}".format(int(self.id_combobox.currentText()))
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

    def update_service(self):
        try:
            cur = self.con.cursor()
            query = r"Update services set name = '{}'," \
                    r"cost_our = {}," \
                    r"cost_foreign = {} " \
                    r"where id = {}".format(self.name_edit.text(),
                                            self.costour_edit.text(),
                                            self.costforeign_edit.text(),
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
        cur.execute("select id from services order by id")
        l = cur.fetchall()
        for id in l:
            self.id_combobox.addItem(str(id[0]))

        self.id_combobox.setCurrentIndex(0)

    def update_table(self):
        cur = self.con.cursor()
        cur.execute('select count(*) from services')
        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Название', 'Стоимость для\nотчественной', 'Стоимость для\nиномарки'])
        cur.execute("select ID, name, cost_our, cost_foreign from services order by id")

        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 4):
                self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

    def update_edits(self):
        cur = self.con.cursor()
        if self.apply_btn.text() == 'Изменить':
            cur.execute('select * from services order by id')
            l = cur.fetchall()
            self.name_edit.setText(l[int(self.id_combobox.currentIndex())][1])
            self.costour_edit.setText(str(l[int(self.id_combobox.currentIndex())][2]))
            self.costforeign_edit.setText(str(l[int(self.id_combobox.currentIndex())][3]))

    def id_changed(self):
        self.update_edits()

    def add_clicked(self):
        self.hide_all()
        self.clear_all()

        self.title_label.setText('Введите новую услугу')
        self.title_label.show()

        self.name_label.show()
        self.costour_label.show()
        self.costforeign_label.show()

        self.name_edit.show()
        self.costour_edit.show()
        self.costforeign_edit.show()

        self.apply_btn.setText('Добавить')
        self.rollback_btn.setText('Отменить')
        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def modify_clicked(self):
        self.hide_all()
        self.clear_all()

        self.title_label.setText('Измените данные услуги')
        self.title_label.show()

        self.id_label.show()
        self.name_label.show()
        self.costour_label.show()
        self.costforeign_label.show()

        self.id_combobox.show()
        self.name_edit.show()
        self.costour_edit.show()
        self.costforeign_edit.show()
        self.update_combobox()

        self.apply_btn.setText('Изменить')
        self.rollback_btn.setText('Отменить')

        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def delete_clicked(self):
        self.hide_all()

        self.title_label.setText('Выберите ID услуги, чтобы удалить ее')
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
            self.add_service()
        elif self.apply_btn.text() == 'Удалить':
            self.delete_service()
        elif self.apply_btn.text() == 'Изменить':
            self.update_service()
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
        self.name_label.hide()
        self.costour_label.hide()
        self.costforeign_label.hide()

        self.id_combobox.hide()
        self.name_edit.hide()
        self.costour_edit.hide()
        self.costforeign_edit.hide()

        self.apply_btn.hide()
        self.rollback_btn.hide()
        self.commit_btn.hide()

    def clear_all(self):
        self.name_edit.clear()
        self.costour_edit.clear()
        self.costforeign_edit.clear()

