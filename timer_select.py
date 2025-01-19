import sys
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QDialog
from PyQt5.QtCore import Qt

class Wheel(QDialog):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.setWindowTitle('Select the time')
        self.setGeometry(300, 300, 500, 300)
        self.setStyleSheet("background-color: black; color: white;")
        layout = QVBoxLayout()

        label = QLabel("Select the time")
        label.setStyleSheet("""
        QLabel {
            background-color: black;
            color: white;
            font-size: 30px;
        }
        """)
        label.setAlignment(Qt.AlignCenter)
        layout.addWidget(label)

        self.hour_label = QLabel("Hours : ")
        self.hour_label.setStyleSheet("""
        QLabel {
        font-size: 20px;
        font-weight: bold;}
        """)
        self.minute_label = QLabel("Minutes : ")
        self.minute_label.setStyleSheet(self.hour_label.styleSheet())
        self.second_label = QLabel("Seconds : ")
        self.second_label.setStyleSheet(self.hour_label.styleSheet())

        self.hour_tumbler = self.create_tumbler(0,24)
        self.minutes_tumbler = self.create_tumbler(0,59)
        self.seconds_tumbler = self.create_tumbler(0,59)

        hbox = QHBoxLayout()
        hbox.addWidget(self.hour_label)
        hbox.addWidget(self.hour_tumbler)
        hbox.addWidget(self.minute_label)
        hbox.addWidget(self.minutes_tumbler)
        hbox.addWidget(self.second_label)
        hbox.addWidget(self.seconds_tumbler)

        layout.addLayout(hbox)

        button_layout = QHBoxLayout()
        self.ok_button = QPushButton('Ok')
        self.ok_button.setStyleSheet("""
            QPushButton {
            border: 2px solid white;
            min_width: 100px;
            min_height: 30px;
            padding: 15px;
            font-size: 20px;
            border-radius: 10px}
            QPushButton:hover {
                background-color: darkgray;
            }
        """)

        self.cancel_button = QPushButton('Cancel')
        self.cancel_button.setStyleSheet(self.ok_button.styleSheet())
        button_layout.addWidget(self.ok_button)
        button_layout.addWidget(self.cancel_button)

        layout.addLayout(button_layout)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept) #type: ignore
        self.cancel_button.clicked.connect(self.reject) #type: ignore

    def create_tumbler(self, min_value, max_value):
        combo = QComboBox()
        combo.addItems([f"{i:02}" for i in range(min_value, max_value + 1)])
        combo.setStyleSheet("""
             QComboBox {
                font-size: 20px;
                min-width: 50px;
                padding: 5px;
                border: 2px solid gray;
                border-radius: 5px;
                
            }
            QComboBox QAbstractItemView {
                selection-background-color: gray;
                font-size: 18px;
            }
            """)
        return combo
    def get_selected_time(self):
        hh = self.hour_tumbler.currentText()
        mm = self.minutes_tumbler.currentText()
        ss = self.seconds_tumbler.currentText()
        return f"{hh}:{mm}:{ss}"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    wheel = Wheel()
    wheel.show()
    sys.exit(app.exec())
