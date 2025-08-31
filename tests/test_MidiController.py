import pytest
import sys
import os
import json

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from source.midi_controller import MidiController


with open("./data/data_options_play.json", "r") as file_options_play:
    data = json.load(file_options_play)


@pytest.mark.parametrize(
    "mode, expected_pad_interval",
    [
        ("None", [0, 1, 1, 1, 1, 1, 1, 1]),
        ("Ionian", [0, 2, 2, 1, 2, 2, 2, 1]),
        ("Dorian", [0, 2, 1, 2, 2, 2, 1, 2]),
        ("Phrygian", [0, 1, 2, 2, 2, 1, 2, 2]),
        ("Lydian", [0, 2, 2, 2, 1, 2, 2, 1]),
        ("Myxolydian", [0, 2, 2, 1, 2, 2, 1, 2]),
        ("Aeolian", [0, 2, 1, 2, 2, 1, 2, 2]),
        ("Locrian", [0, 1, 2, 2, 1, 2, 2, 2]),
    ],
)
def test_compute_pad_interval_no_degree(mode, expected_pad_interval):
    midi_controller = MidiController()
    midi_controller.selected_mode = mode
    midi_controller.compute_pad_intervals()
    assert midi_controller.selected_pad_interval == expected_pad_interval


@pytest.mark.parametrize(
    "degree, expected_pad_interval",
    [
        (0, [0, 1, 1, 1, 1, 1, 1, 1]),
        (1, [0, 1, 1, 1, 1, 1, 1, 1]),
        (2, [0, 1, 1, 1, 1, 1, 1, 1]),
        (3, [0, 1, 1, 1, 1, 1, 1, 1]),
        (4, [0, 1, 1, 1, 1, 1, 1, 1]),
        (5, [0, 1, 1, 1, 1, 1, 1, 1]),
        (6, [0, 1, 1, 1, 1, 1, 1, 1]),
    ],
)
def test_compute_pad_interval_None(degree, expected_pad_interval):
    midi_controller = MidiController()
    midi_controller.selected_mode = "None"
    midi_controller.key_degree = degree
    midi_controller.compute_pad_intervals()
    assert midi_controller.selected_pad_interval == expected_pad_interval


@pytest.mark.parametrize(
    "degree, expected_pad_interval",
    [
        (0, [0, 2, 2, 1, 2, 2, 2, 1]),
        (1, [-2, 0, 2, 1, 2, 2, 2, 1]),
        (2, [-2, -2, 0, 1, 2, 2, 2, 1]),
        (3, [-2, -2, -1, 0, 2, 2, 2, 1]),
        (4, [-2, -2, -1, -2, 0, 2, 2, 1]),
        (5, [-2, -2, -1, -2, -2, 0, 2, 1]),
        (6, [-2, -2, -1, -2, -2, -2, 0, 1]),
    ],
)
def test_compute_pad_interval_Ionian(degree, expected_pad_interval):
    midi_controller = MidiController()
    midi_controller.selected_mode = "Ionian"
    midi_controller.key_degree = degree
    midi_controller.compute_pad_intervals()
    assert midi_controller.selected_pad_interval == expected_pad_interval


@pytest.mark.skip
@pytest.mark.parametrize(
    "knob_value, expected_value",
    [
        (0, -36),
        (1, -36),
        (2, -30),
        (3, -30),
        (4, -30),
        (5, -29),
        (6, -29),
        (7, -29),
        (8, -28),
        (9, -28),
        (10, -28),
        (11, -27),
        (12, -27),
        (13, -27),
        (14, -26),
        (15, -26),
        (16, -26),
        (17, -25),
        (18, -25),
        (19, -25),
        (20, -24),
        (21, -24),
        (22, -24),
        (23, -18),
        (24, -18),
        (25, -18),
        (26, -17),
        (27, -17),
        (28, -17),
        (29, -16),
        (30, -16),
        (31, -16),
        (32, -15),
        (33, -15),
        (34, -15),
        (35, -14),
        (36, -14),
        (37, -14),
        (38, -13),
        (39, -13),
        (40, -13),
        (41, -12),
        (42, -12),
        (43, -12),
        (44, -6),
        (45, -6),
        (46, -6),
        (47, -5),
        (48, -5),
        (49, -5),
        (50, -4),
        (51, -4),
        (52, -4),
        (53, -3),
        (54, -3),
        (55, -3),
        (56, -2),
        (57, -2),
        (58, -2),
        (59, -1),
        (60, -1),
        (61, -1),
        (62, 0),
        (63, 0),
        (64, 0),
        (65, 0),
        (66, 0),
        (67, 1),
        (68, 1),
        (69, 1),
        (70, 2),
        (71, 2),
        (72, 2),
        (73, 3),
        (74, 3),
        (75, 3),
        (76, 4),
        (77, 4),
        (78, 4),
        (79, 5),
        (80, 5),
        (81, 5),
        (82, 6),
        (83, 6),
        (84, 6),
        (85, 12),
        (86, 12),
        (87, 12),
        (88, 13),
        (89, 13),
        (90, 13),
        (91, 14),
        (92, 14),
        (93, 14),
        (94, 15),
        (95, 15),
        (96, 15),
        (97, 16),
        (98, 16),
        (99, 16),
        (100, 17),
        (101, 17),
        (102, 17),
        (103, 18),
        (104, 18),
        (105, 18),
        (106, 24),
        (107, 24),
        (108, 24),
        (109, 25),
        (110, 25),
        (111, 25),
        (112, 26),
        (113, 26),
        (114, 26),
        (115, 27),
        (116, 27),
        (117, 27),
        (118, 28),
        (119, 28),
        (120, 28),
        (121, 29),
        (122, 29),
        (123, 29),
        (124, 30),
        (125, 30),
        (126, 30),
        (127, 36),
    ],
)
def test_select_key_note_return_value(knob_value, expected_value):
    midi_controller = MidiController()
    midi_controller.selected_mode = "Ionian"
    assert midi_controller.select_key_note(knob_value) == expected_value


