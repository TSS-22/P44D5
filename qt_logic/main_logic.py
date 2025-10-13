from PySide6.QtCore import QObject, Signal


class MainLogic(QObject):
    # Define a signal to notify the UI
    state_changed = Signal(str)  # Emits a string

    def handle_midi(self):
        pass

    def do_work(self):
        # Simulate logic
        new_state = "Logic updated!"
        self.state_changed.emit(new_state)  # Notify UI
