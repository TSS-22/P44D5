from PySide6.QtWidgets import QStatusBar, QLabel
from PySide6.QtCore import QTimer


class MainStatusBar(QStatusBar):
    def __init__(self):
        super().__init__()
        self.setStyleSheet(
            """
            border: none;
            background: #eeeeee;
            spacing: 2px;
            """
        )
        self.lbl_config_loaded = QLabel("Loaded config: test")
        self.lbl_status_error_sucess = QLabel("")
        self.addPermanentWidget(self.lbl_status_error_sucess)
        self.addPermanentWidget(self.lbl_config_loaded)

    def new_config_loaded(self, name):
        self.lbl_config_loaded.setText(f"Loaded config: {name}")

    def print_error_success(self, error_text):
        self.lbl_status_error_sucess.setText(error_text)
        QTimer.singleShot(2000, lambda: self.lbl_status_error_sucess.setText(""))
