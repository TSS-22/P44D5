import tkinter as tk
from gui.image_item import ImageItem


class WidgetBaseNote(tk.Frame):

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
        rel_x=0.078,
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

        # Indicator base note knob position
        self.knob_arc = canvas.create_arc(
            # Bouding box
            self.pos_x - self.arc_height,  # x0
            self.pos_y - int(widget_height * 0.475),  # y0
            self.pos_x + self.arc_height,  # x1
            self.pos_y - int(widget_height * 0.475) + self.arc_height * 1.93,  # y1
            start=225,
            extent=self.arc_division * 10,
            fill=arc_color,
            outline="",
        )

        # Background image
        self.img_bckgnd = ImageItem(
            canvas=canvas,
            image_path="./res_2/png/bckgnd-base_note.png",
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

        # Label background base note
        canvas.create_text(
            self.pos_x,
            self.pos_y - int(widget_height * 0.03),  # Center of the image
            text="Base note",  # Your label text
            fill=font_color,  # Text color
            font=(label_font, int(label_font_size * 0.5), "bold"),  # Font style
        )

        # Label base note value
        self.label_base_note_val = canvas.create_text(
            self.pos_x,
            self.pos_y + int(widget_height * 0.20),  # Center of the image
            text="C -3",  # Your label text
            fill=arc_color,  # Text color
            font=(label_font, label_font_size, "bold"),  # Font style
        )

    def update(self, base_note):
        self.canvas.itemconfig(
            self.knob_arc, extent=(self.arc_division * base_note + self.arc_division)
        )
        self.img_knob.rotate(self.arc_division * base_note)
        self.canvas.itemconfig(
            self.label_base_note_val, text=self.compute_note(base_note)
        )

    def compute_note(self, base_note):
        octave = int(base_note / 12) - 2
        temp = base_note % 12
        if temp == 1:
            note = "C#"
        elif temp == 2:
            note = "D"
        elif temp == 3:
            note = "D#"
        elif temp == 4:
            note = "E"
        elif temp == 5:
            note = "F"
        elif temp == 6:
            note = "F#"
        elif temp == 7:
            note = "G"
        elif temp == 8:
            note = "G#"
        elif temp == 9:
            note = "A"
        elif temp == 10:
            note = "A#"
        elif temp == 11:
            note = "B"
        else:
            note = "C"

        return f"{note} {octave}"
