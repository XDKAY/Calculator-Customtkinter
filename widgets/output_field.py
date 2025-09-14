import customtkinter
from config import Config


conf = Config()


class OutputFiled(customtkinter.CTkTextbox):
    def __init__(self, master):
        self.width = master.winfo_screenwidth()
        self.height = int(conf.WINDOW_SIZE[1]*0.11)

        self._font = conf.FONT

        self._fg_color = conf.FG_COLOR_TEXTBOX
        self.wrap = 'none'

        self._scrollbars_activated = True
        self._hide_x_scrollbar = True
        self._hide_y_scrollbar = False

        self._corner_radius = conf.CORNER_RADIUS

        super().__init__(
            master=master,
            width=self.width,
            height=self.height,
            font=self._font,
            fg_color=self._fg_color,
            wrap=self.wrap, 
            activate_scrollbars=True,
            xscrollcommand=True,
            yscrollcommand=False,
            corner_radius=self._corner_radius
        )