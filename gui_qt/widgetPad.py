from PySide6.QtWidgets import QFrame, QPushButton, QStackedLayout, QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QFont


class WidgetPad(QFrame):

    def __init__(
        self,
        parent=None,
        note="C -3",
        root=False,
        pad_pressed=False,
        widget_width=180,
        widget_height=180,
        canvas_width=1200,
        canvas_height=760,
        font="Liberation sans",
        font_size=48,
        font_color="#00ff00",
        rel_x=0.078,
        rel_y=0.715,
    ):
        super().__init__(parent=parent)
        self.widget_width = widget_width
        self.widget_height = widget_height
        self.setFixedSize(self.widget_width, self.widget_height)
        self.root = root
        self.pad_pressed = pad_pressed

        if self.root:
            self.bckgnd_button = "bckgnd-pad_root.png"
        else:
            self.bckgnd_button = "bckgnd-pad.png"

        if self.pad_pressed:
            self.bckgnd_active = "bckgnd-pad_active.png"
        else:
            self.bckgnd_active = ""

        self.lbl_note_properties = {
            "font": font,
            "font_size": font_size,
            "color": font_color,
            "note": note,
        }

        self.setStyleSheet(
            """
                border: none; 
                background: transparent;	
            """
        )

        self.active = QLabel(parent=self, text="")
        self.active.setFixedSize(self.widget_width, self.widget_height)
        self.active.setStyleSheet(
            f"""
                background-repeat: no-repeat;
                background-position: center;
                border: none; 	
                background-image: url(qt-ressources/png/{self.bckgnd_active});
            """
        )

        self.note_font = QFont()
        self.note_font.setFamily(self.lbl_note_properties["font"])
        self.note_font.setPointSize(self.lbl_note_properties["font_size"])

        self.button = QPushButton(parent=self, text=self.lbl_note_properties["note"])
        self.button.setFont(self.note_font)
        self.button.setFixedSize(self.widget_width, self.widget_height)
        self.button.setStyleSheet(
            f"""
                background-repeat: no-repeat;
                background-position: center;
                border: none; 	
                background-image: url(qt-ressources/png/{self.bckgnd_button});
                color: {font_color};
            """
        )

        self.stack = QStackedLayout()
