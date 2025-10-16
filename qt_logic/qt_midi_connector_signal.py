from PySide6.QtCore import QObject, Signal


class QtMidiConnectorSignal(QObject):

    midi_messages = Signal(dict)
    finished = Signal()
    stopped = Signal()
