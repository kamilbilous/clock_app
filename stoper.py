import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt

class Stoper(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.time_button = QPushButton("Time", self)
        self.times_label = QLabel("", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer()
        self.times = []
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Stoper")
        self.setGeometry(800, 300, 500, 600)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.times_label)


        self.setLayout(vbox)

        self.time_label.setAlignment(Qt.AlignTop)
        self.times_label.setAlignment(Qt.AlignTop)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        hbox.addWidget(self.time_button)

        vbox.addLayout(hbox)

        self.setStyleSheet("""
        QWidget {
        background-color:black;
        color: white;
        }
        
        QPushButton, QLabel{
            padding : 20px;
        }
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
        }
        QPushButton:hover {
            background-color: darkgray;
        }
        QLabel {
            font-size: 60px;
            color : white;
            background-color: black;
            border-radius : 20px
        }
        
        
        """)
        self.times_label.setStyleSheet("""
        QLabel {
            font-size: 20px
        }
        """)

        self.start_button.clicked.connect(self.start) #type: ignore
        self.stop_button.clicked.connect(self.stop) #type: ignore
        self.reset_button.clicked.connect(self.reset) #type: ignore
        self.time_button.clicked.connect(self.add_times) #type:ignore
        self.timer.timeout.connect(self.update_display) #type: ignore
    def start(self):
        self.timer.start(10)
    def stop(self):
        self.timer.stop()
    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))
        self.times.clear()
        self.times_label.setText("")
    def format_time(self,time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        miliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{miliseconds:02}"
    def update_display(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
    def add_times(self):
        if len(self.times) >= 10:
            self.times.clear()
        timestamp = self.format_time(self.time)
        self.times.append(timestamp)
        self.times_label.setText("\n".join([f"{i + 1}. {t}" for i, t in enumerate(self.times)]))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stoper = Stoper()
    stoper.show()
    sys.exit(app.exec())

