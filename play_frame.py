#################################################################
# FILE : play_frame.py
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs2 ex12 2020
# DESCRIPTION: the main program for the boggle program
# STUDENTS WE DISCUSSED THE EXERCISE WITH:
# WEB PAGES WE USED:
#################################################################

import tkinter as tk

from play_objects import Timer, Score, Board, WordDisplay


class PlayFrame(tk.Frame):
    # todo add doc
    _FONT = 'Shree Devanagari 714'

    def __init__(self, parent, controller, random_board):
        # todo add doc

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
        self.score.place(relx=0.05, rely=0.04)

        self.board = Board(container, self, random_board=self.random_board)
        self.board.place(relx=0.10, rely=0.14)

        self.words_display = WordDisplay(container)
        self.words_display.place(relx=0.55, rely=0.295)

        self.hint_button = tk.Button(self, text='Hint',
                                     font=(self._FONT, 18),
                                     width=14,
                                     command=self.controller.confirm_hint).pack(
            side='right')
        self.start_button = tk.Button(self, text='Start',
                                      font=(self._FONT, 18, 'bold'),
                                      width=14,
                                      command=self.controller.switch_start_restart)
        self.start_button.pack(side='right', expand='yes')
        # self.restart_button = tk.Button(self, text='Restart',
        #                                 font=(self._FONT, 18),
        #                                 width=14,
        #                                 command=self.controller.press_restart_button).pack(
        #     side='right')
        self.back_button = tk.Button(self, text='Back',
                                     font=(self._FONT, 18),
                                     width=14,
                                     command=self.controller.press_back_button)
        self.back_button.pack(side='left')
