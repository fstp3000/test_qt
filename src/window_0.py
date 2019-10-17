import sys
from PyQt5 import QtCore, QtWidgets

class MainWindow(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Main Window')
        self.layout = QtWidgets.QGridLayout()
        self.line_edit = QtWidgets.QLineEdit()
        self.layout.addWidget(self.line_edit)
        self.button = QtWidgets.QPushButton('Switch Window')
        #self.button.clicked.connect(self.switch)
        #button1 = QPushButton(text='button caption', objectName='button1', clicked=someMethod)
        self.button.clicked.connect(self.addBottom)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def switch(self):
        self.switch_window.emit(self.line_edit.text())
    def addBottom(self):
        self.button2 = QtWidgets.QPushButton(text = 'add botton', objectName =
                                             'button1')
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)
        for i in range(self.layout.count()):
            print(self.layout.itemAt(i).widget().objectName())
