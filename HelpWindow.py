from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow2(object):
    def setupUi(self, MainWindow, text):
        MainWindow.setObjectName("Help Window")
        #MainWindow.resize(500, 350)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        font = QtGui.QFont()
        font.setPointSize(12)
        self.body_text = QtWidgets.QLabel(self.centralwidget)
        self.body_text.setMargin(50)
        #self.body_text.resize()
        self.body_text.setFont(font)
        self.body_text.setObjectName("body_text")
        self.body_text.setText(text)
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        print(self.body_text.width(), self.body_text.x())
        self.resize(self.body_text.width(), 350)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Help Window", "Help Window"))
