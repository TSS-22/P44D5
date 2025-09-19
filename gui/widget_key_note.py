import math
import tkinter as tk
from gui.image_item import ImageItem


class WidgetKeyNote(tk.Frame):

    arc_division = -(270 / 128)
    arc_height = 72
    arc_width = arc_height

    def __init__(
        self,
        master=None,
        canvas=None,
        widget_width=168,
        widget_height=415,
        canvas_width=1200,
        canvas_height=760,
        bckgnd_color="#260006",
        font_color="#340006",
        arc_color="#00ff00",
        label_font="Arial",
        label_font_size=36,
        rel_x=1 - 0.078,
        rel_y=0.715,
    ):
        super().__init__(master=master, width=widget_width, height=widget_height)
        self.pos_x = int(canvas_width * rel_x)
        self.pos_y = int(canvas_height * rel_y)
        self.widget_width = widget_width
        self.widget_height = widget_height
        self.canvas = canvas

        # Background arc
        canvas.create_rectangle(
            # Bouding box
            self.pos_x - int(widget_width * 0.4),  # x0
            self.pos_y - int(widget_height * 0.47),  # y0
            self.pos_x + int(widget_width * 0.4),  # x1
            self.pos_y - int(widget_height * 0.1),  # y1
            fill=bckgnd_color,
            outline="",
        )

        # Indicator key note knob position
        self.knob_arc = canvas.create_arc(
            # Bouding box
            self.pos_x - self.arc_height,  # x0
            self.pos_y - int(widget_height * 0.475),  # y0
            self.pos_x + self.arc_height,  # x1
            self.pos_y - int(widget_height * 0.475) + self.arc_height * 1.93,  # y1
            start=225,
            extent=self.arc_division * 1,
            fill=arc_color,
            outline="",
        )

        # Background image
        self.img_bckgrnd = ImageItem(
            canvas=canvas,
            image_path="./res_2/png/bckgnd-key_note.png",
            width=widget_width,
            height=widget_height,
            x=self.pos_x,
            y=self.pos_y,
        )

        # Knob image
        self.img_knob = ImageItem(
            canvas=canvas,
            image_path="./res_2/png/knob.png",
            width=int(widget_width * 0.85),
            height=int(widget_width * 0.85),
            x=self.pos_x,
            y=self.pos_y - int(widget_height * 0.3),
        )

        # Label background key degree
        canvas.create_text(
            self.pos_x,
            self.pos_y - int(widget_height * 0.08),  # Center of the image
            text="Key degree",  # Your label text
            fill=font_color,  # Text color
            font=(label_font, int(label_font_size * 0.5), "bold"),  # Font style
        )

        # Label background octave
        canvas.create_text(
            self.pos_x,
            self.pos_y + int(widget_height * 0.21),  # Center of the image
            text="Octave",  # Your label text
            fill=font_color,  # Text color
            font=(label_font, int(label_font_size * 0.5), "bold"),  # Font style
        )

        # Label key degree value
        self.label_key_degree_val = canvas.create_text(
            self.pos_x,
            self.pos_y + int(widget_height * 0.07),  # Center of the image
            text="7",  # Your label text
            fill=arc_color,  # Text color
            font=(label_font, label_font_size, "bold"),  # Font style
        )

        # Label octave value
        self.label_octave_val = canvas.create_text(
            self.pos_x,
            self.pos_y + int(widget_height * 0.35),  # Center of the image
            text="+3",  # Your label text
            fill=arc_color,  # Text color
            font=(label_font, label_font_size, "bold"),  # Font style
        )

    def update(self, key_degree, raw_key_knob):
        self.canvas.itemconfig(
            self.knob_arc, extent=(self.arc_division * raw_key_knob + self.arc_division)
        )
        self.img_knob.rotate(self.arc_division * raw_key_knob)
        self.canvas.itemconfig(self.label_key_degree_val, text=f"{key_degree}")
        self.canvas.itemconfig(
            self.label_octave_val, text=self.compute_octave(raw_key_knob)
        )

    def compute_octave(self, raw_key_knob):
        temp_note = int((raw_key_knob - 64) / 3)
        octave = int(temp_note / 7) * 12
        octave = math.floor(octave / 12) if octave >= 0 else math.ceil(octave / 12)
        return f"{octave}"
