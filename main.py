from source.midi_controller import MidiController
from source.midi_bridge import MidiBridge

midi_controller = MidiController()

midi_bridge = MidiBridge()

midi_bridge.start(midi_controller)
