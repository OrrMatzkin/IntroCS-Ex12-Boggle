import tkinter as tk
from PIL import ImageTk, Image


class WelcomeFrame(tk.Frame):
    """
    The first frame shown when creating a Game class.
    WelcomeFrame is an inherited object from tkinter Frame class.
    """
    _TITLE = 'Boggle !'
    _SUB_TITLE = '3-Minute Word Game'
    _COPYRIGHTS = '@ Avihu Almog & Orr Matzkin'
    _SUB_TITLE_FONT = 'Hobo Std'
    _FONT_TITLE = 'Ubicada Pro'
    _FONT = 'Shree Devanagari 714'

    def __init__(self, parent, controller):
        """
        Initializing WelcomeFrame frame.
        :param parent: frame container (parent widget)
        :param controller: the main Game object
        """
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.title = tk.Label(self, text=self._TITLE,
                              font=(self._FONT_TITLE, 84),
                              fg="red3").pack(side='top', expand='yes')

        load = Image.open("logo_Boggle.png")
        render = ImageTk.PhotoImage(load)
        self.game_logo = tk.Label(self, image=render)
        self.game_logo.image = render
        self.game_logo.pack(side='top', expand='no')

        self.sub_title = tk.Label(self, text=self._SUB_TITLE,
                                  font=(self._SUB_TITLE_FONT, 14),
                                  fg="grey").place(relx=0.37, rely=0.242)

        self.play_button = tk.Button(self, text='Play', font=(self._FONT, 18),
                                     width=16, command=lambda: controller.
                                     set_frame("play_frame")).\
            pack(side='top', expand='yes')

        self.instructions_button = tk.Button(self, text='Instructions',
                                             font=(self._FONT, 18),
                                             width=16,
                                             command=lambda: controller.
                                             set_frame("instructions_frame")).\
            pack(side='top', expand='yes')

        self.copyrights = tk.Label(self, text=self._COPYRIGHTS,
                                   font=('Times New Roman',
                                         12)).pack(side='left', anchor='sw',
                                                   expand='yes')

        load = Image.open("logo_huji.png")
        render = ImageTk.PhotoImage(load)

        self.huji_logo = tk.Label(self, image=render)
        self.huji_logo.image = render
        self.huji_logo.place(relx=0.72, rely=0.85)
