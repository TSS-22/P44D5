from PySide6.QtCore import QObject, Signal


class MainLogicSignal(QObject):
    base_note_changed = Signal(int)
    key_note_changed = Signal(dict)
