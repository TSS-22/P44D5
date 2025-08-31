

# Check if the note doesn't go below or above the maximum MIDI protocol values
# Used to prevent error when computing notes as they can go below and above
# those values
# min: 0
# max: 127
def check_note(note):
    if note > 127:
        return 127
    elif note < 0:
        return 0
    else:
        return note

# Reset the key_degree value from controller settings.
# Used when changing the mode
def reset_key_degree():
    print("Key degree: 0")
    return 0

# Select the note that serve as base for the rest.
def select_base_note(note_value):
    print(f"Base note: {note_value}")
    return note_value

def compute_pad_intervals(key_degree, tone_progression):
    tone_intervals = [-x for x in tone_progression[:key_degree]] + [0] + tone_progression[key_degree:]
    return tone_intervals

def note_off(note, velocity, id_pad):
    outport.send(mido.Message("note_off", note=note, velocity=velocity))
    print(f"Note off: {note} | Pad: {id_pad + 1}")

# Used to select the modes.
# Refer to "./data.py/knob_values_playModes" for more details about the possible values
def select_playMode(knob_values_playModes, knob_quadrant_playModes, message):
    print(f"Mode: {knob_values_playModes[int(message.value/knob_quadrant_playModes)]}\n")
    return knob_values_playModes[int(message.value/knob_quadrant_playModes)]

# Used to select the type of play, either chord like or single note.
# Refer to "./data.py/knob_values_playTypes" for more details about the possible values
def select_playTypes(knob_values_playTypes, knob_quadrant_PlayType, message):
    print(f"Play type: {knob_values_playTypes[int(message.value/knob_quadrant_PlayType)]}\n")
    return knob_values_playTypes[int(message.value/knob_quadrant_PlayType)]

#########################

def note_on(state_controller, note, velocity, id_pad):
    
    if state_controller["play_type"] == "Single":
        state_controller["buffer_note"][id_pad].append(note)
        outport.send(mido.Message("note_on", note=note, velocity=velocity))
        print(f"Note on: {note} | Pad: {id_pad + 1}")

    elif state_controller["play_type"] == "Normal":
        for chord_interval in play_type_chord_prog[state_controller["play_type"]][id_pad]:
            buffer_note[id_pad].append(note + chord_interval)
            outport.send(mido.Message("note_on", note=note + chord_interval, velocity=velocity))

    else:
        for chord_interval in play_type_chord_prog[state_controller["play_type"]]:
            buffer_note[id_pad].append(note + chord_interval)
            outport.send(mido.Message("note_on", note=note + chord_interval, velocity=velocity))
    
# When using no mode, it is equivalent to select_base_node
# When using modes play, the mode stick to the base note to 
# determine the key we are in, but you can use the select_key_note
# to chose the note the pad will play from within the key.
# This allow for play within the key without loosing it.
# Easier than changing the mode and base_note and doing the mental acrobat.
# Tied to the key_note change, as it gives us an indication of 
# where we are in the key. This allow later to compute the adequat intervals
# to play the right notes. This is again done to simplify the process 
# of playing around in the same key.
def select_key_note(state_controller, playModes_toneProg, tone_progression, note_value):
    temp_note = int((note_value-64)/3)
    degree = 0

    if state_controller["mode"] == "None":
        return temp_note
        state_controller["key_degree"] = 0

    else:
        octave = int(temp_note/7)*12
        inter_octave = 0

        if temp_note >= 0:
            temp = (temp_note%7)
            print(state_controller["mode"])
            for val in playModes_toneProg[state_controller["mode"]][:temp]:
                inter_octave = inter_octave + tone_progression[val]
                degree = degree + 1

        else:
            temp = (temp_note%-7)-1
            for val in playModes_toneProg[state_controller["mode"]][:temp:-1]:
                inter_octave = inter_octave - tone_progression[val]
                degree = degree + 1

        print(f"Key note: {(octave + inter_octave)}")
        print(f"Key degree: {degree}")
        state_controller["key_degree"] = degree
        return (octave+inter_octave)


############################
# PHYSICAL CONTROL SECTION #
############################
# 
def knob_base_note(state_controller, message):
    any_pad_on = False
    for id_pad, pad_on in enumerate(state_controller["state_pad"]):
        if pad_on:
            any_pad_on = True
            temp_note = check_note(state_controller["buffer_note"][id_pad][0] + message.value-64)
            note_on(state_controller, temp_note, id_pad)

    if not any_pad_on:
        state_controller["base_note"] = select_base_note(message.value)

#
def knob_key_note(state_controller, message):
    any_pad_on = False
    for id_pad, pad_on in enumerate(state_pad):
        if pad_on:
            any_pad_on = True
            array_pad_interval = compute_pad_intervals(state_controller["key_degree"])
            # WARNING I DON'T THINK THAT IS GOING TO WORKS ONCE THE KEY_NOTE IS CHANGED
            temp_note = check_note(state_controller["buffer_note"][id_pad][0]+ select_key_note(message.value))
            note_on(state_controller, temp_note, id_pad)

    if not any_pad_on:
        state_controller["key_note"] = select_key_note(message.value)
        state_controller["key_degree"] = select_key_degree(message.value)

# Pad pressed
def pad_pressed(state_controller, base_note_offset, message):
    id_pad = message.note - base_note_offset
    state_controller["state_pad"][id_pad] = 1
    
    note = check_note(message.note - base_note_offset + state_controller["base_note"] + state_controller["key_note"])
    
    state_controller["buffer_velocity"][id_pad] = message.velocity

    note_on(state_controller, note, message.velocity, id_pad)

# Pad released
def pad_released(state_controller, base_note_offset, message):
    state_controller["state_pad"][message.note - base_note_offset] = 0

    for note in state_controller["buffer_note"][message.note-base_note_offset]:
        note_off(note, state_controller["buffer_velocity"][message.note-base_note_offset], message.note - base_note_offset)   
            
    state_controller["buffer_note"][message.note-base_note_offset] = []
    state_controller["buffer_velocity"] = 0




