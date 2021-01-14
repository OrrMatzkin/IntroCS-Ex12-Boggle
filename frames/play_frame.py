#################################################################
# FILE : play_frame.py
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs Ex12 2020
# DESCRIPTION: The playing screen frame
# STUDENTS WE DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES WE USED: N/A
#################################################################

import tkinter as tk
from play_objects import Timer, Score, Board, WordDisplay


class PlayFrame(tk.Frame):
    """
    The playing screen (frame) of the game.
    PlayFrame is an inherited object from tkinter Frame class.
    """
    _FONT = 'Shree Devanagari 714'

    def __init__(self, parent, controller, random_board):
        """
        Initiates the playing page of the game.
        This function creates the Timer, Score, Board and WordDisplay objects.
        :param parent: the root of the game
        :param controller: the Game class
        :param random_board: a 4x4 board (list of lists)
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.random_board = random_board
        self.board = Board(container, self, random_board=self.random_board)
        self.board.place(relx=0.10, rely=0.14)

        self.timer = Timer(container, self.controller)
        self.timer.place(relx=0.82, rely=0.04)

        self.score = Score(container)
        self.score.place(relx=0.05, rely=0.046)

        self.words_display = WordDisplay(container)
        self.words_display.place(relx=0.6, rely=0.295)

        self.hint_button = tk.Button(self,
                                     text=f'Hint (-{self.controller._HINT_COST})',
                                     font=(self._FONT, 16),
                                     width=14,
                                     command=self.controller.confirm_hint).\
            pack(side='right')

        self.start_button = tk.Button(self, text='Start',
                                      font=(self._FONT, 16, 'bold'),
                                      width=14,
                                      command=self.controller.
                                      switch_start_restart)
        self.start_button.pack(side='right', expand='yes')

        self.back_button = tk.Button(self, text='Main Menu',
                                     font=(self._FONT, 16),
                                     width=14,
                                     command=self.controller.press_back_button)
        self.back_button.pack(side='left')
