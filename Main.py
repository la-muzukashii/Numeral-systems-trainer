import random
import sys

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

import HelpWindow
import MainWindow
from Help import *


class Main(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.on_check_click)
        self.data = []

    @pyqtSlot()
    def on_check_click(self):
        self.data.append(str(self.answer) == str(self.lineEdit.text()))
        #print(self.data, self.answer, self.lineEdit.text())
        #print(all(self.data))
        self.lineEdit.clear()
        self.lineEdit.setFocus()
        if str(self.answer) == str(self.lineEdit.text()):
            pass
        else:
            self.help_form = HelpForm(
                self.left, self.l_sys, self.r_sys, self.answer)
            self.help_form.show()

    def setTask(self):
        self.left, self.l_sys, self.answer, self.r_sys = Functional.generate()
        self.label.setText(str(self.left))
        self.label_2.setText(str(self.r_sys))
        self.label_4.setText(str(self.l_sys))
        print(self.answer)


class HelpForm(QtWidgets.QMainWindow, HelpWindow.Ui_MainWindow2):
    def __init__(self, left, l_sys, r_sys, answer):
        super().__init__()
        text = self.genSol(left, l_sys, r_sys)
        self.setupUi(self, to_10.format(
            left=left, solution=text, answer=answer))
        self.solution = ""
        self.answer = ""

    def genSol(self, left, l_sys, r_sys):
        if r_sys == 10:
            if l_sys == 2 or l_sys == 8:
                left = str(left)[::-1]
                self.solution = "{first_rank}*{l_sys}^0".format(
                    first_rank=left[0], l_sys=l_sys)
                for i in range(1, len(str(left))):
                    self.solution += " + {rank}*{l_sys}^{degree}".format(
                        rank=left[i], l_sys=l_sys, degree=i)
        return self.solution


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    window.setTask()
    app.exec_()


class Functional:
    @staticmethod
    def generate():
        num = random.randint(0, 255)
        mas = [2, 8, 10, 16]
        l_sys = random.choice(mas)
        r_sys = random.choice(list(set(mas) - {l_sys}))
        return Functional.to_sys(num, l_sys), l_sys, Functional.to_sys(num, r_sys), r_sys

    @staticmethod
    def to_sys(num, syst):
        if syst == 2:
            return int(bin(num).replace('0b', ''))
        if syst == 8:
            return int(oct(num).replace('0o', ''))
        if syst == 16:
            return hex(num).replace('0x', '')
        if syst == 10:
            return num


if __name__ == "__main__":
    main()
