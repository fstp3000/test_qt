import sys
from PyQt5 import QtCore, QtWidgets

from window_0 import MainWindow
from window_1 import WindowTwo
from controller import Controller
def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

