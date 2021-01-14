#################################################################
# FILE : welcome_frame.py
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs Ex12 2020
# DESCRIPTION: The welcome screen frame
# STUDENTS WE DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES WE USED: https://docs.python.org/3.3/library/tkinter.html#images
#################################################################

import tkinter as tk


class WelcomeFrame(tk.Frame):
    """
    The first frame shown when creating a Game class.
    WelcomeFrame is an inherited object from tkinter Frame class.
    """
    _TITLE = {'text': 'Boggle !',
              'font': 'Ubicada Pro',
              'size': 84,
              'color': 'red3'}
    _SUB_TITLE = {'text': '3-Minute Word Game             ',
                  'font': 'Hobo Std',
                  'size': 14,
                  'color': 'grey'}
    _COPYRIGHTS = {'text': '@ Avihu Almog & Orr Matzkin',
                   'font': 'Times New Roman',
                   'size': 12}
    _FONT = 'Shree Devanagari 714'
    _BOGGLE_LOGO_PATH = "assets/logo_Boggle.png"
    _HUJI_LOGO_PATH = 'assets/logo_huji.png'

    def __init__(self, parent, controller):
        """
        Initializing WelcomeFrame frame.
        :param parent: frame container (parent widget)
        :param controller: the main Game object
        """
        tk.Frame.__init__(self, parent)

        self.controller = controller

        self.title = tk.Label(self, text=self._TITLE['text'],
                              font=(self._TITLE['font'], self._TITLE['size']),
                              fg=self._TITLE['color']).pack(side='top', expand='yes')

        self.sub_title = tk.Label(self, text=self._SUB_TITLE['text'],
                                  font=(self._SUB_TITLE['font'],
                                        self._SUB_TITLE['size']),
                                  fg=self._SUB_TITLE['color']).pack(side='top', expand='yes')

        photo = tk.PhotoImage(file=self._BOGGLE_LOGO_PATH)
        self.game_logo = tk.Label(self, image=photo)
        self.game_logo.image = photo
        self.game_logo.pack(side='top', expand='no')

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

        self.copyrights = tk.Label(self, text=self._COPYRIGHTS['text'],
                                   font=(self._COPYRIGHTS['font'],
                                         self._COPYRIGHTS['size'])).\
            pack(side='left', anchor='sw', expand='yes')

        render = tk.PhotoImage(file=self._HUJI_LOGO_PATH)
        self.huji_logo = tk.Label(self, image=render)
        self.huji_logo.image = render
        self.huji_logo.place(relx=0.72, rely=0.85)

