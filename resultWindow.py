from PyQt5.QtWidgets import QTableWidget, QWidget, QPushButton, QMessageBox, QTableWidgetItem
from PyQt5.QtGui import *

class resultWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(450, 160, 550, 500)
        self.setFixedSize(self.size())
        self.setWindowTitle('Результат')
        self.text1 = ''
        self.text2 = ''
        self.text3 = ''
        self.text4 = ''
        self.text5 = ''

        self.write1_btn = QPushButton('Записать в файл', self)
        self.write1_btn.resize(500, 40)
        self.write1_btn.move(25, 450)
        self.write1_btn.setFont(QFont('Helvetica', 14))

        self.write2_btn = QPushButton('Записать в файл', self)
        self.write2_btn.resize(500, 40)
        self.write2_btn.move(25, 450)
        self.write2_btn.setFont(QFont('Helvetica', 14))

        self.write3_btn = QPushButton('Записать в файл', self)
        self.write3_btn.resize(500, 40)
        self.write3_btn.move(25, 450)
        self.write3_btn.setFont(QFont('Helvetica', 14))

        self.write4_btn = QPushButton('Записать в файл', self)
        self.write4_btn.resize(500, 40)
        self.write4_btn.move(25, 450)
        self.write4_btn.setFont(QFont('Helvetica', 14))

        self.write5_btn = QPushButton('Записать в файл', self)
        self.write5_btn.resize(500, 40)
        self.write5_btn.move(25, 450)
        self.write5_btn.setFont(QFont('Helvetica', 14))

        self.write6_btn = QPushButton('Записать в файл', self)
        self.write6_btn.resize(500, 40)
        self.write6_btn.move(25, 450)
        self.write6_btn.setFont(QFont('Helvetica', 14))

    def update_table1(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(3)
        self.table.resize(486, 450)
        self.table.move(32, 0)
        self.write2_btn.hide()
        self.write3_btn.hide()
        self.write4_btn.hide()
        self.write5_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from avg_cost_tbl')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setColumnWidth(0, 148)
            self.table.setColumnWidth(1, 160)
            self.table.setColumnWidth(2, 160)
            self.table.setHorizontalHeaderLabels(['Номер автомобиля', 'Марка', 'Средняя стоимость услуг'])
            cur.execute("select * from avg_cost_tbl")

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            # print(ll)
            for i in range(0, self.N_ROWS):
                for j in range(0, 3):
                    # if j == 2 & (str(ll[i][j]) != 'None'):
                    #     self.table.setItem(i, j, QTableWidgetItem(str(round(float(ll[i][j]), 1))))
                    # else:
                        self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.write1_btn.show()
            self.write1_btn.clicked.connect(self.click1)
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!")
            error_d.exec_()
            return

    def click1(self):
        f = open('1.txt', 'w')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def update_table2(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(486, 420)
        self.table.move(32, 0)
        self.write1_btn.hide()
        self.write3_btn.hide()
        self.write4_btn.hide()
        self.write5_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from service_cost_for_car_tbl')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setHorizontalHeaderLabels(['Общая стоимость', 'Количество'])
            cur.execute("select sum, quantity from service_cost_for_car_tbl")
            self.table.setColumnWidth(0, 235)
            self.table.setColumnWidth(1, 235)

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 2):
                    self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.write2_btn.show()
            self.write2_btn.clicked.connect(self.click2)
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!")
            error_d.exec_()
            return

    def click2(self):
        f = open('2.txt', 'w')
        f.write("Общая стоимость и количество работ по услуге '{}'\n"
                "для автомобиля с номером '{}'".format(self.text1, self.text2))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def update_table3(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(486, 450)
        self.table.move(32, 0)
        self.write1_btn.hide()
        self.write2_btn.hide()
        self.write4_btn.hide()
        self.write5_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from number_of_services_tbl')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setHorizontalHeaderLabels(["Количество услуг, которые оказали "
                                                  "{} и {}".format(self.text3, self.text4)])
            cur.execute("select * from number_of_services_tbl")
            self.table.setColumnWidth(0, 470)

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 1):
                        self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.write3_btn.show()
            self.write3_btn.clicked.connect(self.click3)
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!")
            error_d.exec_()
            return

    def click3(self):
        f = open('3.txt', 'w')
        f.write("Количество услуг, которые оказали мастер {} и мастер {}".format(self.text3, self.text4))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def update_table4(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(486, 450)
        self.table.move(32, 0)
        self.write1_btn.hide()
        self.write2_btn.hide()
        self.write3_btn.hide()
        self.write5_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from total_cost_tbl')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setColumnWidth(0, 470)
            self.table.setHorizontalHeaderLabels(['Общая стоимость обслуживания отечественных и импортных автомобилей'])
            cur.execute("select * from total_cost_tbl")

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            # print(ll)
            for i in range(0, self.N_ROWS):
                for j in range(0, 1):
                    self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.write4_btn.show()
            self.write4_btn.clicked.connect(self.click4)
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!")
            error_d.exec_()
            return

    def click4(self):
        f = open('4.txt', 'w')
        f.write("Общая стоимость обслуживания отечественных и импортных автомобилей")
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def update_table5(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.resize(486, 450)
        self.table.move(32, 0)
        self.write1_btn.hide()
        self.write2_btn.hide()
        self.write3_btn.hide()
        self.write4_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from top5_tbl')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setColumnWidth(0, 235)
            self.table.setColumnWidth(1, 233)
            self.table.setHorizontalHeaderLabels(['Имя', 'Количество работ'])
            cur.execute("select * from top5_tbl")

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            # print(ll)
            for i in range(0, self.N_ROWS):
                for j in range(0, 2):
                     self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.write5_btn.show()
            self.write5_btn.clicked.connect(self.click5)
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!")
            error_d.exec_()
            return

    def click5(self):
        f = open('5.txt', 'w')
        f.write("Пять мастеров, которые выполнили наибольшее число работ")
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

    def update_table6(self):
        self.table = QTableWidget(self)
        self.table.setColumnCount(1)
        self.table.resize(486, 450)
        self.table.move(32, 0)
        self.write1_btn.hide()
        self.write2_btn.hide()
        self.write3_btn.hide()
        self.write4_btn.hide()
        self.write5_btn.hide()
        cur = self.con.cursor()
        try:
            cur.execute('select count(*) from bonus_tbl')
            self.N_ROWS = cur.fetchone()[0]
            self.table.setRowCount(self.N_ROWS)
            self.table.setHorizontalHeaderLabels(["Зарплата + премия мастеру {} ".format(self.text5)])
            cur.execute("select * from bonus_tbl")
            self.table.setColumnWidth(0, 470)

            self.l = cur.fetchall()
            ll = []
            for el in self.l:
                ll.append(list(el))
            for i in range(0, self.N_ROWS):
                for j in range(0, 1):
                        self.table.setItem(i, j, QTableWidgetItem(str(ll[i][j])))

            self.table.show()
            self.write6_btn.show()
            self.write6_btn.clicked.connect(self.click6)
        except:
            error_d = QMessageBox()
            error_d.setIcon(QMessageBox.Critical)
            error_d.setWindowTitle("Ошибка!")
            error_d.setText("Ошибка Загрузки данных!")
            error_d.exec_()
            return

    def click6(self):
        f = open('6.txt', 'w')
        f.write("Зарплата + премия мастеру {} ".format(self.text5))
        f.write('\n')
        for id in self.l:
            f.writelines(str(id))
            f.write('\n')
        f.close()

