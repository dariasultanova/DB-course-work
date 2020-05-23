from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget, QPushButton, QToolTip, QLabel, QComboBox, QLineEdit, QErrorMessage, QMessageBox, QRadioButton, QGroupBox, QVBoxLayout
from PyQt5.QtGui import *

import carsWindow
import connect
import enterWindow
import mastersWindow
import servicesWindow
import usersWindow
import worksWindow


class StartWindow(QWidget):
    def __init__(self, con):
        super().__init__()
        self.con = con
        self.setGeometry(520, 300, 400, 200)
        self.setFixedSize(self.size())
        self.setWindowTitle('Главное меню')

        # self.procWindow = procedureWindow.procWindow(self.con)
        self.worksWindow = worksWindow.worksWindow(self.con)
        self.carsWindow = carsWindow.carsWindow(self.con)
        self.mastersWindow = mastersWindow.mastersWindow(self.con)
        self.servicesWindow = servicesWindow.servicesWindow(self.con)
        self.usersWindow = usersWindow.usersWindow(self.con)

        titleLabel = QLabel('Выберите таблицу', self)
        titleLabel.move(135, 30)
        titleLabel.setFont(QFont('Helvetica', 14))

        self.main_comb = QComboBox(self)
        self.main_comb.move(100, 60)
        self.main_comb.resize(200, 40)
        self.init_main_comb()
        self.main_comb.setFont(QFont('Helvetica', 14))
        self.main_comb.currentIndexChanged.connect(self.id_changed)
        self.main_comb.show()

        logout_btn = QPushButton('Выход', self)
        logout_btn.setToolTip('Log out')
        logout_btn.resize(100, 100)
        logout_btn.move(140, 150)
        logout_btn.resize(130, 35)
        logout_btn.setFont(QFont('Helvetica', 14))
        logout_btn.clicked.connect(self.LogOutButtonClicked)
        self.show()

    def init_main_comb(self):
        self.main_comb.clear()
        self.main_comb.addItems(['Мастера', 'Автомобили', 'Услуги', 'Работы', 'Пользователи'])
        self.main_comb.setCurrentIndex(0)

    def LogOutButtonClicked(self):
        self.close()
        self.mastersWindow.close()
        self.carsWindow.close()
        self.servicesWindow.close()
    #     self.procWindow.close()
        self.worksWindow.close()
        self.enterWindow = enterWindow.EnterWindow()
        connect.shutDownConnection(self.con)
        self.enterWindow.show()

    def id_changed(self):
        if self.main_comb.currentText() == 'Мастера':
            self.MastersButtonClicked()
        if self.main_comb.currentText() == 'Автомобили':
            self.CarsButtonClicked()
        if self.main_comb.currentText() == 'Услуги':
            self.ServicesButtonClicked()
        if self.main_comb.currentText() == 'Работы':
            self.WorksButtonClicked()
        if self.main_comb.currentText() == 'Пользователи':
            self.UsersButtonClicked()
        # if self.main_comb.currentText() == 'Процедуры':
        #     self.ProcButtonClicked()
        # self.update_edits()

    def MastersButtonClicked(self):
        self.mastersWindow.show()

        if self.carsWindow.isVisible():
            self.carsWindow.close()

        if self.servicesWindow.isVisible():
            self.servicesWindow.close()

        if self.worksWindow.isVisible():
            self.worksWindow.close()

        if self.usersWindow.isVisible():
            self.usersWindow.close()

    def CarsButtonClicked(self):
        self.carsWindow.show()

        if self.mastersWindow.isVisible():
            self.mastersWindow.close()

        if self.servicesWindow.isVisible():
            self.servicesWindow.close()

        if self.worksWindow.isVisible():
            self.worksWindow.close()

        if self.usersWindow.isVisible():
            self.usersWindow.close()

    def ServicesButtonClicked(self):
        self.servicesWindow.show()

        if self.mastersWindow.isVisible():
            self.mastersWindow.close()

        if self.carsWindow.isVisible():
            self.carsWindow.close()

        if self.worksWindow.isVisible():
            self.worksWindow.close()

        if self.usersWindow.isVisible():
            self.usersWindow.close()

    def WorksButtonClicked(self):
        self.worksWindow.show()

        if self.mastersWindow.isVisible():
            self.mastersWindow.close()

        if self.carsWindow.isVisible():
            self.carsWindow.close()

        if self.servicesWindow.isVisible():
            self.servicesWindow.close()

        if self.usersWindow.isVisible():
            self.usersWindow.close()

    def UsersButtonClicked(self):
        self.usersWindow.show()

        if self.mastersWindow.isVisible():
            self.mastersWindow.close()

        if self.carsWindow.isVisible():
            self.carsWindow.close()

        if self.servicesWindow.isVisible():
            self.servicesWindow.close()

        if self.worksWindow.isVisible():
            self.worksWindow.close()


