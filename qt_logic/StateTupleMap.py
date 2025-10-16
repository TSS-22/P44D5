from enum import Enum


class StateTupleMap(Enum):
    BUFFER = 0
    BASE_NOTE = 1
    KEY_NOTE = 2
    KEY_DEGREE = 3
    SELECTED_MODE = 4
    SELECTED_PLAY_TYPE = 5
    CHORD_TYPE = 6
    RAW_KNOB_KEY = 7
    RAW_KNOB_MODE = 8
    RAW_KNOB_PLAY_TYPE = 9
    RAW_KNOB_CHORD_TYPE = 10
    VELOCITY = 0
    NOTES = 1
