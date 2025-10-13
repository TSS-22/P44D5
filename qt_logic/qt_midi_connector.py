from PySide6.QtCore import QRunnable, Signal, Slot

from source.midi_controller import MidiController
from source.midi_bridge import MidiBridge


class QtMidiConnector(QRunnable):
    midi_message = Signal(dict)

    def __init__(self):
        super().__init__()

        self.midi_controller = MidiController()
        self.midi_bridge = MidiBridge()

    @Slot()
    def run(self):
        print("starting thread")
        while True:
            try:
                print("polling message")
                for midi_msg in self.midi_bridge.input.iter_pending():
                    messages = self.midi_bridge.bridge_out(
                        self.midi_controller.receive_message(midi_msg)
                    )
            except KeyboardInterrupt:
                print("Stopped.")

        self.midi_bridge.stop()
        #     # self.midi_message.emit(message)
