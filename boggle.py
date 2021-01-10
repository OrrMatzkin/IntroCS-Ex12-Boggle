import tkinter as tk

from welcome_frame import WelcomeFrame
from instructions_frame import InstructionsFrame
from play_frame import PlayFrame


class Game(tk.Tk):
    """
    A Tk class inherited Game class
    """

    _TITLE_NAME = 'IntroCS Ex12'
    _SCREEN_SIZE = (750, 500)
    _FONT = 'Shree Devanagari 714'
    _FONT_TITLE = 'Ubicada Pro'

    def __init__(self, *args, **kwargs):
        """
        Initializing the inherited class Game.
        Game inherits from a Tk class, meaning the Game is the root Tk.
        :param args: inherited args from Tk class
        :param kwargs: inherited kwargs from Tk class
        """
        # initializing Tk class, Game is the root Tk
        tk.Tk.__init__(self, *args, **kwargs)

        self.geometry(f'{self._SCREEN_SIZE[0]}x{self._SCREEN_SIZE[1]}')
        self.title(self._TITLE_NAME)

        # the container is what holds all frames, the parent widget.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {"welcome_frame": WelcomeFrame(parent=container,
                                                     controller=self),
                       "play_frame": PlayFrame(parent=container,
                                               controller=self),
                       "instructions_frame": InstructionsFrame(
                           parent=container,
                           controller=self)}

        self.frames["welcome_frame"].grid(row=0, column=0, sticky="nsew")
        self.frames["play_frame"].grid(row=0, column=0, sticky="nsew")
        self.frames["instructions_frame"].grid(row=0, column=0, sticky="nsew")

        self.set_frame("welcome_frame")

    def set_frame(self, page_name):
        """
        Show a frame for the given page name
        """
        frame = self.frames[page_name]
        frame.tkraise()


if __name__ == '__main__':
    app = Game()
    app.mainloop()
