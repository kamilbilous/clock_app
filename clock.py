import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt



class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.TimeLabel = QLabel(self)
        self.Timer = QTimer(self)

        self.initUI()
    def initUI(self):
        self.setWindowTitle("Clock")
        self.setGeometry(800, 300, 500, 300)

        vbox = QVBoxLayout()
        vbox.addWidget(self.TimeLabel)
        self.setLayout(vbox)

        self.TimeLabel.setAlignment(Qt.AlignCenter)
        self.TimeLabel.setStyleSheet("background-color:black;"
                                     "font-size: 120px;"
                                     "font-weight: bold;"
                                     "color: white;")
        self.Timer.timeout.connect(self.update_time)
        self.Timer.start(1000)
        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss")
        self.TimeLabel.setText(current_time)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())