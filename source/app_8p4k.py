import tkinter as tk
import time
from gui.ui_canvas import UiCanvas
from source.midi_controller import MidiController
from source.midi_bridge import MidiBridge


class App8P4K:

    def __init__(
        self,
        canvas_height=1200,
        canvas_width=760,
    ):
        self.midi_controller = MidiController()
        self.midi_bridge = MidiBridge()
        self.app_running = True
        self.root = tk.Tk()
        self.root.title("8P4K Power House")
        self.root.geometry(f"{canvas_height}x{canvas_width}")
        self.root.resizable(width=False, height=False)
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.main_canvas = UiCanvas(master=self.root)

    def main_loop(self):
        polled_msg = self.midi_bridge.input.poll()
        if polled_msg:
            self.midi_bridge.bridge_out(
                self.midi_controller.receive_message(polled_msg)
            )
        # main_canvas.update(midi_controller.get_state())
        self.root.update_idletasks()
        self.root.update()
        time.sleep(0.016)  # ~60 FPS

    def on_close(self):
        self.app_running = False

    def start(self):
        while self.app_running:
            self.main_loop()
        self.stop()

    def stop(self):
        self.midi_bridge.stop()
        self.root.destroy()
        exit()
