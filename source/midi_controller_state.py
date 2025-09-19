from source.midi_controller_buffer import MidiControllerBuffer


class MidiControllerState:
    def __init__(
        self, selected_mode=None, selected_play_type=None, selected_chord_type=None
    ):
        self.buffer = MidiControllerBuffer()
        self.base_note = 0
        self.key_note = 0
        self.key_degree = 0
        self.selected_mode = selected_mode
        self.selected_play_type = selected_play_type
        self.chord_type = selected_chord_type
        self.raw_key_knob = 0
        self.raw_knob_mode = 0
        self.raw_knob_play_type = 0
        self.raw_knob_chord_type = 0
