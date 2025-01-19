import sys
import pytz
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout,QStackedWidget,QDialog
from PyQt5.QtCore import QTimer, QTime, Qt, QDateTime
from PyQt5.QtGui import QFontDatabase
from analog_clock import AnalogClock
from timezones import Timezones

#TODO : Changable colors?


class Clock(QWidget):
    def __init__(self):
        super().__init__()
        self.mode_label = QLabel("Select mode: ")
        self.analog_button = QPushButton("Analog")
        self.digital_button = QPushButton("Digital")
        self.timezones_button = QPushButton("Timezones")
        self.timezones_label = QLabel("Current timezone: Not selected")
        self.timezones_widget = Timezones()
        self.stack = QStackedWidget(self)
        self.stack.setGeometry(0, 50, 800, 750)
        self.analog_widget = AnalogClock()
        self.TimeLabel = QLabel(self)
        self.Timer = QTimer(self)
        self.selected_timezone = None

        self.initUI()
    def initUI(self):
        self.setWindowTitle("Clock")
        self.setGeometry(800, 300, 800, 500)

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.mode_label)

        hbox.addWidget(self.analog_button)
        self.analog_button.setStyleSheet("""QPushButton {
            border: 2px solid white;
            min_width: 100px;
            min_height: 20px;
            padding: 10px;
            font-size: 20px;
            border-radius: 10px}
            QPushButton:hover {
                background-color: darkgray;
            }
        
        """

        )
        hbox.addWidget(self.digital_button)
        self.digital_button.setStyleSheet(self.analog_button.styleSheet())
        hbox.addWidget(self.timezones_button)
        self.timezones_button.setStyleSheet(self.analog_button.styleSheet())
        self.analog_button.clicked.connect(self.show_page_analog)
        self.digital_button.clicked.connect(self.show_digital_time)
        self.timezones_button.clicked.connect(self.show_page_timezones)
        vbox.addLayout(hbox)
        vbox.addWidget(self.timezones_label)
        vbox.addWidget(self.TimeLabel)
        vbox.addWidget(self.stack)

        self.setLayout(vbox)

        self.show_digital_time()

        self.TimeLabel.setAlignment(Qt.AlignCenter)
        self.mode_label.setAlignment(Qt.AlignLeft)
        self.mode_label.setStyleSheet("""
            QLabel{
            font-size: 20px;
            font-weight: bold;
            }
        """)
        self.setStyleSheet("""
        QWidget{
        background-color: black;
        color: white;
        font-size: 120px;
        font-weight: bold;
        }
        """)
        QFontDatabase.addApplicationFont("digital-7 (italic).ttf")
        self.TimeLabel.setStyleSheet("""
        QLabel{
            border: 5px solid white;
            font-family: 'Digital-7 Italic';
            font-size: 120px;
            font-weight: bold
        }""")
        self.timezones_widget.setStyleSheet("font-size: 20px")
        self.Timer.timeout.connect(self.update_time)
        self.timezones_label.setStyleSheet("font-size:20px")
        self.timezones_label.setText(f"Current timezone: {self.selected_timezone}")
        self.Timer.start(1000)
        self.update_time()

    def update_time(self):
        if self.selected_timezone:
            utc_now = QDateTime.currentDateTime().toUTC().toPyDateTime()
            timezone = pytz.timezone(self.selected_timezone)
            time_in_timezone = pytz.utc.localize(utc_now).astimezone(timezone)
            self.TimeLabel.setText(time_in_timezone.strftime("%H:%M:%S"))
            self.timezones_label.setText(f"Current timezone: {self.selected_timezone}")
        else:
            current_time = QTime.currentTime().toString("hh:mm:ss")
            self.TimeLabel.setText(current_time)

    def show_digital_time(self):
        if self.stack.indexOf(self.TimeLabel) == -1:
            self.stack.addWidget(self.TimeLabel)
        self.stack.setCurrentWidget(self.TimeLabel)
        self.timezones_button.setVisible(True)

    def show_page_analog(self):
        if self.stack.indexOf(self.analog_widget) == -1:
            self.stack.addWidget(self.analog_widget)
        self.stack.setCurrentWidget(self.analog_widget)
        self.timezones_button.setVisible(False)

    def show_page_timezones(self):
        dialog = Timezones()
        if dialog.exec_() == QDialog.Accepted:  # Wait for user to select and press "OK"
            selected_timezone = dialog.get_timezone()
            if selected_timezone:
                self.selected_timezone = selected_timezone
                self.update_time()  # Immediately update time

                self.Timer.timeout.disconnect()
                self.Timer.timeout.connect(self.update_time)
                self.Timer.start(1000)
                self.timezones_label.setText(f"Current timezone: {self.selected_timezone}")
                self.show_digital_time()









if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = Clock()
    clock.show()
    sys.exit(app.exec_())