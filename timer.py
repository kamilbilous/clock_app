import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from timer_select import Wheel
#TODO: Add sound on timer hitting 0
#TODO: Diff styles

class Timer(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0,0,0)
        self.time_label = QLabel("00:00:00",self)
        self.error_label = QLabel("",self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.set_button =QPushButton("Set Time", self)
        self.timer = QTimer()
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Timer")
        self.setGeometry(800, 300, 500, 300)
        self.setStyleSheet("background-color:black; color:white")
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.time_label.setStyleSheet("""
            QLabel {
            font-size: 50px;
            font-weight: bold;
            }
        """)
        self.time_label.setAlignment(Qt.AlignCenter)
        vbox.addWidget(self.error_label)
        self.error_label.setStyleSheet("""
                    QLabel {
                        font-size: 30px;
                        color: red;
                        font-weight: bold;
                    }
                """)
        self.error_label.setAlignment(Qt.AlignCenter)
        self.setLayout(vbox)
        self.set_button.setStyleSheet("""
        QPushButton {
        font-size: 20px;
        border: 2px solid white;
        border-radius: 10px
        }
        QPushButton:hover {
        background-color: grey;
        }
        """)
        self.start_button.setStyleSheet("""
                QPushButton {
                border: 2px solid white;
                min_width: 100px;
                min_height: 30px;
                padding: 15px;
                font-size: 20px;
                border-radius: 10px}
                QPushButton:hover {
                background-color: grey;
                }
                """)
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        self.start_button.setStyleSheet(self.start_button.styleSheet())
        self.stop_button.setStyleSheet(self.start_button.styleSheet())
        self.reset_button.setStyleSheet(self.start_button.styleSheet())

        vbox.addLayout(hbox)
        self.set_button.clicked.connect(self.open_tumbler) #type: ignore
        self.start_button.clicked.connect(self.start)  # type: ignore
        self.stop_button.clicked.connect(self.stop)  # type: ignore
        self.reset_button.clicked.connect(self.reset)  # type: ignore
        self.timer.timeout.connect(self.update_display) #type: ignore
    def start(self):
        if not self.timer.isActive() and self.time > QTime(0,0,0):
            self.timer.start(1000)
            self.error_label.setText("")
        elif self.time == QTime(0,0,0):
            self.error_label.setText("! Timer can't start at 0 !")
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
        self.error_label.setText("")
    def format_time(self, time_or_string):
        if isinstance(time_or_string, QTime):
            return time_or_string.toString("hh:mm:ss")
        else:
            return QTime.fromString(time_or_string, "hh:mm:ss")

    def update_display(self):
        if self.time > QTime(0, 0, 0):
            self.time = self.time.addSecs(-1)
            self.time_label.setText(self.format_time(self.time))
        else:
            self.timer.stop()
    def open_tumbler(self):
        popup = Wheel()
        if popup.exec_():
            selected_time = popup.get_selected_time()
            self.time = self.format_time(selected_time)
            self.time_label.setText(selected_time)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    timer = Timer()
    timer.show()
    sys.exit(app.exec())
