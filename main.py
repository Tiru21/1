import sys

from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor, QPolygon, QPen, QBrush
from random import randint
from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QRadioButton


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi(r'UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.clickk)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        w = randint(10, 75)
        qp.setBrush(QColor(255, 255, 0))
        qp.drawEllipse(50, 50, w, w)

    def clickk(self):
        self.repaint()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
