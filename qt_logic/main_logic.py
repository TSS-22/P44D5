from PySide6.QtCore import QObject, Signal, Slot
from source.midi_bridge_message_out import MidiBridgeMessageOut
from qt_logic.main_logic_signal import MainLogicSignal
from qt_logic.StateTupleMap import StateTupleMap


class MainLogic(QObject):
    id_knob_base_note = 70  # HARDCODED
    signal = MainLogicSignal()

    @Slot()
    def handle_midi(self, midi_controller_state):
        self.signal.base_note_changed.emit(midi_controller_state["base_note"])
        self.signal.key_note_changed.emit(
            {
                "key_degree": midi_controller_state["key_degree"],
                "key_degree_octave": midi_controller_state["key_degree_octave"],
                "key_note": midi_controller_state["key_note"],
                "raw_key_knob": midi_controller_state["raw_key_knob"],
            }
        )

    def do_work(self):
        # Simulate logic
        new_state = "Logic updated!"
        self.state_changed.emit(new_state)  # Notify UI
