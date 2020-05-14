from PyQt5 import QtCore, QtGui, QtWidgets  # импорт всего необходимого из графического модуля


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(500, 350)  # определение размера окна
        self.centralwidget = QtWidgets.QWidget(MainWindow)  # создание места, где всё будет размещено – центрального виджета
        MainWindow.setCentralWidget(self.centralwidget)  # присвоение центрального виджета главному окну
        font = QtGui.QFont("Roboto", 15)  # определение шрифта и его размера

        self.task_sys_label = QtWidgets.QLabel(self.centralwidget)  # создание строки для СС числа-задания
        self.task_sys_label.setGeometry(QtCore.QRect(185, 80, 25, 20))  # определение места и размера строки
        self.task_sys_label.setFont(font)  # определение шрифта строки
        self.answer_sys_label = QtWidgets.QLabel(self.centralwidget)  # создание строки для СС числа-ответа
        self.answer_sys_label.setGeometry(QtCore.QRect(400, 80, 25, 20))  # определение места и размера строки
        self.answer_sys_label.setFont(font)  # определение шрифта строки

        font.setPointSize(20)  # изменение размера шрифта
        self.task_num_label = QtWidgets.QLabel(self.centralwidget)  # создание строки для числа-задания
        self.task_num_label.setGeometry(QtCore.QRect(60, 50, 130, 30))  # определение места и размера строки
        self.task_num_label.setFont(font)  # определение шрифта строки
        self.task_num_label.setAlignment(QtCore.Qt.AlignRight)  # выравнивание по правому краю строки
        self.equals_sign = QtWidgets.QLabel(self.centralwidget)  # создание строки для знака равенства
        self.equals_sign.setGeometry(QtCore.QRect(235, 50, 30, 30))  # определение места и размера строки
        self.equals_sign.setFont(font)  # определение шрифта строки
        self.answer_num_label = QtWidgets.QLineEdit(self.centralwidget)  # создание поля для числа-ответа
        self.answer_num_label.setGeometry(QtCore.QRect(290, 50, 110, 30))  # определение места и размера поля
        self.answer_num_label.setFont(font)  # определение шрифта поля
        self.checkButton = QtWidgets.QPushButton(self.centralwidget)  # создание кнопки проверки
        self.checkButton.setGeometry(QtCore.QRect(165, 180, 155, 40))  # определение места и размера кнопки
        self.checkButton.setFont(font)  # определение шрифта кнопки

        self.retranslateUi(MainWindow)  # вызов функции, отображающей все постоянные данные

    def retranslateUi(self, MainWindow):  # функция, отображающая все постоянные данные
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate(
            "MainWindow", "Тренажёр по системам счисления"))  # отображение названия окна
        self.equals_sign.setText(_translate("MainWindow", "="))  # отображение знака равенства
        self.checkButton.setText(_translate("MainWindow", "Проверить"))  # отображение надписи на кнопке
        # все остальные данные будут сгенерированы в ходе работы программы