from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QRadioButton, QLabel, QPushButton, QScrollArea, QVBoxLayout
from PyQt5.QtGui import QIcon, QPixmap
import sys
from scanner import scanner


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(100, 100, 800, 620)
        self.setWindowTitle('test')
        self.initUI()

    #What goes inside our window
    def initUI(self):

        self.label = QtWidgets.QLabel(self)
        self.label.setText('Scan port number:')
        self.label.move(20, 20)
        self.label.setGeometry(10, 20, 200, 50)

        self.textbox = QLineEdit(self)
        self.textbox.move(20, 50)
        #self.texbox.resize(200, 32)


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Click me')
        self.b1.clicked.connect(self.clicked)
        #self.b1.resize(200, 32)
        self.b1.move(80,60)


    def clicked(self):
        self.label.setText('You pressed the button')

    def update(self):
        self.label.adjustSize()


def clicked():
    print("Clicked")

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()