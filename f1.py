from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QLineEdit, QVBoxLayout, QPushButton
class CompletableEdit(QLineEdit):
    ATTRNAME = '123' # must be set
    def __init__(self, parent=None):
        QLineEdit.__init__(self, parent=parent)
        #self.model = model
    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        if e.key() == Qt.Key_Return:
            self.close()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    w = CompletableEdit()
    w.show()
    app.exec_()
