from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt


class Viewport(QWidget):
    """
    Main simulation visualization area.
    """

    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)

        self.setFocusPolicy(
            Qt.StrongFocus
        )


    def paintEvent(self, event):

        painter = QPainter(self)

        painter.drawText(
            350,
            300,
            "WarpLab Space-Time Viewport"
        )

        painter.end()