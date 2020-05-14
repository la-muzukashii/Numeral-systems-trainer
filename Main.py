import random  # импорт модуля-рандомизатора
import sys

# импорт всего необходимого из графического модуля
from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot

import HelpWindow, MainWindow  # импорт окон
from Help import *  # импорт всех переменных из файла с решениями


class Functional:
    @staticmethod
    def genTask(systems=[2, 8, 10, 16]):  # функция, в которой генерируются переменные задания
        task_num = random.randint(10, 255)  # модуль random выбирает число-задание
        task_sys = random.choice(systems)  # модуль random выбирает СС числа-задания
        answer_sys = random.choice(list(set(systems) - {task_sys}))  # модуль random выбирает СС числа-ответа
        return Functional.to_syst(task_num, task_sys), task_sys, Functional.to_syst(task_num, answer_sys), answer_sys # функция
        #                   возвращает число-задание и число-ответ, переведённые в заданные СС другой функцией, а также сами СС

    @staticmethod
    def to_syst(num, syst):  # функция, переводящая число-задание и число-ответ в заданные СС
        if syst == 2:
            return int(bin(num).replace('0b', ''))
        if syst == 8:
            return int(oct(num).replace('0o', ''))
        if syst == 16:
            return hex(num).replace('0x', '')
        if syst == 10:
            return num


class Help(QtWidgets.QMainWindow, HelpWindow.Ui_MainWindow2):  # всё, что касается вспомогательного окна:
    def __init__(self, task_num, task_sys, answer_sys, answer_num):  # функция инициализации
        super().__init__()
        self.solution = ""
        self.answer_num = answer_num
        self.genSolution(task_num, task_sys, answer_sys)  # вызов функции, в которой генерируется решение для окна "Помощь"
        self.setupUi(self)

    def genSolution(self, task_num, task_sys, answer_sys):  # функция, в которой генерируется решение для окна "Помощь"
        if answer_sys == 10:  # если СС числа-ответа равна десяти:
            if task_sys == 2 or task_sys == 8:  # если СС числа-задания равна двум или 8:
                task_num = str(task_num)[::-1]
                self.solution = "{first_rank}*{task_sys}^0".format(
                    first_rank=task_num[0], task_sys=task_sys)
                for i in range(1, len(str(task_num))):
                    self.solution += " + {rank}*{task_sys}^{degree}".format(
                        rank=task_num[i], task_sys=task_sys, degree=i)
            if task_sys == 16:  # если СС числа-задания равна шестнадцати:
                nums = []
                for char in str(task_num)[::-1]:
                    if char.isnumeric():
                        nums.append(char)
                    for num in range(10, 16):
                        if chr(87 + num) == char:
                            nums.append(num)
                self.solution = "{first_rank}*{task_sys}^0".format(
                    first_rank=nums[0], task_sys=task_sys)
                for i in range(1, len(nums)):
                    self.solution += " + {rank}*{task_sys}^{degree}".format(
                        rank=nums[i], task_sys=task_sys, degree=i)
            self.solution = to_10.format(task_num=task_num, solution=self.solution,
                                         answer_num=self.answer_num)
            return
        if task_sys == 10:  # если СС числа-задания равна десяти:
            temp_task_num = task_num
            while temp_task_num >= answer_sys:
                self.solution += "\n{task_num}/{answer_sys}={quotient}({remainder})".format(
                    task_num=temp_task_num, answer_sys=answer_sys,quotient=temp_task_num//answer_sys,
                    remainder=temp_task_num % answer_sys)
                temp_task_num = temp_task_num//answer_sys
            self.solution += "\n({remainder})\n".format(remainder=temp_task_num)
            self.solution = from_10.format(task_num=task_num, solution=self.solution,
                                           answer_num=self.answer_num)
            return
        if task_sys == 16 and (answer_sys == 2 or answer_sys == 8):  # если СС числа-задания равна шестнадцати и СС
        #                                                                                   числа-ответа равна двум или восьми:
            blocks = []
            for char in task_num:
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
            if answer_sys == 2:  # если СС числа-ответа равна двум:
                self.solution = from_16_to_2.format(task_num=task_num, solution=self.solution,
                                                    answer_num=self.answer_num)
            if answer_sys == 8:  # если СС числа-ответа равна восьми:
                blocks_str = "".join([p[::-1] for p in blocks[::-1]])
                blocks_str = blocks_str[::-1]
                if len(blocks_str) % 3 == 1:
                    blocks_str = "00" + blocks_str
                if len(blocks_str) % 3 == 2:
                    blocks_str = "0" + blocks_str
                blocks = [blocks_str[x:x+3]
                          for x in range(0, len(blocks_str), 3)]
                self.solution += "={}".format("|".join(blocks))
                self.solution = from_16_to_8.format(task_num=task_num, solution=self.solution,
                                                    answer_num=self.answer_num)
            return
        if task_sys == 8 and (answer_sys == 2 or answer_sys == 16):  # если СС числа-задания равна восьми и СС числа-ответа
        #                                                                                           равна двум или шестнадцати:
            blocks = []
            for char in str(task_num):
                if int(char) < 8 and int(char) >= 4:
                    blocks.append(bin(int(char)).replace("0b", ""))
                if int(char) == 3 or int(char) == 2:
                    blocks.append("0" + bin(int(char)).replace("0b", ""))
                if int(char) == 0 or int(char) == 1:
                    blocks.append("00" + char)
            self.solution += "|".join(blocks)
            if answer_sys == 2:  # если СС числа-ответа равна двум:
                self.solution = from_8_to_2.format(task_num=task_num, solution=self.solution,
                                                   answer_num=self.answer_num)
            if answer_sys == 16:  # если СС числа-ответа равна шестнадцати:
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
                self.solution = from_8_to_16.format(task_num=task_num, solution=self.solution,
                                                    answer_num=self.answer_num)
                return
        if task_sys == 2:  # если СС числа-задания равна двум:
            if answer_sys == 8:  # если СС числа-ответа равна восьми:
                temp_task_num = str(task_num)[::-1]
                self.solution = temp_task_num[:3]
                temp_task_num = temp_task_num[3:]
                while len(temp_task_num) > 0:
                    self.solution += "|" + temp_task_num[:3]
                    temp_task_num = temp_task_num[3:]
                self.solution = self.solution[::-1]
                self.solution = from_2_to_8.format(task_num=task_num, solution=self.solution,
                                                   answer_num=self.answer_num)
            if answer_sys == 16:  # если СС числа-ответа равна шестнадцати:
                temp_task_num = str(task_num)[::-1]
                self.solution = temp_task_num[:4]
                temp_task_num = temp_task_num[4:]
                while len(temp_task_num) > 0:
                    self.solution += "|" + temp_task_num[:4]
                    temp_task_num = temp_task_num[4:]
                self.solution = self.solution[::-1]
                self.solution = from_2_to_16.format(task_num=task_num, solution=self.solution,
                                                    answer_num=self.answer_num)
            return


