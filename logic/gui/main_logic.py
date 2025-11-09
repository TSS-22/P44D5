from PySide6.QtCore import QRunnable, Signal, Slot, QObject

from logic.core.controller.midi_controller import MidiController
from logic.core.bridge.midi_bridge import MidiBridge
from logic.gui.main_logic_signals import MainLogicSignals
from logic.core.controller.controller_message_flag import ControllerMessageFlag


class MainLogic(QRunnable):

    def __init__(self):
        super().__init__()
        self.signals = MainLogicSignals()
        self.midi_controller = MidiController()
        self.midi_bridge = MidiBridge()
        self._is_running = False

    def run(self):
        print("starting thread")
        self._is_running = True
        while self._is_running:
            try:
                for midi_msg in self.midi_bridge.input.iter_pending():
                    midi_controller_output = self.midi_bridge.bridge_out(
                        self.midi_controller.receive_message(midi_msg)
                    )
                    self.handle_midi(midi_controller_output.to_dict())

            except KeyboardInterrupt:
                print("Stopped.")

        self.midi_bridge.stop()
        self.signals.finished.emit()

    @Slot()
    def stop(self):
        self._is_running = False
        self.signals.stopped.emit()

    def handle_midi(self, midi_controller_output):
        if midi_controller_output["flag"] == ControllerMessageFlag.BASE_NOTE_CHANGED:
            self.signals.base_note_changed.emit(midi_controller_output["state"])
        elif midi_controller_output["flag"] == ControllerMessageFlag.KEY_NOTE_CHANGED:
            self.signals.key_note_changed.emit(
                # {
                #     "key_degree": midi_controller_output["state"]["key_degree"],
                #     "key_degree_octave": midi_controller_output["state"][
                #         "key_degree_octave"
                #     ],
                #     "key_note": midi_controller_output["state"]["key_note"],
                #     "raw_key_knob": midi_controller_output["state"]["raw_key_knob"],
                # }
                midi_controller_output["state"]
            )
        elif midi_controller_output["flag"] == ControllerMessageFlag.MODE_CHANGED:
            self.signals.panel_mode_changed.emit(
                # {
                #     "raw_knob_mode": midi_controller_output["state"]["raw_knob_mode"],
                #     "selected_mode": midi_controller_output["state"]["selected_mode"],
                # }
                midi_controller_output["state"]
            )
        elif midi_controller_output["flag"] == ControllerMessageFlag.CHORD_CHANGED:
            self.signals.panel_chord_changed.emit(
                # {
                #     "raw_knob_chord_type": midi_controller_output["state"][
                #         "raw_knob_chord_type"
                #     ],
                #     "chord_type": midi_controller_output["state"]["chord_type"],
                # }
                midi_controller_output["state"]
            )
        elif midi_controller_output["flag"] == ControllerMessageFlag.PLAY_CHANGED:
            self.signals.panel_play_changed.emit(
                # {
                #     "raw_knob_play_type": midi_controller_output["state"][
                #         "raw_knob_play_type"
                #     ],
                #     "selected_play_type": midi_controller_output["state"][
                #         "selected_play_type"
                #     ],
                # }
                midi_controller_output["state"]
            )
        elif (
            midi_controller_output["flag"] == ControllerMessageFlag.PAD_PRESSED
            or ControllerMessageFlag.PAD_RELEASED
        ):
            self.signals.pad_grid_changed.emit(
                # {
                #     "velocity": midi_controller_output["state"]["buffer"]["velocity"],
                #     "key_degree": midi_controller_output["state"]["key_degree"],
                #     "base_note": midi_controller_output["state"]["base_note"],
                #     "key_note": midi_controller_output["state"]["key_note"],
                #     "pad_intervals": midi_controller_output["state"]["pad_intervals"],
                #     "key_degree_octave": midi_controller_output["state"][
                #         "key_degree_octave"
                #     ],  # Probably key_note and key_degree_octave are redundant
                # }
                midi_controller_output["state"]
            )
