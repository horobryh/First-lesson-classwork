import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QBrush, QColor
from PyQt5.QtWidgets import QWidget, QApplication


class Form(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.pb.clicked.connect(self.redraw)
        self.need_to_draw = False

    def redraw(self):
        self.need_to_draw = True
        self.update()

    def paintEvent(self, event) -> None:
        if self.need_to_draw:
            self.need_to_draw = False
            self.draw_ellipse()

    def draw_ellipse(self):
        qp = QPainter()
        qp.begin(self)
        r = randint(10, 100)
        x, y = (randint(0, self.width() - r * 2),
                randint(0, self.height() - r * 2))
        brush = QBrush(QColor('yellow'))
        qp.setBrush(brush)
        qp.drawEllipse(x, y, r * 2, r * 2)
        qp.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    wnd = Form()
    wnd.show()
    sys.exit(app.exec())
