from PySide6.QtWidgets import QMainWindow, QPushButton

import sys


class App8p4k(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("8P4K Power House")

        button = QPushButton("My simple app.")
        button.pressed.connect(self.close)

        self.setCentralWidget(button)
        self.show()
