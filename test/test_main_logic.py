import pytest
from logic.gui.main_logic import MainLogic
from data.data_general import hc_pad_mode_note, hc_pad_mode_cc


def assert_midi_config_validity(midi_config_settings):
    result = True
    for key, value in midi_config_settings.items():
        if key.startswith("id_knob_"):
            if assert_if_int_or_null(value) is False:
                result = False
            elif is_int(value):
                if value < 0:
                    result = False
        elif key == "pad_mode":
            if value != hc_pad_mode_note and value != hc_pad_mode_cc:
                result = False
        elif key == "base_note_offset" or key == "pot_max_value":
            if is_int(value) is False:
                return False
            elif value < 0:
                return False

    return result


def assert_if_int_or_null(value):
    result = False
    if value:
        if is_int(value):
            result = True
        else:
            result = False
    else:
        result = True

    return result


def is_int(value):
    return isinstance(value, int) and not isinstance(value, bool)


@pytest.mark.parametrize(
    "midi_config_settings, expected",
    [
        pytest.param(
            {  # Default config
                "pad_mode": "note",
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": None,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            True,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": hc_pad_mode_note,
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": None,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            True,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": hc_pad_mode_cc,
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": None,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            True,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": hc_pad_mode_cc,
                "base_note_offset": -1,
                "pot_max_value": 127,
                "id_knob_mode": None,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            False,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": "note",
                "base_note_offset": -36,
                "pot_max_value": 127,
                "id_knob_mode": None,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            False,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": "note",
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": 10,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            True,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": "note",
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": 25,
                "id_knob_chord_comp": 15,
                "id_knob_chord_size": 16,
                "id_knob_base_note": 17,
                "id_knob_key_note": 18,
            },
            True,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": "note",
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": -1,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            False,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": "note",
                "base_note_offset": -36,
                "pot_max_value": 127,
                "id_knob_mode": None,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            False,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": "note",
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": None,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": 2.8,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            False,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": "mistral is a buffon",
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": 10,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            False,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": "note",
                "base_note_offset": "mistral suck",
                "pot_max_value": 127,
                "id_knob_mode": 10,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            False,
        ),
        pytest.param(
            {  # Default config
                "pad_mode": 2.8,
                "base_note_offset": 0,
                "pot_max_value": 127,
                "id_knob_mode": 10,
                "id_knob_chord_comp": None,
                "id_knob_chord_size": None,
                "id_knob_base_note": None,
                "id_knob_key_note": None,
            },
            False,
        ),
    ],
)
def test_assert_midi_config_validity(midi_config_settings, expected):
    assert (
        assert_midi_config_validity(midi_config_settings=midi_config_settings)
        == expected
    )
