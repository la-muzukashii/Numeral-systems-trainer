from PyQt5 import QtCore, QtGui, QtWidgets  # импорт всего необходимого из модуля


class Ui_MainWindow2(object):
    def setupUi(self, HelpWindow):
        HelpWindow.resize(700, 350)  # определение размера окна
        self.centralwidget = QtWidgets.QWidget(HelpWindow)  # создание места, где всё будет размещено – центрального виджета
        HelpWindow.setCentralWidget(self.centralwidget)  # присвоение центрального виджета главному окну
        font = QtGui.QFont("Roboto", 12)  # определение шрифта и его размера

        self.help_label = QtWidgets.QLabel(self.centralwidget)  # создание строки для алгоритма и решения
        self.help_label.setMargin(50)  # создание отступов строки сверху и снизу
        self.help_label.setFont(font)  # определение шрифта строки

        self.retranslateUi(HelpWindow)  # вызов функции, отображающей все постоянные данные

    def retranslateUi(self, HelpWindow):
        _translate = QtCore.QCoreApplication.translate
        HelpWindow.setWindowTitle(_translate("HelpWindow", "Помощь"))  # отображение названия окна
        # все остальные данные будут меняться в ходе работы программы