import sys

from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QHBoxLayout,
    QVBoxLayout,
    QWidget,
)
from gui_qt.widgetBaseNote import WidgetBaseNote
from gui_qt.widgetKeyNote import WidgetKeyNote
from gui_qt.widgetPanelMode import WidgetPanelMode
from gui_qt.widgetPanelChord import WidgetPanelChord


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("8P4K PowerHouse")
        self.wdgt_base_note = WidgetBaseNote(self)
        self.wdgt_key_note = WidgetKeyNote(self)
        self.wdgt_panel_mode = WidgetPanelMode(self)
        self.wdgt_panel_chord = WidgetPanelChord(self)

        self.layout_col = QVBoxLayout(self)
        self.layout_row_up = QHBoxLayout(self)
        self.layout_row_down = QHBoxLayout(self)

        self.layout_row_up.addWidget(self.wdgt_panel_mode)
        self.layout_row_up.addWidget(self.wdgt_panel_chord)

        self.layout_row_down.addWidget(self.wdgt_base_note)
        self.layout_row_down.addWidget(self.wdgt_key_note)

        self.layout_col.addLayout(self.layout_row_up)
        self.layout_col.addLayout(self.layout_row_down)

        self.layout_container = QWidget()
        self.layout_container.setLayout(self.layout_col)
        self.setCentralWidget(self.layout_container)
