from midi_controller import MidiController
from midi_bridge import MidiBridge

# from nicegui import ui
import asyncio

midi_controller = MidiController()

midi_bridge = MidiBridge()

#################
# UI DEFINITION #
#################
# ui.label("Hello NiceGUI!")


async def main2(midi_controller, midi_bridge):
    await midi_bridge.start(midi_controller)


asyncio.run(main2(midi_controller, midi_bridge))
# ui.run(main=main2)
