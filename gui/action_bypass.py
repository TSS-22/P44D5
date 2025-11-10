from PySide6.QtGui import QAction, QIcon
from PySide6.QtWidgets import QStyle
from PySide6.QtCore import Signal


class QActionBypass(QAction):
    signal_toggled = Signal(bool)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setText("Midi bypass")
        self.setStatusTip("Midi bypass turned off")
        self.setCheckable(True)
        self.icon_stop = QIcon("../ressources/gui/icons/prohibition.png")
        self.icon_go = QIcon("../ressources/gui/icons/play_solid.png")
        self.toggled.connect(self.on_toggled)  # Connect the signal
        self.setIcon(self.icon_go)

    def on_toggled(self, checked):
        self.signal_toggled.emit(checked)
        if checked:
            self.setStatusTip("Midi bypass turned on")
            self.setIcon(self.icon_stop)
        else:
            self.setStatusTip("Midi bypass turned off")
            self.setIcon(self.icon_go)
