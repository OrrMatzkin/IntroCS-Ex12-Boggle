import tkinter as tk
from play_objects import Timer, Score, Cube, Board, WordDisplay


class PlayFrame(tk.Frame):
    _FONT = 'Shree Devanagari 714'

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        self.timer = Timer(container).grid(row=0, column=2, sticky='ne' )
        self.high_score = Score(container).grid(row=0, column=3, sticky='ne' )

        self.board = Board(container,self)
        self.board.grid(row=0, column=1, sticky="nsew",)

        self.words_display = WordDisplay(container)
        self.words_display.grid(row=0, column=2, columnspan=2)
        self.back_button = tk.Button(self, text='Back', font=(self._FONT, 18),
                                     width=14, command=lambda: controller.
                                     set_frame("welcome_frame")).pack(side='right')
        self.restart_button = tk.Button(self, text='Restart', font=(self._FONT, 18),
                                     width=14).pack(
            side='right')
        self.hint_button = tk.Button(self, text='Hint',
                                        font=(self._FONT, 18),
                                        width=14).pack(
            side='left')
        # self.button = tk.Button(self, text="back",
        #                     command=lambda: controller
        #                     .set_frame("welcome_frame")).pack().grid(row=3, column=2,)

        self.controller.bind('<ButtonRelease-1>', self.release)


    def release(self, event):
        print(self.board.get_visited_cube_positions())
        self.board.reset_used_cube()
        self.board.reset()



