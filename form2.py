from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow2")
        MainWindow.resize(500, 350)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.body_text = QtWidgets.QLabel(self.centralwidget)
        self.body_text.setGeometry(QtCore.QRect(60, 50, 600, 200))
        self.body_text.setFont(font)
        self.body_text.setObjectName("body_text")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow2", "MainWindow2"))
        # self.body_text.setText(_translate("MainWindow2", "TEST"))
        # self.label.setText(_translate("MainWindow2", "11111111"))
