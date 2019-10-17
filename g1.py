from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QLineEdit, QVBoxLayout, QPushButton, QHBoxLayout
class CompletableEdit(QLineEdit):
    ATTRNAME = '123' # must be set
    def __init__(self, parent=None):
        #super().__init__(self, parent=parent)
        super().__init__()
    def keyPressEvent(self, e):
        super().keyPressEvent(e)
        if e.key() == Qt.Key_Return:
            print("1223")
            #self.setFocusPolicy(Qt.NoFocus)
            self.focusNextChild()



if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    layout = QHBoxLayout()
    b1 = CompletableEdit()
    b2 = CompletableEdit()
    b3 = CompletableEdit()
    layout.addWidget(b1)
    layout.addWidget(b2)
    layout.addWidget(b3)
    w = QWidget()
    w.setLayout(layout)
    w.show()
    app.exec_()
