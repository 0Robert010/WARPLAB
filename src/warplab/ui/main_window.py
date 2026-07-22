from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt

from warplab.ui.viewport import Viewport
from warplab.ui.panels import (
    create_scene_panel,
    create_properties_panel,
    create_console_panel,
)

from warplab.ui.menus import create_menu_bar


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setup()

    def setup(self):

        self.setWindowTitle(
            "WarpLab"
        )

        self.resize(
            1600,
            900
        )

        # Central viewport
        self.setCentralWidget(
            Viewport()
        )

        # Dock panels

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            create_scene_panel(self)
        )

        self.addDockWidget(
            Qt.RightDockWidgetArea,
            create_properties_panel(self)
        )

        self.addDockWidget(
            Qt.BottomDockWidgetArea,
            create_console_panel(self)
        )

        # Menu

        create_menu_bar(self)