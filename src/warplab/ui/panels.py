from PySide6.QtWidgets import (
    QDockWidget,
    QLabel
)


def create_scene_panel(parent):

    dock = QDockWidget(
        "Scene Explorer",
        parent
    )

    dock.setWidget(
        QLabel(
            "Universe\n"
            "Camera\n"
            "Objects"
        )
    )

    return dock



def create_properties_panel(parent):

    dock = QDockWidget(
        "Properties",
        parent
    )

    dock.setWidget(
        QLabel(
            "Object Properties"
        )
    )

    return dock



def create_console_panel(parent):

    dock = QDockWidget(
        "Console",
        parent
    )

    dock.setWidget(
        QLabel(
            "WarpLab Console"
        )
    )

    return dock