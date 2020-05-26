from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, \
    QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout, QTableWidget, QTableWidgetItem
from PyQt5.QtGui import *

import startWindow
import resultWindow


class proceduresWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.resultWindow = resultWindow.resultWindow(self.con)
        self.setGeometry(450, 160, 550, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Процедуры')

        '''Первая процедура'''
        first_btn = QPushButton('Средняя стоимость услуг по каждому автомобилю', self)
        first_btn.resize(500, 35)
        first_btn.move(25, 10)
        first_btn.setFont(QFont('Helvetica', 14))
        first_btn.clicked.connect(self.proc1)

        '''Вторая процедура'''
        second_btn = QPushButton('Общая стоимость услуги для автомобиля', self)
        second_btn.resize(500, 35)
        second_btn.move(25, 50)
        second_btn.setFont(QFont('Helvetica', 14))
        second_btn.clicked.connect(self.proc2)

        self.service_label = QLabel('Услуга', self)
        self.service_label.resize(200, 160)
        self.service_label.move(150, 205)
        self.service_label.hide()

        self.car_label = QLabel('Автомобиль', self)
        self.car_label.resize(200, 160)
        self.car_label.move(330, 205)
        self.car_label.hide()

        self.service_combobox = QComboBox(self)
        self.service_combobox.resize(200, 160)
        self.service_combobox.move(70, 225)
        self.service_combobox.hide()

        self.car_combobox = QComboBox(self)
        self.car_combobox.resize(200, 160)
        self.car_combobox.move(270, 225)
        self.car_combobox.hide()

        self.btn_show2 = QPushButton('Показать результат', self)
        self.btn_show2.resize(300, 40)
        self.btn_show2.move(125, 400)
        self.btn_show2.setFont(QFont('Helvetica', 14))
        self.btn_show2.hide()

        '''Третья процедура'''
        third_btn = QPushButton('Количество услуг, которые оказывали два мастера', self)
        third_btn.resize(500, 35)
        third_btn.move(25, 90)
        third_btn.setFont(QFont('Helvetica', 14))
        third_btn.clicked.connect(self.proc3)

        self.master1_label = QLabel('Первый мастер', self)
        self.master1_label.resize(200, 160)
        self.master1_label.move(120, 205)
        self.master1_label.hide()

        self.master2_label = QLabel('Второй мастер', self)
        self.master2_label.resize(200, 160)
        self.master2_label.move(315, 205)
        self.master2_label.hide()

        self.master1_combobox = QComboBox(self)
        self.master1_combobox.resize(200, 160)
        self.master1_combobox.move(70, 225)
        self.master1_combobox.hide()

        self.master2_combobox = QComboBox(self)
        self.master2_combobox.resize(200, 160)
        self.master2_combobox.move(270, 225)
        self.master2_combobox.hide()

        self.btn_show3 = QPushButton('Показать результат', self)
        self.btn_show3.resize(300, 40)
        self.btn_show3.move(125, 400)
        self.btn_show3.setFont(QFont('Helvetica', 14))
        self.btn_show3.hide()

        '''Четвертая процедура'''
        fourth_btn = QPushButton('Общая стоимость обслуживания отечественных и импортных автомобилей', self)
        fourth_btn.resize(500, 35)
        fourth_btn.move(25, 130)
        fourth_btn.setFont(QFont('Helvetica', 13))
        fourth_btn.clicked.connect(self.proc4)

        '''Пятая процедура'''
        fifth_btn = QPushButton('Пять мастеров, которые выполнили наибольшее число работ', self)
        fifth_btn.resize(500, 35)
        fifth_btn.move(25, 170)
        fifth_btn.setFont(QFont('Helvetica', 14))
        fifth_btn.clicked.connect(self.proc5)

        '''Курсор'''
        sixth_btn = QPushButton('Расчет премии', self)
        sixth_btn.resize(500, 35)
        sixth_btn.move(25, 210)
        sixth_btn.setFont(QFont('Helvetica', 14))
        sixth_btn.clicked.connect(self.proc6)

        self.master_label = QLabel('Мастер', self)
        self.master_label.resize(200, 160)
        self.master_label.move(150, 205)
        self.master_label.hide()

        self.salary_label = QLabel('Зарплата', self)
        self.salary_label.resize(200, 160)
        self.salary_label.move(330, 205)
        self.salary_label.hide()

        self.master_combobox = QComboBox(self)
        self.master_combobox.resize(200, 160)
        self.master_combobox.move(70, 225)
        self.master_combobox.hide()

        self.salary_edit = QLineEdit(self)
        self.salary_edit.resize(200, 20)
        self.salary_edit.move(270, 295)
        self.salary_edit.hide()

        self.btn_show6 = QPushButton('Показать результат', self)
        self.btn_show6.resize(300, 40)
        self.btn_show6.move(125, 400)
        self.btn_show6.setFont(QFont('Helvetica', 14))
        self.btn_show6.hide()

        back_btn = QPushButton('Вернуться в главное меню', self)
        back_btn.resize(300, 40)
        back_btn.move(125, 440)
        back_btn.setFont(QFont('Helvetica', 14))
        back_btn.clicked.connect(self.backToStart)

    def backToStart(self):
        self.procWindow = startWindow.StartWindow(self.con)
        self.close()

    def proc1(self):
        self.service_label.hide()
        self.service_combobox.hide()
        self.car_label.hide()
        self.car_combobox.hide()
        self.btn_show2.hide()

        self.master1_label.hide()
        self.master1_combobox.hide()
        self.master2_label.hide()
        self.master2_combobox.hide()
        self.btn_show3.hide()

        self.showRes1()

    def showRes1(self):
        self.resultWindow.show()
        cur = self.con.cursor()
        try:
            cur.callproc('avg_cost')
            self.resultWindow.update_table1()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!")
            error_d.exec_()
            return

    def proc2(self):
        self.master1_label.hide()
        self.master1_combobox.hide()
        self.master2_label.hide()
        self.master2_combobox.hide()
        self.btn_show3.hide()

        self.service_label.show()
        self.service_combobox.show()
        self.car_label.show()
        self.car_combobox.show()
        self.btn_show2.show()
        self.init_service_combobox()
        self.init_car_combobox()
        self.btn_show2.clicked.connect(self.showRes2)

    def init_service_combobox(self):
        cur = self.con.cursor()
        self.service_combobox.clear()
        cur.execute("select id, name from services order by id")
        l = cur.fetchall()
        for id in l:
            self.service_combobox.addItem(("{} - {}".format(id[0], id[1])))

        self.service_combobox.setCurrentIndex(0)

    def init_car_combobox(self):
        cur = self.con.cursor()
        self.car_combobox.clear()
        cur.execute("select id, num from cars order by id")
        l = cur.fetchall()
        for id in l:
            self.car_combobox.addItem(("{} - {}".format(id[0], id[1])))

        self.car_combobox.setCurrentIndex(0)

    def showRes2(self):
        self.resultWindow.show()
        cur = self.con.cursor()
        try:
            cur.callproc('service_cost_for_car',
                         [int(self.service_combobox.currentText().split()[0]),
                          int(self.car_combobox.currentText().split()[0])])

            query = r"select name from services where id = {}".format(self.service_combobox.currentText().split()[0])
            cur.execute(query)
            serv = cur.fetchall()

            query = r"select num from cars where id = {}".format(self.car_combobox.currentText().split()[0])
            cur.execute(query)
            car = cur.fetchall()

            self.resultWindow.text1 = serv[0][0]
            self.resultWindow.text2 = car[0][0]

            self.resultWindow.update_table2()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!")
            error_d.exec_()
            return

    def init_master1_combobox(self):
        cur = self.con.cursor()
        self.master1_combobox.clear()
        cur.execute("select id, name from masters order by id")
        l = cur.fetchall()
        for id in l:
            self.master1_combobox.addItem(("{} - {}".format(id[0], id[1])))

        self.master1_combobox.setCurrentIndex(0)

    def init_master2_combobox(self):
        cur = self.con.cursor()
        self.master2_combobox.clear()
        cur.execute("select id, name from masters order by id")
        l = cur.fetchall()
        for id in l:
            self.master2_combobox.addItem(("{} - {}".format(id[0], id[1])))

        self.master2_combobox.setCurrentIndex(0)

    def proc3(self):
        self.service_label.hide()
        self.service_combobox.hide()
        self.car_label.hide()
        self.car_combobox.hide()
        self.btn_show2.hide()

        self.master1_label.show()
        self.master1_combobox.show()
        self.master2_label.show()
        self.master2_combobox.show()
        self.btn_show3.show()
        self.init_master1_combobox()
        self.init_master2_combobox()
        self.btn_show3.clicked.connect(self.showRes3)

    def showRes3(self):
        self.resultWindow.show()
        cur = self.con.cursor()
        try:
            cur.callproc('number_of_services',
                         [int(self.master1_combobox.currentText().split()[0]),
                          int(self.master2_combobox.currentText().split()[0])])

            query = r"select name from masters where id = {}".format(self.master1_combobox.currentText().split()[0])
            cur.execute(query)
            m1 = cur.fetchall()

            query = r"select name from masters where id = {}".format(self.master2_combobox.currentText().split()[0])
            cur.execute(query)
            m2 = cur.fetchall()

            self.resultWindow.text3 = m1[0][0]
            self.resultWindow.text4 = m2[0][0]

            self.resultWindow.update_table3()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!")
            error_d.exec_()
            return

    def proc4(self):
        self.service_label.hide()
        self.service_combobox.hide()
        self.car_label.hide()
        self.car_combobox.hide()
        self.btn_show2.hide()

        self.master1_label.hide()
        self.master1_combobox.hide()
        self.master2_label.hide()
        self.master2_combobox.hide()
        self.btn_show3.hide()

        self.showRes4()

    def showRes4(self):
        self.resultWindow.show()
        cur = self.con.cursor()
        try:
            cur.callproc('total_cost')
            self.resultWindow.update_table4()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!")
            error_d.exec_()
            return

    def proc5(self):
        self.service_label.hide()
        self.service_combobox.hide()
        self.car_label.hide()
        self.car_combobox.hide()
        self.btn_show2.hide()

        self.master1_label.hide()
        self.master1_combobox.hide()
        self.master2_label.hide()
        self.master2_combobox.hide()
        self.btn_show3.hide()

        self.showRes5()

    def showRes5(self):
        self.resultWindow.show()
        cur = self.con.cursor()
        try:
            cur.callproc('top5')
            self.resultWindow.update_table5()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!")
            error_d.exec_()
            return

    def init_master_combobox(self):
        cur = self.con.cursor()
        self.master_combobox.clear()
        cur.execute("select id, name from masters order by id")
        l = cur.fetchall()
        for id in l:
            self.master_combobox.addItem(("{} - {}".format(id[0], id[1])))

        self.master_combobox.setCurrentIndex(0)

    def proc6(self):
        self.service_label.hide()
        self.service_combobox.hide()
        self.car_label.hide()
        self.car_combobox.hide()
        self.btn_show2.hide()

        self.master1_label.hide()
        self.master1_combobox.hide()
        self.master2_label.hide()
        self.master2_combobox.hide()
        self.btn_show3.hide()

        self.master_label.show()
        self.master_combobox.show()
        self.salary_label.show()
        self.salary_edit.show()
        self.btn_show6.show()
        self.init_master_combobox()
        self.btn_show6.clicked.connect(self.showRes6)

    def showRes6(self):
        self.resultWindow.show()
        cur = self.con.cursor()
        cur.execute(
            "ALTER SESSION SET NLS_DATE_FORMAT = 'DD-MM-YYYY'"
            " NLS_TIMESTAMP_FORMAT = 'DD-MM-YYYY'")
        try:
            cur.callproc('bonus',
                     [int(self.master_combobox.currentText().split()[0]),
                      int(self.salary_edit.text())])

            query = r"select name from masters where id = {}".format(self.master_combobox.currentText().split()[0])
            cur.execute(query)
            m = cur.fetchall()

            self.resultWindow.text5 = m[0][0]

            self.resultWindow.update_table6()
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка вызова процедуры!")
            error_d.exec_()
            return
