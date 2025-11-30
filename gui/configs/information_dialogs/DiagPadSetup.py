from PySide6.QtWidgets import QMessageBox
from PySide6.QtCore import Signal, QTimer


class DiagPadSetup(QMessageBox):

    sig_cancel = Signal()
    sig_ok = Signal()

    def __init__(
        self,
        parent=None,
        title="Instructions",
    ):
        super().__init__(parent)
        self.setIcon(QMessageBox.Information)
        self.setWindowTitle(title)
        self.setText('Press all your pad at least once and click "OK" once done.')
        self.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        self.accepted.connect(self.sig_ok)
        self.rejected.connect(self.sig_cancel)
