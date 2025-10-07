import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from gui_qt.widgetBaseNote import WidgetBaseNote
from gui_qt.widgetKeyNote import WidgetKeyNote


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("8P4K PowerHouse")
        wdgt_base_note = WidgetBaseNote(self)
        wdgt_key_note = WidgetKeyNote(self)
        self.setCentralWidget(wdgt_key_note)
