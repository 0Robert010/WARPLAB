import sys

from PySide6.QtWidgets import QApplication

from warplab.ui.main_window import MainWindow


class Application:
    """
    Main application controller.

    Responsible for:
    - initializing Qt
    - creating main window
    - running application loop
    """

    def __init__(self):
        self.qt_application = QApplication(sys.argv)
        self.main_window = MainWindow()

    def run(self) -> int:
        """
        Starts application event loop.
        """

        self.main_window.show()

        return self.qt_application.exec()