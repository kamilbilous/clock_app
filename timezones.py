import sys
import pytz
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QPushButton, QDialog
import tkinter as tk

class Timezones(QDialog):
    def __init__(self):
        super().__init__()
        self.ok_button = QPushButton('Ok', self)
        self.cancel_button = QPushButton('Cancel', self)
        