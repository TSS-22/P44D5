from PySide6.QtCore import QObject, Signal


class MainLogicSignal(QObject):
    base_note_changed = Signal(int)
    key_note_changed = Signal(dict)
    panel_mode_changed = Signal(dict)
    panel_chord_changed = Signal(dict)
    panel_play_changed = Signal(dict)
    pad_grid_changed = Signal(dict)
