import sys
import pygame
import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QImage, QPixmap, QPainter
from PyQt5.QtCore import QTimer, Qt
from math import pi, cos, sin

WIDTH, HEIGHT = 400, 400
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

pygame.init()

class PygameClock:
    def __init__(self):
        self.screen = pygame.Surface((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

    def polar_to_cartesian(self, r, theta):
        x = r * sin(pi * theta / 180)
        y = r * cos(pi * theta / 180)
        return x + WIDTH / 2, -(y - HEIGHT / 2)

    def draw_clock(self):
        self.screen.fill(BLACK)
        center = (WIDTH / 2, HEIGHT / 2)
        clock_radius = HEIGHT * 0.375

        now = datetime.datetime.now()
        second, minute, hour = now.second, now.minute, now.hour

        pygame.draw.circle(self.screen, WHITE, center, clock_radius, 10)
        pygame.draw.circle(self.screen, WHITE, center, 8)


        for number in range(1, 13):
            pos = self.polar_to_cartesian(clock_radius - 40, number * 30)
            font = pygame.font.SysFont("Arial", 20, True)
            text = font.render(str(number), True, WHITE)
            text_rect = text.get_rect(center=pos)
            self.screen.blit(text, text_rect)

        for number in range(0, 360, 6):
            start = self.polar_to_cartesian(clock_radius - 10, number)
            end = self.polar_to_cartesian(clock_radius - (30 if number % 30 == 0 else 15), number)
            pygame.draw.line(self.screen, WHITE, start, end, 6 if number % 30 == 0 else 2)

        pygame.draw.line(self.screen, WHITE, center, self.polar_to_cartesian(clock_radius*0.5, (hour % 12 + minute / 60) * 30), 10)
        pygame.draw.line(self.screen, WHITE, center, self.polar_to_cartesian(clock_radius*0.65, minute * 6), 6)
        pygame.draw.line(self.screen, RED, center, self.polar_to_cartesian(clock_radius*0.75, second * 6), 3)

        self.clock.tick(FPS)

    def get_surface(self):
        self.draw_clock()
        buffer = pygame.image.tostring(self.screen, "RGB")
        return QImage(buffer, WIDTH, HEIGHT, QImage.Format_RGB888)


class PygameWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.pygame_clock = PygameClock()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(1000 // FPS)

    def paintEvent(self, event):
        painter = QPainter(self)
        img = self.pygame_clock.get_surface()
        pixmap = QPixmap.fromImage(img)
        painter.drawPixmap(0, 0, pixmap)


class AnalogClock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Clock")
        self.setGeometry(100, 100, WIDTH, HEIGHT)
        self.pygame_widget = PygameWidget(self)
        layout = QVBoxLayout()

        layout.addWidget(self.pygame_widget)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        self.setFixedSize(WIDTH, HEIGHT)
        self.setStyleSheet("background-color: black; color:white")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnalogClock()
    window.show()
    sys.exit(app.exec_())
