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
        if str(self.answer) == str(self.lineEdit.text()):
            self.setTask()
        else:
            self.help_form = HelpForm(
                self.left, self.l_sys, self.r_sys, self.answer)
            self.help_form.body_text.setText(self.help_form.solution)
            self.help_form.show()
        self.lineEdit.setText("")
        self.lineEdit.setFocus()

    def setTask(self):
        self.left, self.l_sys, self.answer, self.r_sys = Functional.generate()
        self.label.setText(str(self.left))
        self.label_2.setText(str(self.r_sys))
        self.label_4.setText(str(self.l_sys))


class HelpForm(QtWidgets.QMainWindow, HelpWindow.Ui_MainWindow2):
    def __init__(self, left, l_sys, r_sys, answer):
        super().__init__()
        self.solution = ""
        self.answer = answer
        self.genSol(left, l_sys, r_sys)
        self.setupUi(self)

    def genSol(self, left, l_sys, r_sys):
        def parse_sixt_words():
            nums = []
            for char in str(left)[::-1]:
                if char.isnumeric():
                    nums.append(char)
                for num in range(10, 16):
                    if chr(87 + num) == char:
                        nums.append(num)
            return nums
        if r_sys == 10:
            if l_sys == 2 or l_sys == 8:
                left = str(left)[::-1]
                self.solution = "{first_rank}*{l_sys}^0".format(
                    first_rank=left[0], l_sys=l_sys)
                for i in range(1, len(str(left))):
                    self.solution += " + {rank}*{l_sys}^{degree}".format(
                        rank=left[i], l_sys=l_sys, degree=i)
            if l_sys == 16:
                parsed = parse_sixt_words()
                self.solution = "{first_rank}*{l_sys}^0".format(
                    first_rank=parsed[0], l_sys=l_sys)
                for i in range(1, len(parsed)):
                    self.solution += " + {rank}*{l_sys}^{degree}".format(
                        rank=parsed[i], l_sys=l_sys, degree=i)
            self.solution = to_10.format(left=left, solution=self.solution,
                                         answer=self.answer)
            return
        if l_sys == 10:
            temp_left = left
            while temp_left >= r_sys:
                self.solution += "\n{left}/{r_sys}={quotient}({remainder})".format(
                    left=temp_left, r_sys=r_sys, quotient=temp_left//r_sys, remainder=temp_left % r_sys)
                temp_left = temp_left//r_sys
            self.solution += "\n({remainder})\n".format(remainder=temp_left)
            self.solution = from_10.format(left=left, solution=self.solution,
                                           answer=self.answer)
            return
        if l_sys == 16 and (r_sys == 2 or r_sys == 8):
            blocks = []
            for char in left:
                if char.isalpha() or int(char) >= 8:
                    blocks.append(bin(int(char, base=16)).replace("0b", ""))
                if char.isnumeric() and int(char) < 8 and int(char) >= 4:
                    blocks.append(
                        "0" + bin(int(char, base=16)).replace("0b", ""))
                if char.isnumeric() and (int(char) == 3 or int(char) == 2):
                    blocks.append(
                        "00" + bin(int(char, base=16)).replace("0b", ""))
                if char.isnumeric() and (int(char) == 0 or int(char) == 1):
                    blocks.append("000" + char)
            self.solution += "|".join(blocks)
            if r_sys == 2:
                self.solution = from_16_to_2.format(left=left, solution=self.solution,
                                                    answer=self.answer)
            if r_sys == 8:
                blocks_str = "".join([p[::-1] for p in blocks[::-1]])
                blocks_str = blocks_str[::-1]
                if len(blocks_str) % 3 == 1:
                    blocks_str = "00" + blocks_str
                if len(blocks_str) % 3 == 2:
                    blocks_str = "0" + blocks_str
                blocks = [blocks_str[x:x+3]
                          for x in range(0, len(blocks_str), 3)]
                self.solution += "={}".format("|".join(blocks))
                self.solution = from_16_to_8.format(left=left, solution=self.solution,
                                                    answer=self.answer)
            return
        if l_sys == 8 and (r_sys == 2 or r_sys == 16):
            blocks = []
            for char in str(left):
                if int(char) < 8 and int(char) >= 4:
                    blocks.append(bin(int(char)).replace("0b", ""))
                if int(char) == 3 or int(char) == 2:
                    blocks.append("0" + bin(int(char)).replace("0b", ""))
                if int(char) == 0 or int(char) == 1:
                    blocks.append("00" + char)
            self.solution += "|".join(blocks)
            if r_sys == 2:
                self.solution = from_8_to_2.format(left=left, solution=self.solution,
                                                   answer=self.answer)
            if r_sys == 16:
                blocks_str = "".join([p[::-1] for p in blocks[::-1]])
                blocks_str = blocks_str[::-1]
                if len(blocks_str) % 4 == 1:
                    blocks_str = "000" + blocks_str
                if len(blocks_str) % 4 == 2:
                    blocks_str = "00" + blocks_str
                if len(blocks_str) % 4 == 3:
                    blocks_str = "0" + blocks_str
                blocks = [blocks_str[x:x+4]
                          for x in range(0, len(blocks_str), 4)]
                self.solution += "={}".format("|".join(blocks))
                self.solution = from_8_to_16.format(left=left, solution=self.solution,
                                                    answer=self.answer)
                return
        if l_sys == 2:
            if r_sys == 8:
                temp_left = str(left)[::-1]
                self.solution = temp_left[:3]
                temp_left = temp_left[3:]
                while len(temp_left) > 0:
                    self.solution += "|" + temp_left[:3]
                    temp_left = temp_left[3:]
                self.solution = self.solution[::-1]
                self.solution = from_2_to_8.format(left=left, solution=self.solution,
                                                   answer=self.answer)
            if r_sys == 16:
                temp_left = str(left)[::-1]
                self.solution = temp_left[:4]
                temp_left = temp_left[4:]
                while len(temp_left) > 0:
                    self.solution += "|" + temp_left[:4]
                    temp_left = temp_left[4:]
                self.solution = self.solution[::-1]
                self.solution = from_2_to_16.format(left=left, solution=self.solution,
                                                    answer=self.answer)
            return


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    window.setTask()
    app.exec_()


class Functional:
    @staticmethod
    def generate(systems=[2, 8, 10, 16]):
        num = random.randint(10, 255)
        l_sys = random.choice(systems)
        r_sys = random.choice(list(set(systems) - {l_sys}))
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
