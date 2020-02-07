import Form1
import random
import sys
import Form2
from Help import *

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot


class ExampleApp(QtWidgets.QMainWindow, Form1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.help_form = HelpForm()
        self.pushButton.clicked.connect(self.on_check_click)
        self.data = []

    @pyqtSlot()
    def on_check_click(self):
        self.data.append(str(self.answer) == str(self.lineEdit.text()))
        print(self.data, self.answer, self.lineEdit.text())
        print(all(self.data))
        self.lineEdit.clear()
        self.lineEdit.setFocus()
        if str(self.answer) == str(self.lineEdit.text()):
            pass
        else:
            self.help_form.genSol(self.left, self.l_sis, self.r_sis)
            self.help_form.setText(self.left, self.l_sis, self.r_sis)
            self.help_form.show()

    def setTask(self):
        self.left, self.l_sis, self.answer, self.r_sis = Functional.generate()
        self.label.setText(str(self.left))
        self.label_2.setText(str(self.r_sis))
        self.label_4.setText(str(self.l_sis))
        print(self.answer)


class HelpForm(QtWidgets.QMainWindow, Form2.Ui_MainWindow2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.solution=""
        self.answer=""
        
    def genSol(self, left, l_sis, r_sis):
       if r_sis == 10:
           if l_sis == 2 or l_sis == 8:
               left=str(left)[::-1]
               self.solution="{first_rank}*{l_sis}^0".format(first_rank=left[0], l_sis=l_sis)
               for i in range(1,len(str(left))):
                   self.solution += " + {rank}*{l_sis}^{degree}".format(rank=left[i], l_sis=l_sis, degree = i)

    def setText(self, left, solution, r_sis):
        self.body_text.setText(to_10.format(left=left, solution=self.solution, answer=self.answer))
            
           
def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    window.setTask()
    app.exec_()


class Functional:
    @staticmethod
    def generate():
        num = random.randint(0, 255)
        mas = [2, 8, 10, 16]
        l_sis = random.choice(mas)
        r_sis = random.choice(list(set(mas) - {l_sis}))
        return Functional.to_sis(num, l_sis), l_sis, Functional.to_sis(num, r_sis), r_sis

    @staticmethod
    def to_sis(num, syst):
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
