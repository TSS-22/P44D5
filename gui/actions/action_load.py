from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QStyle, QFileDialog
from PySide6.QtCore import Signal


class QActionConfigLoad(QAction):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setText("Open MIDI controller config")
        self.setStatusTip("Open MIDI controller config (Ctrl + O)")
        self.icon = QIcon.fromTheme("document-open")
        self.setIcon(self.icon)
        self.triggered.connect(self.open_file_dialog)
        self.setShortcut(QKeySequence.Open)

    def open_file_dialog(self):
        file_path, _ = QFileDialog.getOpenFileName(
            None,
            "Open File",
            "",
            "Midi controller config files (*.cnfmidi);;All Files (*);;",
        )
        if file_path:
            print(f"Selected file: {file_path}")
            # Do something with the file path
