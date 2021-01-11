import tkinter as tk

from play_objects import Timer, Score, Board, WordDisplay


class PlayFrame(tk.Frame):
    _FONT = 'Shree Devanagari 714'

    def __init__(self, parent, controller, random_board):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)
        self.random_board = random_board
        self.timer = Timer(container)
        self.timer.grid(row=0, column=2, sticky='ne')
        self.score = Score(container)
        self.score.grid(row=0, column=3, sticky='ne')

        self.board = Board(container, self, random_board=self.random_board)
        self.board.grid(row=0, column=1, sticky="nsew")

        self.words_display = WordDisplay(container)
        self.words_display.grid(row=0, column=2, columnspan=2)

        self.hint_button = tk.Button(self, text='Hint', font=(self._FONT, 18),
                                     width=14).pack(side='right')
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
                                     width=14, command=lambda: controller.
                                     set_frame("welcome_frame")).pack(
            side='left')