class Main(QtWidgets.QMainWindow, MainWindow.Ui_MainWindow):  # всё, что касается главного окна:
    def __init__(self):  # функция инициализации
        super().__init__()
        self.setupUi(self)
        self.checkButton.clicked.connect(self.click_on_checkButton)  # подключение кнопки к функции

    @pyqtSlot()
    def click_on_checkButton(self):  # функция, в которой описывается, что происходит при нажатии на кнопку "Проверить"
        if str(self.answer_num) == str(self.answer_num_label.text()):  # если текст в поле для ввода совпадает с числом-ответом:
            self.setTask()  # создаётся новое задание
        else:  # иначе:
            self.help_window = Help(
                self.task_num, self.task_sys, self.answer_sys, self.answer_num)
            self.help_window.help_label.setText(self.help_window.solution)  # заполнение строки с алгоритмом и решением
            self.help_window.show()  # открытие окна "Помощь"
        self.answer_num_label.setText("")  # очистка поля для ввода
        self.answer_num_label.setFocus()  # фокусировка на поле для ввода

    def setTask(self):  # функция, в которой строкам главного окна присваиваются переменные задания
        self.task_num, self.task_sys, self.answer_num, self.answer_sys = Functional.genTask()  # получение переменных из
        #                                                                                          функции генератора "genTask"
        self.task_num_label.setText(str(self.task_num))  # присваивание строке для числа-задания этого числа
        self.answer_sys_label.setText(str(self.answer_sys))  # присваивание строке для СС числа-ответа этой СС
        self.task_sys_label.setText(str(self.task_sys))  # присваивание строке для СС числа-задания этой СС


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()  # открытие окна
    window.setTask()  # вызов функции, в которой строкам главного окна присваиваются переменные задания
    app.exec_()


if __name__ == "__main__":
    main()