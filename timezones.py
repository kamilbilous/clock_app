import sys
import pytz
from PyQt5.QtWidgets import QApplication, QVBoxLayout,QPushButton, QDialog, QListWidget,QLineEdit


class Timezones(QDialog):
    def __init__(self):
        super().__init__()
        self.ok_button = QPushButton('Ok', self)
        self.cancel_button = QPushButton('Cancel', self)
        self.my_set = set(pytz.all_timezones)
        self.search_bar = QLineEdit(self)
        self.selected_timezone = None
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Timezones')
        self.setGeometry(300, 300, 500, 500)

        vbox = QVBoxLayout(self)
        self.search_bar.setPlaceholderText("Search timezones...")
        self.search_bar.setStyleSheet("font-size: 20px")
        self.search_bar.textChanged.connect(self.filter_timezones)
        self.list_widget = QListWidget(self)
        for item in sorted(self.my_set):
            self.list_widget.addItem(item)
        self.list_widget.setMinimumHeight(300)
        self.list_widget.itemClicked.connect(self.select_timezone)
        vbox.addWidget(self.search_bar)
        vbox.addWidget(self.list_widget)
        vbox.addWidget(self.ok_button)
        self.ok_button.setStyleSheet("""QPushButton {
            border: 2px solid white;
            min_width: 100px;
            min_height: 20px;
            padding: 10px;
            font-size: 20px;
            border-radius: 10px}
            QPushButton:hover {
                background-color: darkgray;
            }""")
        vbox.addWidget(self.cancel_button)
        self.cancel_button.setStyleSheet(self.ok_button.styleSheet())
        self.ok_button.clicked.connect(self.accept) # type: ignore
        self.cancel_button.clicked.connect(self.reject)
        self.setStyleSheet("background-color: black; color: white")
        self.setLayout(vbox)

    def accept(self):
        if self.selected_timezone:
            super().accept()
    def filter_timezones(self):
        search_text = self.search_bar.text().lower()
        self.list_widget.clear()

        for item in sorted(self.my_set):
            if search_text in item.lower():
                self.list_widget.addItem(item)

    def select_timezone(self, item):
        self.selected_timezone = item.text()
    def get_timezone(self):
        if self.selected_timezone:
            return self.selected_timezone
        return None

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Timezones()
    window.show()
    sys.exit(app.exec_())
