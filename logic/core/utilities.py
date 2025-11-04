import json
import os

# TODO changer les noms dans les JSON et dans les variables pour que ca soit plus lisible et intuitif


def resolve_references(data):
    for value in data:
        if isinstance(value, list):
            data[value] = [
                data[ref.replace("$ref:", "")]
                for ref in value
                if isinstance(ref, str) and ref.startswith("$ref:")
            ]
    return data


def correct_file_path(file_path):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(script_dir, file_path)


def init_state_app():

    with open(correct_file_path("data_settings.json"), "r") as file_settings:
        data_settings = json.load(file_settings)

    with open(correct_file_path("data_options_play.json"), "r") as file_options_play:
        data_options_play = json.load(file_options_play)

    return {
        "name_midi_in": data_settings["name_midi_in"],
        "name_midi_out": data_settings["name_midi_out"],
        "base_note_offset": data_settings["base_note_offset"],
        "pot_max_value": data_settings["pot_max_value"] + 1,
        "knob_quadrant_playModes": (
            data_settings["pot_max_value"]
            / len(data_options_play["knob_values_playModes"])
        ),
        "knob_quadrant_PlayType": (
            data_settings["pot_max_value"]
            / len(data_options_play["knob_values_playTypes"])
        ),
    }


def init_state_controller():
    with open(correct_file_path("data_options_play.json"), "r") as file_options_play:
        data_options_play = json.load(file_options_play)

    return {
        "mode": data_options_play["knob_values_playModes"][0],
        "base_note": 0,
        "key_note": 0,
        "key_degree": 0,
        "play_type": data_options_play["knob_values_playTypes"][0],
        "state_pad": [0, 0, 0, 0, 0, 0, 0, 0],
        "buffer_velocity": [0, 0, 0, 0, 0, 0, 0, 0],
        "buffer_note": [[], [], [], [], [], [], [], []],
        "midi_in": None,
        "midi_out": None,
    }


def init_options_play():
    with open(correct_file_path("data_options_play.json"), "r") as file_options_play:
        data_options_play = json.load(file_options_play)

    playModes_chordProg = {
        "Ionian": [0, 1, 2, 3, 4, 5, 6, 7],
        "Dorian": [1, 2, 3, 4, 5, 6, 7, 0],
        "Phrygian": [2, 3, 4, 5, 6, 7, 0, 1],
        "Lydian": [3, 4, 5, 6, 7, 0, 1, 2],
        "Myxolydian": [4, 5, 6, 7, 0, 1, 2, 3],
        "Aeolian": [5, 6, 7, 0, 1, 2, 3, 4],
        "Locrian": [6, 7, 0, 1, 2, 3, 4, 5],
    }

    mode_prog_chord = {}

    for key in data_options_play["playModes_chordProg"]:
        mode_prog_chord.update({key: []})
        for val in data_options_play["playModes_chordProg"][key]:
            mode_prog_chord[key].append(
                data_options_play[data_options_play["ionian_chord_prog"][val]]
            )

        print(mode_prog_chord[key])

    return {
        "knob_values_playModes": data_options_play["knob_values_playModes"],
        "knob_values_playTypes": data_options_play["knob_values_playTypes"],
        "playModes_toneProg": data_options_play["playModes_toneProg"],
        "playModes_chordProg": data_options_play["playModes_chordProg"],
        "chord_major": data_options_play["chord_major"],
        "chord_minor": data_options_play["chord_minor"],
        "chord_dom7": data_options_play["chord_dom7"],
        "chord_dim": data_options_play["chord_dim"],
        "tone_progression": data_options_play["tone_progression"],
        "mode_prog_chord": mode_prog_chord,
    }
