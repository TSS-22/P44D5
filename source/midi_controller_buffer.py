class MidiControllerBuffer:
    def __init__(self):
        self.velocity = [0, 0, 0, 0, 0, 0, 0, 0]
        self.notes = [[], [], [], [], [], [], [], []]
