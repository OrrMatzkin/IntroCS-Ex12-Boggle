#################################################################
# FILE : game_objects.py
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs Ex12 2020
# DESCRIPTION: A python file with the game classes
# STUDENTS WE DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES WE USED: https://www.tutorialspoint.com/python/tk_listbox.htm
#                    https://www.tutorialspoint.com/python/tk_scrollbar.htm
#################################################################

import tkinter as tk
import datetime
from typing import List


class Timer(tk.Frame):
    """
    The timer of the game.
    Timer is an inherited object from tkinter Frame class.
    """
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 40

    def __init__(self, parent, controller):
        """
        Initializing the Timer.
        :param parent: frame container (parent widget)
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.time_running = False
        self.seconds_left = self.controller.TIME_IN_SECONDS
        self._timer_display = tk.Label(self,
                                       text=self.convert_seconds_str(),
                                       font=(self._FONT, self._FONT_SIZE))
        self._timer_display.grid()

    def start_countdown(self):
        """
        Starts the countdown.
        If time has not reach zero the function will subtract 1 second from
        the time left and then will call itself again after 1000
        milliseconds.
        Each call it sets the text value of the timer_display label to the
        new time left.
        """
        if self.seconds_left:
            self.time_running = True
            self.seconds_left -= 1
            self.time_running = self.after(1000, self.start_countdown)
            if self.seconds_left <= 30:
                self._timer_display['fg'] = 'red2'
        else:
            self.time_running = False
            self.controller.end_of_time()
        self._timer_display['text'] = self.convert_seconds_str()

    def stop_countdown(self):
        """
        Stops the countdown.
        """
        if self.time_running:
            self.after_cancel(self.time_running)
            self.time_running = False

    def reset_timer(self):
        """
        Reset the countdown.
        """
        self.seconds_left = self.controller.TIME_IN_SECONDS
        self._timer_display['text'] = self.convert_seconds_str()
        self._timer_display['fg'] = 'black'

    def convert_seconds_str(self):
        """
        Converts the seconds to time format and then returning the sliced
        string to show only the minutes.
        """
        time_remain = datetime.timedelta(seconds=self.seconds_left)
        return str(time_remain)[3:]


class Score(tk.Frame):
    """
    The score of the game.
    Score is an inherited object from tkinter Frame class.
    """
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 34

    def __init__(self, parent):
        """
        Initializing the Score frame.
        :param parent: frame container (parent widget)
        """
        tk.Frame.__init__(self, parent)
        self.score = 0
        self._score_display = tk.Label(self, text=f'Score: {self.score}',
                                       font=(self._FONT, self._FONT_SIZE))
        self._score_display.pack()

    def add_score(self, score=1):
        """
        Adds the given points amount to the score and updates the label
        accordingly.
        :param score: the amount of points to add
        """
        self.score += score
        self._score_display['text'] = f'Score: {self.score}'

    def reset_score(self):
        """
        Resets the score back to zero and updates the label accordingly.
        """
        self.score = 0
        self._score_display['text'] = f'Score: {self.score}'


class Cube(tk.Frame):
    """
    The board cube.
    Cube is an inherited object from tkinter Frame class.
    """
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 22
    _WIDTH = 3
    _HEIGHT = 1
    _COLORS = {'main': 'white',
               'chosen': 'MistyRose4',
               'correct': 'SpringGreen3',
               'wrong': 'firebrick3',
               'hint': 'sienna1'}

    def __init__(self, parent, controller, letter, pos_x, pos_y):
        """
        Initializing the Cube.
        :param parent: frame container (parent widget)
        :param controller: the widget controller
        :param letter: the letter for the cube
        :param pos_x: the x position in the board
        :param pos_y: the y position in the board
        """

        tk.Frame.__init__(self, parent)
        self.configure(borderwidth=2, padx=6, pady=8)
        self.controller = controller
        self.letter = letter
        self.entered = False
        self.position = (pos_x, pos_y)

        self.content = tk.Label(self, padx=2, pady=2, cursor='hand1',
                                text=self.letter,
                                font=(self._FONT, self._FONT_SIZE),
                                width=self._WIDTH, height=self._HEIGHT,
                                bg=self._COLORS['main'], relief="raised",
                                borderwidth=4)
        self.content.grid()

        self.content.bind("<B1-Motion>", self.generate_events)
        self.content.bind("<Button-1>", self.mouse_enter_or_click)
        self.content.bind("<<B1-Enter>>", self.mouse_enter_or_click)

    def mouse_enter_or_click(self, event):
        """
        A method triggered when a cube is clicked or the mouse have entered
        a cube after another cube is pressed.
        The method check if the cube haven't already entered and if the cube is
        a valid option for the last cube to create a word. If so the cube color
        is changed and her letter adds to the current word' her controller
        (board) is holding.
        :param event: a bind event (not used)
        """
        if not self.entered and self.controller.valid_next_cube(
                self) and self.letter:
            self.content.configure(bg=self._COLORS['chosen'])
            self.controller.add_letter_to_current_word(self.letter)
            self.controller.add_position_to_positions_path(self.position)
            self.entered = True
            self.controller.set_last_cube_visited(self)

    def generate_events(self, event):
        """
        Generates a new event sequences: <<B1-Enter>>
        meaning a cube is entered while (!) another cube is pressed.
        :param event: bind event
        """
        # widget is the widget which is at the mouse coordinates
        widget = self.winfo_containing(event.x_root, event.y_root)
        # checks if widget is the same widget
        if self.content != widget:
            current_widget = widget
            try:
                current_widget.event_generate("<<B1-Enter>>")
            # when the current_widget is None
            except AttributeError:
                pass

    def hide_and_show_label(self, hide):
        """
        Hide or Show the cube content.
        if hide is True the function hides the content of herself,
        if hide is False the function sets the content to be the cube letter.
        :param hide: a boolean representing if to show or hide the content
        """
        if hide:
            self.content.configure(text='')
        if not hide:
            self.content.configure(text=self.letter)

    def get_position(self):
        """
        Returns the cube positions in board.
        :return: cube position as a Tuple
        """
        return self.position

    def get_letter(self):
        """
        Returns the letter in the cube.
        :return: the cube letter in string
        """
        return self.letter

    def set_main_color(self):
        """
        Sets the cube color back to main color.
        """
        self.content.configure(bg=self._COLORS['main'])

    def set_content(self, content):
        """
        Sets the cube letter to the given new content.
        :param content: a string value of letter/s
        """
        self.letter = content
        self.content.configure(text=self.letter)

    def set_correct_color(self):
        """
        Sets the color of the cube to _CORRECT_COLOR
        """
        self.content.configure(bg=self._COLORS['correct'])

    def set_wrong_color(self):
        """
        Sets the color of the cube to _WRONG_COLOR
        """
        self.content.configure(bg=self._COLORS['wrong'])

    def set_hint_color(self):
        """
        Sets the color of the cube to _HINT_COLOR
        """
        self.content.configure(bg=self._COLORS['hint'])


class Board(tk.Frame):
    """
    The main board.
    Board is an inherited object from tkinter Frame class.
    """
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 30

    def __init__(self, parent, controller, random_board: List[List[str]]):
        """
        Initializing Board.
        :param parent: frame container (parent widget)
        :param controller: the widget controller
        :param random_board: a 4x4 board (list of lists)
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(padx=10, pady=10)
        self.random_board = random_board

        self.current_word = ''
        self.word_display = tk.Label(self, text=self.current_word,
                                     font=(self._FONT, self._FONT_SIZE))
        self.word_display.pack()

        self.container = tk.Frame(self)
        self.container.pack()

        self.cubes = []
        self.init_cubes(True)

        self.current_visited_positions = []
        self.last_cube_visited = None

    def init_cubes(self, first: bool = False):
        """
        Initializing the board cubes.
        If first is True the function is actually creating the cubes
        objects, if first is False the function sets the content
        of each cube to the the accordingly cell in random_board.
        :param first: a boolean representing if this the first init made
        """
        for pos_x in range(len(self.random_board)):
            row = []
            for pos_y in range(len(self.random_board[0])):
                if first:
                    cube = Cube(self.container, self, '', pos_x, pos_y)
                    cube.grid(row=pos_x, column=pos_y, sticky="nsew")
                    row.append(cube)
                else:
                    self.cubes[pos_x][pos_y].set_content(self.random_board[
                                                             pos_x][pos_y])
            if first:
                self.cubes.append(row)

    def reset_board(self):
        """
        Reverts the board back to when first Initialized, but without changing
        the cubes.
        """
        self.current_word = ''
        self.current_visited_positions = []
        self.last_cube_visited = None
        self.word_display.configure(text=self.current_word)

    def reset_used_cube(self):
        """
        Reset all cubes in board, meaning reverting them back how they was when
        first Initialized.
        """
        for i in range(len(self.cubes)):
            for j in range(len(self.cubes[i])):
                self.cubes[i][j].set_main_color()
                self.cubes[i][j].entered = False

    def add_letter_to_current_word(self, letter):
        """
        Adds given letter to the ongoing word.
        :param letter: a string representing a cube letter
        """
        self.current_word += letter
        self.word_display.configure(text=self.current_word)

    def add_position_to_positions_path(self, cube_position):
        """
        Adds given position to the visited positions list.
        :param cube_position: a tuple representing a cube position in board
        """
        self.current_visited_positions.append(cube_position)

    def get_visited_cube_positions(self):
        """
        Returns the all visited cube position
        :return: a list of positions (tuples)
        """
        return self.current_visited_positions

    def get_word(self):
        """
        Returns the word created.
        :return: a string word
        """
        return self.current_word

    def set_last_cube_visited(self, cube):
        """
        Sets last_cube_visited to the given cube
        :param cube: a Cube object
        """
        self.last_cube_visited = cube

    def valid_next_cube(self, cube):
        """
        Check if the given cube is a valid cube (the given cube is a neighbor
        with the last visited cube.
        :param cube: a Cube object
        :return: True is given cube is a neighbor and False if not
        """
        if self.last_cube_visited is None:
            return True
        else:
            return cube.get_position() in \
                   self.get_all_possible_neighbours_position(
                       self.last_cube_visited)

    def get_all_possible_neighbours_position(self, cube):
        """
        Returns a list with all the valid cubes positions (neighbours) for
        the given cube.
        :param cube: a Cube object
        :return: list of all valid positions (list of tuples)
        """
        cube_pos = cube.get_position()
        possible_neighbours_position = [(cube_pos[0] - 1, cube_pos[1] - 1),
                                        (cube_pos[0] - 1, cube_pos[1]),
                                        (cube_pos[0] - 1, cube_pos[1] + 1),
                                        (cube_pos[0], cube_pos[1] - 1),
                                        (cube_pos[0], cube_pos[1] + 1),
                                        (cube_pos[0] + 1, cube_pos[1] - 1),
                                        (cube_pos[0] + 1, cube_pos[1]),
                                        (cube_pos[0] + 1, cube_pos[1] + 1)]
        return [pos for pos in possible_neighbours_position if 0 <=
                pos[0] <= 3 and 0 <= pos[1] <= 3]

    def hide_and_show_cube_labels(self, hide):
        """
        Hides and shows all cubes content accordingly to the boolean value
        given. If hide is True the function hides the cube content, if hide is
        False the function shows the cubes content.
        :param hide: a boolean representing the decision for the function
        """
        for pos_x in range(len(self.random_board)):
            for pos_y in range(len(self.random_board[0])):
                self.cubes[pos_x][pos_y].hide_and_show_label(hide)

    def color_selected_cubes(self, valid_word):
        """
        Colors the selected cubes. If valid_word is True the function colors
        the cubes in the correct color (green) and if valid_word is False to
        wrong color (red).
        :param valid_word: a boolean value representing what color to color
        :return:
        """
        for pos in self.current_visited_positions:
            if valid_word:
                self.cubes[pos[0]][pos[1]].set_correct_color()
            else:
                self.cubes[pos[0]][pos[1]].set_wrong_color()

    def color_hint(self, hint):
        """
        Colors the given cubes position in hint and show the hint word in the
        above display.
        the user.
        :param hint: a tuple holding the hint word and positons
        :return:
        """
        for pos in hint[1]:
            self.cubes[pos[0]][pos[1]].set_hint_color()


class WordDisplay(tk.Frame):
    """
    The words display object (showing all the correct words the user found).
    """
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 20

    def __init__(self, parent):
        """
        Initializing thw WordDisplay frame.
        :param parent: frame container (parent widget)
        """

        tk.Frame.__init__(self, parent)

        self.scroll_bar = tk.Scrollbar(self)
        self.scroll_bar.pack(side='right', fill='y')

        self.correct_words = tk.Listbox(self,
                                        yscrollcommand=self.scroll_bar.set,
                                        width=22, height=14)

        self.correct_words.pack(side='left', fill='both')
        self.scroll_bar.config(command=self.correct_words.yview)

    def add_word(self, word):
        """
        Adds the given word to the words display.
        :param word: a word (str)
        """
        self.correct_words.insert(0, word)

    def reset_words(self):
        """
        Deletes all the words inside the display.
        """
        self.correct_words.delete(0, 'end')

    def get_length(self):
        """
        Returns the number of words in the display.
        :return: number of words in the display
        """
        return self.correct_words.size()
