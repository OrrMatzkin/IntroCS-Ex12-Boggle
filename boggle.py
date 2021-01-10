import tkinter as tk

from boggle_board_randomizer import *
from ex12_utils import *
from instructions_frame import InstructionsFrame
from play_frame import PlayFrame
from welcome_frame import WelcomeFrame


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
        self.random_board = randomize_board()
        # the container is what holds all frames, the parent widget.
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {"welcome_frame": WelcomeFrame(parent=container,
                                                     controller=self),
                       "play_frame": PlayFrame(parent=container,
                                               controller=self,
                                               random_board=self.random_board),
                       "instructions_frame": InstructionsFrame(
                           parent=container,
                           controller=self)}

        self.frames["welcome_frame"].grid(row=0, column=0, sticky="nsew")
        self.frames["play_frame"].grid(row=0, column=0, sticky="nsew")
        self.frames["instructions_frame"].grid(row=0, column=0, sticky="nsew")

        self.set_frame("welcome_frame")
        self.bind('<ButtonRelease-1>', self.release)

        self.board = self.frames['play_frame'].board
        self.score = self.frames['play_frame'].score
        self.words_display = self.frames['play_frame'].words_display

        self._word_dict = load_words_dict()
        self._latest_input = []
        self._user_coordinates_inputs = dict()
        self.found_words = []
        self.score = 0

    def set_frame(self, page_name):
        """
        Show a frame for the given page name
        """
        frame = self.frames[page_name]
        frame.tkraise()

    def release(self, event):
        self._latest_input = self.board.get_visited_cube_positions()
        print(self._latest_input)
        if not self._latest_input:
            pass
        elif str(self._latest_input) in self._user_coordinates_inputs:
            pass
        else:
            self._user_coordinates_inputs[str(self._latest_input)] = True
            new_word = is_valid_path(self.random_board, self._latest_input,
                                     self._word_dict)
            if new_word and new_word not in self.found_words:
                self.add_score(self._latest_input)
                self.found_words.append(new_word)
                print("found word!", new_word)
                print("score", self.score)

        self.board.reset_used_cube()
        self.board.reset()

    def add_score(self, word_path: List[Tuple[int, int]]):
        self.score += len(word_path) ** 2


if __name__ == '__main__':
    app = Game()
    app.mainloop()
