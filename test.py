from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QMenu
print("hello_world")
app = QApplication([])
app.setStyle('Macintosh')
window = QWidget()

layout = QHBoxLayout()
b1 = QPushButton('Top')
b2 = QPushButton('Botton')
layout.addWidget(b1)
layout.addWidget(b2)

#menu = QPushButton.menu()
#menu = QMenu("hello_wolrd")
#b2.setMenu(menu)

def on_button_clicked():
    print("123")
def eventFilter(self, obj, event):
    if event.type() == QtCore.QEvent.KeyPress:
        print("keypress")

        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            return 1
        if event.key() == QtCore.Qt.Key_Tab:
            print("Tab")
            return 1

    return super().eventFilter(obj, event)


b2.clicked.connect(on_button_clicked)

window.setLayout(layout)
window.connect(eventFilter)

window.showMaximized()
#window.show()
app.exec_()
