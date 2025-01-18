import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox
from clock import Clock
from stoper import Stoper

def clock():
    clock = Clock()
    clock.show()
def stoper():
    stoper = Stoper()
    stoper.show()



class Menu(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        layout = QVBoxLayout()

        button1 = QPushButton('Clock')
        button1.clicked.connect(clock) #type: ignore
        layout.addWidget(button1)

        button2 = QPushButton('Stoper')
        button2.clicked.connect(stoper) #type: ignore
        layout.addWidget(button2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.exit(app.exec())



