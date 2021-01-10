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
        self.timer = self.frames['play_frame'].timer
        self.words_display = self.frames['play_frame'].words_display

        self._word_dict = load_words_dict()
        self._latest_input = []
        self._user_coordinates_inputs = dict()
        self.found_words = []

    def reset_user_guesses(self):
        self._word_dict = load_words_dict()
        self._latest_input = []
        self._user_coordinates_inputs = dict()
        self.found_words = []

    def set_frame(self, page_name):
        """
        Show a frame for the given page name
        """
        frame = self.frames[page_name]
        frame.tkraise()

    def release(self, event):
        """
        if player releases the left mouse button
        :param event:
        """
        self._latest_input = self.board.get_visited_cube_positions()
        if not self._latest_input:  # if coordinates list is empty
            pass
        elif str(self._latest_input) in self._user_coordinates_inputs:
            # if the current path has already been tried
            pass
        else:
            self._user_coordinates_inputs[str(self._latest_input)] = True
            # add path to paths dictionary
            new_word = is_valid_path(self.random_board, self._latest_input,
                                     self._word_dict)  # check if path points
            # to a valid word
            if new_word and new_word not in self.found_words:  # if the path
                # points to a vaild word that has not been guessed before
                self.add_score(self.calculate_score(self._latest_input))
                self.found_words.append(new_word)
                # TODO add change of colour to the word if correct

        self.board.reset_used_cube()
        self.board.reset()

    def calculate_score(self, word_path: List[Tuple[int, int]]):
        """
        calculates the score for the found word
        :param word_path: the list of coordinates of the word
        """
        return len(word_path) ** 2

    def press_start_button(self):
        """
        if player presses start button
        """
        if not self.timer.time_running:
            self.timer.start_countdown()
            self.board.init_cubes()
            self.frames['play_frame'].start_button.configure(bg='white')

    def press_restart_button(self):
        """
        if player presses restart button
        """
        self.reset_user_guesses()
        self.timer.restart_countdown()
        self.random_board = randomize_board()
        self.board.random_board = self.random_board
        self.board.init_cubes()

    def add_score(self, score):
        self.score.add_score(score)


if __name__ == '__main__':
    app = Game()
    app.mainloop()
