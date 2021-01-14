#################################################################
# FILE : boggle.py
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs Ex12 2020
# DESCRIPTION: the main program for the boggle program
# STUDENTS WE DISCUSSED THE EXERCISE WITH:
# WEB PAGES WE USED:
# Graphical User Interfaces with Tk - https://docs.python.org/3/library/tk.html
# itertools — Functions creating iterators for efficient looping -
# https://docs.python.org/3/library/itertools.html
#################################################################

import tkinter as tk
from tkinter import messagebox
from boggle_board_randomizer import *
from ex12_utils import *
from frames.instructions_frame import InstructionsFrame
from frames.play_frame import PlayFrame
from frames.welcome_frame import WelcomeFrame


class Game(tk.Tk):
    """
    A Tk class inherited Game class.
    """
    _SCREEN_SIZE = (750, 500)
    _SCORE_COEFFICIENT = 2
    _HINT_COST = 2
    TIME_IN_SECONDS = 180

    _GAME_TITLE = 'IntroCS Ex12'

    _FONT = 'Shree Devanagari 714'

    _EXIT_TEXT = 'Are you sure you want to exit your ongoing game?'
    _RESTART_TEXT = 'Are you sure you want to restart your ongoing game?'
    _REMINDER_TEXT = 'To start a new game just press start...'
    _HINT_TEXT = f"The cost of a hint is {_HINT_COST} points,\n" \
                 f"You don't have enough points."

    def __init__(self, *args, **kwargs):
        """
        Initializing the inherited class Game.
        Game inherits from a Tk class, meaning the Game is the root Tk.
        :param args: inherited args from Tk class
        :param kwargs: inherited kwargs from Tk class
        """
        # initializing Tk class, the Game is the root Tk
        tk.Tk.__init__(self, *args, **kwargs)
        self.resizable(width=False, height=False)
        self.geometry(f'{self._SCREEN_SIZE[0]}x{self._SCREEN_SIZE[1]}')
        self.title(self._GAME_TITLE)

        self.random_board = randomize_board()
        self._word_dict = load_words_dict()

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

        self.bind('<ButtonRelease-1>', self.game_cycle)

        self.board = self.frames['play_frame'].board
        self.score = self.frames['play_frame'].score
        self.timer = self.frames['play_frame'].timer
        self.words_display = self.frames['play_frame'].words_display

        self._latest_user_input = []
        self._user_coordinates_inputs = dict()
        self.found_words = []
        self.given_hints = []
        self.last_hint = None

    def set_frame(self, page_name):
        """
        Shows a frame for the given page name.
        """
        frame = self.frames[page_name]
        frame.tkraise()

    def game_cycle(self, event):
        """
        This is a single game cycle, this function is called every time the
        player releases the left mouse button. The main purpose of function
        is to check the validity of the created word.
        :param event: a bind event (not used)
        """
        self._latest_user_input = self.board.get_visited_cubes_positions()
        # if coordinates list is empty
        if not self._latest_user_input:
            pass
        # if the current path has already been tried
        elif str(self._latest_user_input) in self._user_coordinates_inputs:
            self.board.color_selected_cubes(False)
        else:
            # add path to paths dictionary
            self._user_coordinates_inputs[str(self._latest_user_input)] = True
            # checks if path points to a valid word
            new_word = is_valid_path(self.random_board, self._latest_user_input,
                                     self._word_dict)
            # if path points to a valid word that has notbeen guessed before
            if new_word and new_word not in self.found_words:
                self.add_score(len(self._latest_user_input) **
                               self._SCORE_COEFFICIENT)
                self.board.color_selected_cubes(True)
                self.words_display.add_word(new_word)
                self.found_words.append(new_word)
            else:
                self.board.color_selected_cubes(False)

        self.after(400, self.board.reset_used_cube)
        self.board.reset_board()

    def reset_user_guesses(self):
        """
        Rests all assets associated with user previous actions in the game
        """
        self._word_dict = load_words_dict()
        self._latest_user_input = []
        self._user_coordinates_inputs = dict()
        self.found_words = []
        self.given_hints = []
        self.last_hint = None

    def switch_start_restart(self):
        """
        Switches the Start Button in PlayFrame to Restart button and also the
        other way around accordingly to if the game is running or not.
        """
        if not self.timer.time_running:
            self.press_start_button()
            self.frames['play_frame'].start_button.configure(text='Restart')
        else:
            self.timer.stop_countdown()
            self.board.hide_and_show_cube_labels(True)
            self.after(100, self.restart_confirm)

    def press_start_button(self):
        """
        If player presses start button.
        """
        if not self.timer.time_running:
            self.timer.start_countdown()
            self.board.init_cubes()
            self.reset_user_guesses()
            self.frames['play_frame'].start_button.configure(font=(self._FONT,
                                                                   16))

    def press_restart_button(self):
        """
        If player presses restart button.
        """
        self.frames['play_frame'].start_button.configure(text='Start')
        self.frames['play_frame'].start_button.configure(font=(self._FONT, 16,
                                                               'bold'))
        self.reset_user_guesses()
        self.timer.stop_countdown()
        self.timer.reset_timer()
        self.score.reset_score()
        self.random_board = randomize_board()
        self.board.random_board = self.random_board
        self.board.init_cubes()
        self.board.hide_and_show_cube_labels(True)
        self.words_display.reset_words()

    def press_back_button(self):
        """
        If player presses main menu button.
        """
        if not self.timer.time_running:
            self.set_frame("welcome_frame")
        else:
            self.board.hide_and_show_cube_labels(True)
            self.after(100, self.back_confirm)

    def restart_confirm(self):
        """
        Displays a confirmation window before restarting the game.
        If user presses 'YES' the game restart, if user presses 'NO' the game
        continues.
        """
        rest_conf_window = tk.messagebox.askyesno('Restart Game',
                                                  self._RESTART_TEXT,
                                                  icon='question')
        if rest_conf_window:
            tk.messagebox.showinfo('Reminder', self._REMINDER_TEXT,
                                   icon='info')
            self.press_restart_button()
        else:
            self.board.hide_and_show_cube_labels(False)
            self.timer.start_countdown()

    def back_confirm(self):
        """
        Displays a confirmation window before exiting the game.
        If user presses 'YES' the game stops and the user gets back
        to the welcome screen, if user presses 'NO' the game continues.
        """
        time_was_running = self.timer.time_running
        self.timer.stop_countdown()
        back_conf_window = tk.messagebox.askyesno('Exit Game',
                                        self._EXIT_TEXT,
                                        icon='question')
        if back_conf_window:
            self.press_restart_button()
            self.set_frame("welcome_frame")
        else:
            if time_was_running:
                self.timer.start_countdown()
                self.board.hide_and_show_cube_labels(False)

    def add_score(self, score):
        """
        Adds the given score to score and updates the Score Widget.
        :param score: score (int)
        """
        self.score.add_score(score)

    def confirm_hint(self):
        """
        Checks if the user has enough points to use the hint option.
        If there isn't enough points the function show a an error message,
        else give the user a hint.

        """
        if self.score.score - self._HINT_COST > 0:
            self.score.add_score(-self._HINT_COST)
            self.give_hint()
        else:
            tk.messagebox.showinfo('Not enough score', self._HINT_TEXT,
                                   icon='info')

    def give_hint(self):
        """
        Gives the player a hint for a word on the board.
        :return:
        """
        # if game is not currently ongoing
        if not self.timer.time_running:
            return
        while True:
            hint_length = random.randint(3, 4)
            # generates a hint
            optional_hints = find_length_n_words(hint_length,
                                                 self.random_board,
                                                 self._word_dict)
            if not optional_hints:
                continue
            else:
                while True:
                    checked_hint = optional_hints[
                        random.randint(0, len(optional_hints) - 1)]
                    # checks hint validity
                    if str(checked_hint[1]) not in \
                            list(self._user_coordinates_inputs.keys()) \
                            and checked_hint not in self.given_hints and \
                            checked_hint[0] not in self.found_words:
                        self.last_hint = checked_hint
                        self.given_hints.append(self.last_hint)
                        if len(self.given_hints) > 10:
                            self.given_hints.pop(0)
                        self.board.color_hint(self.last_hint)
                        break
            break

    def end_of_time(self):
        """
        Displays a the end game message with the current game achievements.
        """
        end_message = tk.messagebox.showinfo("Time's over",
                                         f'Well done!\n\nScore: '
                                         f'{self.score.score}\nWords found: '
                                         f'{self.words_display.get_length()}')
        if end_message:
            self.press_restart_button()


if __name__ == '__main__':
    game = Game()
    game.mainloop()
