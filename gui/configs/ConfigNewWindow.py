from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QComboBox, QVBoxLayout
from PySide6.QtGui import QIcon


class ConfigNewWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Create MIDI controller configuration")

        self.lbl_list_midi_controller = QLabel("MIDI controller available")

        self.button_list_midi_controller_refresh = QPushButton()
        self.button_list_midi_controller_refresh.setIcon(
            QIcon.fromTheme("view-refresh")
        )  # System theme icon
        self.button_list_midi_controller_refresh.setText("Refresh")
        self.button_list_midi_controller_refresh.clicked.connect(
            self.refresh_list_midi_controller
        )

        self.cmb_list_midi_controller = QComboBox()
        self.cmb_list_midi_controller.addItem("Option 1")
        self.cmb_list_midi_controller.addItem("Option 2")
        self.cmb_list_midi_controller.addItem("Option 3")
        self.cmb_list_midi_controller.addItem("Option 4")

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_list_midi_controller)
        self.layout.addWidget(self.button_list_midi_controller_refresh)
        self.layout.addWidget(self.cmb_list_midi_controller)

        self.setLayout(self.layout)

    def refresh_list_midi_controller(self):
        print("refresh midi controller list")
