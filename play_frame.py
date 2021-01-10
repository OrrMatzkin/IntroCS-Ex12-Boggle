import tkinter as tk
from play_objects import Timer, Score, Cube, Board, WordDisplay


class PlayFrame(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        # container.grid_rowconfigure(0, weight=1)
        # container.grid_columnconfigure(0, weight=1)

        self.timer = Timer(container).grid(row=0, column=1, sticky="nsew")
        self.high_score = Score(container).grid(row=0, column=2, sticky="nsew")
        self.board = Board(container,self)

        self.board.grid(row=1, column=1, sticky="nsew")

        self.button = tk.Button(self, text="back",
                                command=lambda: controller
                                .set_frame("welcome_frame")).pack()

        self.controller.bind('<ButtonRelease-1>', self.release)


    def release(self, event):
        self.board.reset_used_cube()
        self.board.reset()


