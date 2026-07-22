from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QLabel,
    QDockWidget,
)
from PySide6.QtCore import Qt


class MainWindow(QMainWindow):
    """
    Main WarpLab application window.
    """

    def __init__(self):
        super().__init__()

        self._setup_window()
        self._create_viewport()
        self._create_docks()
        self._create_menu()

    def _setup_window(self):
        self.setWindowTitle("WarpLab")
        self.resize(1400, 900)

    def _create_viewport(self):
        viewport = QLabel(
            "WarpLab Viewport\n\nSimulation Area"
        )

        viewport.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(viewport)

    def _create_docks(self):

        # Scene Explorer

        scene = QDockWidget(
            "Scene Explorer",
            self
        )

        scene.setWidget(
            QLabel("Objects\nUniverse\nCamera")
        )

        self.addDockWidget(
            Qt.LeftDockWidgetArea,
            scene
        )


        # Properties

        properties = QDockWidget(
            "Properties",
            self
        )

        properties.setWidget(
            QLabel("No object selected")
        )

        self.addDockWidget(
            Qt.RightDockWidgetArea,
            properties
        )


        # Console

        console = QDockWidget(
            "Console",
            self
        )

        console.setWidget(
            QLabel("WarpLab Console")
        )

        self.addDockWidget(
            Qt.BottomDockWidgetArea,
            console
        )


    def _create_menu(self):

        menu = self.menuBar()

        file_menu = menu.addMenu("File")
        view_menu = menu.addMenu("View")
        tools_menu = menu.addMenu("Tools")
        help_menu = menu.addMenu("Help")