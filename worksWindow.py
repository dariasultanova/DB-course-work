import PyQt5
from PyQt5.QtWidgets import QWidget, QPushButton, QLabel, QComboBox, QLineEdit, QTableWidget, QTableWidgetItem, \
    QMessageBox
from PyQt5.QtGui import *


class worksWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(220, 160, 1000, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Работы')

        self.add_btn = QPushButton('Добавить', self)
        self.add_btn.move(20, 460)
        self.add_btn.resize(150, 30)
        self.add_btn.clicked.connect(self.add_clicked)

        self.modify_btn = QPushButton('Изменить', self)
        self.modify_btn.move(220, 460)
        self.modify_btn.resize(150, 30)
        self.modify_btn.clicked.connect(self.modify_clicked)

        self.delete_btn = QPushButton('Удалить', self)
        self.delete_btn.move(410, 460)
        self.delete_btn.resize(150, 30)
        self.delete_btn.clicked.connect(self.delete_clicked)

        self.title_label = QLabel('', self)
        self.title_label.resize(300, 30)
        self.title_label.move(615, 30)
        self.title_label.setFont(QFont('Helvetica', 14))

        self.id_label = QLabel('ID', self)
        self.id_label.move(615, 100)

        self.work_label = QLabel('Дата работы', self)
        self.work_label.move(615, 150)

        self.master_label = QLabel('Мастер', self)
        self.master_label.move(615, 200)

        self.car_label = QLabel('Номер\nавтомобиля', self)
        self.car_label.move(615, 250)

        self.service_label = QLabel('Услуга', self)
        self.service_label.move(615, 300)

        self.id_combobox = QComboBox(self)
        self.id_combobox.move(760, 100)
        self.id_combobox.resize(203, 20)
        self.id_combobox.currentIndexChanged.connect(self.id_changed)

        self.work_edit = QLineEdit(self)
        self.work_edit.move(765, 150)
        self.work_edit.resize(192, 20)

        self.master_combobox = QComboBox(self)
        self.master_combobox.move(760, 200)
        self.master_combobox.resize(203, 20)

        self.car_combobox = QComboBox(self)
        self.car_combobox.move(760, 250)
        self.car_combobox.resize(203, 20)

        self.service_combobox = QComboBox(self)
        self.service_combobox.move(760, 300)
        self.service_combobox.resize(203, 20)

        self.apply_btn = QPushButton('', self)
        self.apply_btn.move(817, 420)
        self.apply_btn.resize(150, 30)
        self.apply_btn.clicked.connect(self.apply_clicked)

        self.commit_btn = QPushButton('Сохранить', self)
        self.commit_btn.move(615, 460)
        self.commit_btn.resize(150, 30)
        self.commit_btn.clicked.connect(self.commit_clicked)

        self.rollback_btn = QPushButton('Отменить', self)
        self.rollback_btn.move(817, 460)
        self.rollback_btn.resize(150, 30)
        self.rollback_btn.clicked.connect(self.rollback_clicked)

        self.table = QTableWidget(self)
        self.table.setColumnCount(5)
        self.table.resize(570, 450)

        self.table.setColumnWidth(0, 35)
        self.table.setColumnWidth(1, 90)
        self.table.setColumnWidth(2, 140)
        self.table.setColumnWidth(3, 85)
        self.table.setColumnWidth(4, 195)

        self.update_table()
        self.update_id_combobox()
        self.update_master_combobox()
        self.update_car_combobox()
        self.update_service_combobox()
        self.hide_all()

    def getMasterId(self):
        cur = self.con.cursor()
        query = r"select id from masters where name = '{}'".format(self.master_combobox.currentText())
        cur.execute(query)
        master = cur.fetchall()
        master_id = master[0][0]
        return master_id

    def getCarId(self):
        cur = self.con.cursor()
        query = r"select id from cars where num = '{}'".format(self.car_combobox.currentText())
        cur.execute(query)
        car = cur.fetchall()
        car_id = car[0][0]
        return car_id

    def getServiceId(self):
        cur = self.con.cursor()
        query = r"select id from services where name = '{}'".format(self.service_combobox.currentText())
        cur.execute(query)
        service = cur.fetchall()
        service_id = service[0][0]
        return service_id

    def add_work(self):
        self.clear_all()
        try:
            if self.work_edit.text():

                cur = self.con.cursor()
                query = r"INSERT INTO works(date_work, master_id, car_id, service_id)" \
                        r" VALUES (TO_DATE('{}', 'YYYY-MM-DD'), {}, {}, {})".format(self.work_edit.text(),
                                                                                int(self.getMasterId()),
                                                                                int(self.getCarId()),
                                                                                int(self.getServiceId()))
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
            error_d.setText("Невозможно добавить работу!")
            error_d.exec_()

    def delete_work(self):
        try:
            cur = self.con.cursor()
            query = r"DELETE from works where ID = {}".format(int(self.id_combobox.currentText()))
            cur.execute(query)
            self.update_table()
            self.update_id_combobox()
            self.update_master_combobox()
            self.update_car_combobox()
            self.update_service_combobox()
            self.update_table()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка удаления данных!")
            error_d.setText("Ошибка!")
            error_d.exec_()

    def update_work(self):
        try:

            cur = self.con.cursor()
            query = r"Update works set date_work = TO_DATE('{}', 'YYYY-MM-DD')," \
                    r"master_id = {}," \
                    r"car_id = {}," \
                    r"service_id = {}" \
                    r"where id = {}".format(self.work_edit.text(),
                                            int(self.getMasterId()),
                                            int(self.getCarId()),
                                            int(self.getServiceId()),
                                            int(self.id_combobox.currentText()))
            cur.execute(query)

            self.update_id_combobox()
            self.update_master_combobox()
            self.update_car_combobox()
            self.update_service_combobox()
            self.update_table()
            self.clear_all()
            self.update_edits()
        except:
            error_d = PyQt5.QtWidgets.QMessageBox()
            error_d.setIcon(PyQt5.QtWidgets.QMessageBox.Critical)
            error_d.setText("Ошибка обновления данных!")
            error_d.setWindowTitle("Ошибка!")
            error_d.exec_()

    def update_id_combobox(self):
        cur = self.con.cursor()
        self.id_combobox.clear()
        cur.execute("select id from works order by id")
        l = cur.fetchall()
        for id in l:
            self.id_combobox.addItem(str(id[0]))

        self.id_combobox.setCurrentIndex(0)

    def update_master_combobox(self):
        cur = self.con.cursor()
        self.master_combobox.clear()

        cur.execute("select name from masters")
        l = cur.fetchall()
        for id in l:
            self.master_combobox.addItem(("{}".format(id[0])))

        self.master_combobox.setCurrentIndex(0)

    def update_car_combobox(self):
        cur = self.con.cursor()
        self.car_combobox.clear()

        cur.execute("select num from cars")
        l = cur.fetchall()
        for id in l:
            self.car_combobox.addItem(("{}".format(id[0])))

        self.car_combobox.setCurrentIndex(0)

    def update_service_combobox(self):
        cur = self.con.cursor()
        self.service_combobox.clear()

        cur.execute("select name from services")
        l = cur.fetchall()
        for id in l:
            self.service_combobox.addItem(("{}".format(id[0])))

        self.service_combobox.setCurrentIndex(0)

    def update_table(self):
        cur = self.con.cursor()
        cur.execute('select count(*) from works')
        self.N_ROWS = cur.fetchone()[0]
        self.table.setRowCount(self.N_ROWS)
        self.table.setHorizontalHeaderLabels(['ID', 'Дата работы', 'Мастер', 'Номер\nавтомобиля', 'Услуга'])
        cur.execute("select works.ID, date_work, masters.name, cars.num, services.name from works "
                    "join masters on works.master_id = masters.id "
                    "join cars on works.car_id = cars.id "
                    "join services on works.service_id = services.id "
                    "order by id")

        l = cur.fetchall()
        ll = []
        for el in l:
            ll.append(list(el))
        for i in range(0, self.N_ROWS):
            for j in range(0, 5):
                if j == 1:
                    self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j]).split()[0]))
                else:
                    self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

    def update_edits(self):
        cur = self.con.cursor()
        if self.apply_btn.text() == 'Изменить':
            cur.execute("select works.ID, date_work, masters.name, cars.num, services.name from works "
                        "join masters on works.master_id = masters.id "
                        "join cars on works.car_id = cars.id "
                        "join services on works.service_id = services.id "
                        "order by id")
            l = cur.fetchall()
            self.work_edit.setText(str(l[int(self.id_combobox.currentIndex())][1]).split()[0])
            self.master_combobox.setCurrentText(str(l[int(self.id_combobox.currentIndex())][2]))
            self.car_combobox.setCurrentText(str(l[int(self.id_combobox.currentIndex())][3]))
            self.service_combobox.setCurrentText(str(l[int(self.id_combobox.currentIndex())][4]))

    def id_changed(self):
        self.update_edits()

    def add_clicked(self):
        self.hide_all()
        self.clear_all()

        self.apply_btn.hide()
        self.rollback_btn.hide()
        self.commit_btn.hide()

        self.title_label.setText('Введите новую работу')
        self.title_label.show()

        self.work_label.show()
        self.master_label.show()
        self.car_label.show()
        self.service_label.show()

        self.work_edit.show()
        self.master_combobox.show()
        self.car_combobox.show()
        self.service_combobox.show()

        self.apply_btn.setText('Добавить')
        self.rollback_btn.setText('Отменить')
        self.update_id_combobox()
        self.update_master_combobox()
        self.update_car_combobox()
        self.update_service_combobox()
        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def modify_clicked(self):
        self.hide_all()
        self.clear_all()

        self.title_label.setText('Измените данные по работе')
        self.title_label.show()

        self.id_label.show()
        self.work_label.show()
        self.master_label.show()
        self.car_label.show()
        self.service_label.show()

        self.id_combobox.show()
        self.work_edit.show()
        self.master_combobox.show()
        self.car_combobox.show()
        self.service_combobox.show()
        self.update_id_combobox()
        cur = self.con.cursor()
        cur.execute("select works.ID, date_work, masters.name, cars.num, services.name from works "
                    "join masters on works.master_id = masters.id "
                    "join cars on works.car_id = cars.id "
                    "join services on works.service_id = services.id "
                    "order by id")
        l = cur.fetchall()
        self.work_edit.setText(str(l[int(self.id_combobox.currentIndex())][1]).split()[0])
        self.master_combobox.setCurrentText(str(l[int(self.id_combobox.currentIndex())][2]))
        self.car_combobox.setCurrentText(str(l[int(self.id_combobox.currentIndex())][3]))
        self.service_combobox.setCurrentText(str(l[int(self.id_combobox.currentIndex())][4]))

        self.apply_btn.setText('Изменить')
        self.rollback_btn.setText('Отменить')
        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def delete_clicked(self):
        self.hide_all()

        self.title_label.setText('Выберите ID работы, чтобы удалить ее')
        self.title_label.show()

        self.id_combobox.show()
        self.id_label.show()
        self.update_id_combobox()

        self.apply_btn.setText('Удалить')
        self.rollback_btn.setText('Отменить')

        self.apply_btn.show()
        self.rollback_btn.show()
        self.commit_btn.show()

    def apply_clicked(self):
        if self.apply_btn.text() == 'Добавить':
            self.add_work()
        elif self.apply_btn.text() == 'Удалить':
            self.delete_work()
        elif self.apply_btn.text() == 'Изменить':
            self.update_work()
        self.update_id_combobox()
        self.update_master_combobox()
        self.update_car_combobox()
        self.update_service_combobox()
        self.update_edits()
        self.update_table()

    def commit_clicked(self):
        self.con.commit()
        self.update_id_combobox()
        self.update_master_combobox()
        self.update_car_combobox()
        self.update_service_combobox()
        self.update_edits()

    def rollback_clicked(self):
        self.con.rollback()
        self.update_table()
        self.update_id_combobox()
        self.update_master_combobox()
        self.update_car_combobox()
        self.update_service_combobox()

    def hide_all(self):
        self.title_label.hide()
        self.id_label.hide()
        self.work_label.hide()
        self.master_label.hide()
        self.car_label.hide()
        self.service_label.hide()

        self.id_combobox.hide()
        self.work_edit.hide()
        self.master_combobox.hide()
        self.car_combobox.hide()
        self.service_combobox.hide()

        self.apply_btn.hide()
        self.rollback_btn.hide()
        self.commit_btn.hide()

    def clear_all(self):
        self.work_edit.clear()
