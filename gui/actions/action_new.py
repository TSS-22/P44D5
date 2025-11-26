from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QStyle, QFileDialog
from PySide6.QtCore import Signal

from gui.configs.ConfigNewWindow import ConfigNewWindow


class QActionConfigNew(QAction):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("New MIDI controller config")
        self.setStatusTip("New MIDI controller config (Ctrl + N)")
        self.icon = QIcon.fromTheme("document-new")
        self.setIcon(self.icon)
        self.triggered.connect(self.clicked)
        self.setShortcut(QKeySequence.New)

    def clicked(self):
        self.config_new_window = ConfigNewWindow()
        self.config_new_window.show()