@pytest.mark.parametrize(
    "knob_value, expected_value",
    [
        (0, 0),
        (1, 0),
        (2, -6),
        (3, -6),
        (4, -6),
        (5, -5),
        (6, -5),
        (7, -5),
        (8, -4),
        (9, -4),
        (10, -4),
        (11, -3),
        (12, -3),
        (13, -3),
        (14, -2),
        (15, -2),
        (16, -2),
        (17, -1),
        (18, -1),
        (19, -1),
        (20, 0),
        (21, 0),
        (22, 0),
        (23, -6),
        (24, -6),
        (25, -6),
        (26, -5),
        (27, -5),
        (28, -5),
        (29, -4),
        (30, -4),
        (31, -4),
        (32, -3),
        (33, -3),
        (34, -3),
        (35, -2),
        (36, -2),
        (37, -2),
        (38, -1),
        (39, -1),
        (40, -1),
        (41, 0),
        (42, 0),
        (43, 0),
        (44, -6),
        (45, -6),
        (46, -6),
        (47, -5),
        (48, -5),
        (49, -5),
        (50, -4),
        (51, -4),
        (52, -4),
        (53, -3),
        (54, -3),
        (55, -3),
        (56, -2),
        (57, -2),
        (58, -2),
        (59, -1),
        (60, -1),
        (61, -1),
        (62, 0),
        (63, 0),
        (64, 0),
        (65, 0),
        (66, 0),
        (67, 1),
        (68, 1),
        (69, 1),
        (70, 2),
        (71, 2),
        (72, 2),
        (73, 3),
        (74, 3),
        (75, 3),
        (76, 4),
        (77, 4),
        (78, 4),
        (79, 5),
        (80, 5),
        (81, 5),
        (82, 6),
        (83, 6),
        (84, 6),
        (85, 0),
        (86, 0),
        (87, 0),
        (88, 1),
        (89, 1),
        (90, 1),
        (91, 2),
        (92, 2),
        (93, 2),
        (94, 3),
        (95, 3),
        (96, 3),
        (97, 4),
        (98, 4),
        (99, 4),
        (100, 5),
        (101, 5),
        (102, 5),
        (103, 6),
        (104, 6),
        (105, 6),
        (106, 0),
        (107, 0),
        (108, 0),
        (109, 1),
        (110, 1),
        (111, 1),
        (112, 2),
        (113, 2),
        (114, 2),
        (115, 3),
        (116, 3),
        (117, 3),
        (118, 4),
        (119, 4),
        (120, 4),
        (121, 5),
        (122, 5),
        (123, 5),
        (124, 6),
        (125, 6),
        (126, 6),
        (127, 0),
    ],
)
def test_select_key_note_temp_note(knob_value, expected_value):
    midi_controller = MidiController()
    midi_controller.selected_mode = "Ionian"

    degree = 0

    temp_note = int((knob_value - 64) / 3)
    octave = int(temp_note / 7) * 12
    inter_octave = 0

    if temp_note > 64:
        temp = temp_note % 7
        for val in midi_controller.selected_pad_interval[1:temp]:
            inter_octave = inter_octave + val
            degree = degree + 1

    else:
        temp = temp_note % -7  # To test
        for val in midi_controller.selected_pad_interval[1:temp:-1]:
            inter_octave = inter_octave - val
            degree = degree + 1

    assert inter_octave == expected_value
