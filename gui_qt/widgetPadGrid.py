from PySide6.QtWidgets import QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QPalette, QColor, QFont


class WidgetPadGrid(QFrame):

    list_note = [
        "C -3",
        "D -3",
        "E -3",
        "F -3",
        "G -3",
        "A -3",
        "B -3",
        "C -2",
    ]  # HARDOCDED + TEST

    def __init__(
        self,
        parent=None,
        widget_width=818,
        widget_height=418,
        canvas_width=1200,
        canvas_height=760,
        knob_color="#eeeeee",
        lbl_font="Liberation sans",
        lbl_font_size=20,
        lbl_font_color="#340006",
        rel_x=0.078,
        rel_y=0.715,
    ):
        super().__init__(parent)

        self.pos_x = int(canvas_width * rel_x)
        self.pos_y = int(canvas_height * rel_y)
        self.widget_width = widget_width
        self.widget_height = widget_height

        self.setFixedSize(self.widget_width, self.widget_height)
        self.setStyleSheet(
            """            
            background-repeat: no-repeat;
            background-position: center;
            border: none; 	
            background-image: url(qt-ressources/png/qt-bckgnd-pad_grid.png);
            """
        )
