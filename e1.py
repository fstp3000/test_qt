from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow
class Ui_MainWindow(QWidget,object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(200, 200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 110, 75, 23))
        self.pushButton.setObjectName("pushButton")


        #self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #def retranslateUi(self, MainWindow):
    #    _translate = QtCore.QCoreApplication.translate
    #    MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
    #    self.pushButton.setText(_translate("MainWindow", "PushButton"))\

    #def keyPressEvent(self, e):
    #    if e.key() == Qt.Key_Enter:
    #self.close()
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent=parent)
        self.setupUi(self)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Return:
            self.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = MainWindow()
    w.show()
    app.exec_()
