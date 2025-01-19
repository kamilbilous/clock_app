import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox, QHBoxLayout, QStackedWidget
from clock import Clock
from stoper import Stoper
from timer import Timer





class Menu(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Menu")
        self.setGeometry(800, 300, 800, 600)
        self.setStyleSheet("background-color:black; color: white;")

        self.stack = QStackedWidget(self)
        self.back_buttons = {}

        self.main_menu = QWidget(self)
        self.init_main_menu()

        self.clock_widget = Clock()
        self.timer_widget = Timer()
        self.stopwatch_widget = Stoper()

        self.stack.addWidget(self.main_menu)
        self.stack.addWidget(self.clock_widget)
        self.stack.addWidget(self.timer_widget)
        self.stack.addWidget(self.stopwatch_widget)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)
    def init_main_menu(self):
        layout = QVBoxLayout()

        self.label = QLabel("Main Menu")
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setStyleSheet("font-size: 40px; font-weight: bold;")
        layout.addWidget(self.label)

        hbox = QHBoxLayout()

        self.clock_button = QPushButton("Clock")
        self.timer_button = QPushButton("Timer")
        self.stopwatch_button = QPushButton("Stopwatch")



        hbox.addWidget(self.clock_button)
        self.clock_button.setStyleSheet(""" 
            QPushButton {
                border: 2px solid white;
                min-width: 100px;
                min-height: 30px;
                padding: 15px;
                font-size: 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: darkgray;
            }
        """)
        hbox.addWidget(self.timer_button)
        self.timer_button.setStyleSheet(self.clock_button.styleSheet())
        hbox.addWidget(self.stopwatch_button)
        self.stopwatch_button.setStyleSheet(self.clock_button.styleSheet())

        layout.addLayout(hbox)
        self.main_menu.setLayout(layout)

        self.clock_button.clicked.connect(lambda: self.show_page(self.clock_widget))#type: ignore
        self.timer_button.clicked.connect(lambda: self.show_page(self.timer_widget))#type: ignore
        self.stopwatch_button.clicked.connect(lambda: self.show_page(self.stopwatch_widget))#type: ignore

    def show_page(self, widget):
        self.stack.setCurrentWidget(widget)
        self.add_back_button(widget)

    def add_back_button(self, widget):
        if widget not in self.back_buttons:
            back_button = QPushButton("Back")
            back_button.setStyleSheet("""
            QPushButton {
                border: 2px solid white;
                min-width: 100px;
                min-height: 30px;
                padding: 15px;
                font-size: 20px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: darkgray;
            }
        """)
            back_button.clicked.connect(lambda: self.stack.setCurrentWidget(self.main_menu))#type: ignore


            layout = widget.layout() or QVBoxLayout(widget)
            layout.addWidget(back_button)
            widget.setLayout(layout)


            self.back_buttons[widget] = back_button




if __name__ == '__main__':
    app = QApplication(sys.argv)
    menu = Menu()
    menu.show()
    sys.exit(app.exec())



