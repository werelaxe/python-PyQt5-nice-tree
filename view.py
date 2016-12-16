import sys, random
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtCore import QTimerEvent
from PyQt5.QtGui import QKeyEvent
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt

import graphics
import model


class NiceModelTree(QWidget):
    def __init__(self):
        super().__init__()
        self.width = 1400
        self.height = 800
        self.initUI()
        self.tree = model.Tree()
        self.timer = QBasicTimer()
        self.timer.start(0, self)
        self.growing = False

    def initUI(self):
        self.setGeometry(800 - self.width // 2, 450 - self.height // 2,
                         self.width, self.height)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_model(qp)
        qp.end()

    def draw_model(self, qp: QPainter):
        qp.setBrush(Qt.black)
        qp.drawRect(0, 0, self.width, self.height)
        qp.setPen(Qt.red)
        graphics.draw_tree(self.tree, qp)

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Control:
            self.growing = True

    def keyReleaseEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Control:
            self.growing = False

    def timerEvent(self, event: QTimerEvent):
        if self.growing:
            self.tree.grow()
        self.update()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NiceModelTree()
    sys.exit(app.exec_())