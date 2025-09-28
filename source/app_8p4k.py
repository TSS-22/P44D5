import threading
import queue
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
        self.midi_queue = queue.Queue()  # Thread-safe queue for MIDI messages

    def midi_polling_thread(self):
        while self.app_running:
            polled_msg = self.midi_bridge.input.poll()
            if polled_msg:
                self.midi_queue.put(polled_msg)  # Add message to queue
            time.sleep(0.001)  # Small sleep to prevent CPU overload

    def main_loop(self):
        # polled_msg = self.midi_bridge.input.poll()
        # if polled_msg:
        #     self.midi_bridge.bridge_out(
        #         self.midi_controller.receive_message(polled_msg)
        #     )
        #     self.main_canvas.update(self.midi_controller.get_state())
        # self.root.after(32, self.main_loop)
        # # time.sleep(0.016)  # ~60 FPS
        # # time.sleep(0.008)  # ~120 FPS
        # # time.sleep(0.032)  # ~30 FPS
        try:
            # Process all pending MIDI messages
            while True:
                polled_msg = self.midi_queue.get_nowait()
                self.midi_bridge.bridge_out(
                    self.midi_controller.receive_message(polled_msg)
                )
                self.main_canvas.update(self.midi_controller.get_state())
        except queue.Empty:
            pass
        self.root.after(16, self.main_loop)  # ~60 FPS

    def on_close(self):
        self.app_running = False

    def start(self):
        # while self.app_running:
        #     self.main_loop()
        # self.stop()
        midi_thread = threading.Thread(target=self.midi_polling_thread, daemon=True)
        midi_thread.start()
        # Start the GUI loop
        self.root.after(16, self.main_loop)
        self.root.mainloop()
        self.stop()

    def stop(self):
        self.midi_bridge.stop()
        self.root.destroy()
        exit()
