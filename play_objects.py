import tkinter as tk
import datetime


class Timer(tk.Frame):
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 28
    _SECONDS = 180

    def __init__(self, parent):
        """
        Initializing Timer frame.
        :param parent: frame container (parent widget)
        """
        # initializing inherited Frame class
        tk.Frame.__init__(self, parent)

        self._time_running = False
        self.seconds_left = self._SECONDS
        self._timer_display = tk.Label(self,
                                       text=self.convert_seconds_str(),
                                       font=(self._FONT, self._FONT_SIZE))
        self._timer_display.grid()
        self.start = tk.Button(self, text="Start",
                               command=self.start_countdown).grid()
        self.stop = tk.Button(self, text="stop",
                              command=self.stop_countdown).grid()
        self.restart = tk.Button(self, text="restart",
                                 command=self.restart_countdown).grid()

    def start_countdown(self):
        """
        Starts the countdown.
        If time have not reach zero the function will subtract 1 second from
        the time left and then will call itself again after 1000
        milliseconds.
        Each call it sets the text value of the timer_display
        label to the new time left.
        """

        if self.seconds_left <= 30:
            self._timer_display['fg'] = 'red2'
        if self.seconds_left:
            self.seconds_left -= 1
            self._time_running = self.after(1000, self.start_countdown)
        else:
            self._time_running = False
        self._timer_display['text'] = self.convert_seconds_str()

    def stop_countdown(self):
        """
        Stops the countdown.
        """
        # todo: remove method
        if self._time_running:
            self.after_cancel(self._time_running)
            self._time_running = False

    def restart_countdown(self):
        """
        Restart the countdown.
        :return:
        """
        if self._time_running:
            self.seconds_left = self._SECONDS+1
        else:
            self.seconds_left = self._SECONDS
            self._timer_display['text'] = self.convert_seconds_str()

    def convert_seconds_str(self):
        """
        Converts the seconds to time format and then returning the sliced
        string to show only minutes.
        """
        time_remain = datetime.timedelta(seconds=self.seconds_left)
        return str(time_remain)[3:]


class Score(tk.Frame):
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 20

    def __init__(self, parent):
        """
        Initializing Timer frame.
        :param parent: frame container (parent widget)
        """
        # initializing inherited Frame class
        tk.Frame.__init__(self, parent)

        self.score = 0

        self._score_display = tk.Label(self,
                                       text=f'Score: {self.score}',
                                       font=(self._FONT, self._FONT_SIZE),
                                       )
        self._score_display.grid()

        self.add = tk.Button(self, text="add",
                               command=self.add_score).grid()

        self.restart = tk.Button(self, text="restart",
                                 command=self.reset_score).grid()

    def add_score(self, score=1):
        """
        Added the given score to score updates the label accordingly.
        :param score: the amount of score to add
        """
        print(f'added {score} to score')
        self.score += score
        self._score_display['text'] = f'Score: {self.score}'

    def reset_score(self):
        """
        Resets the score back to zero and updates the label accordingly.
        """
        print('reset score to 0')
        self.score = 0
        self._score_display['text'] = f'Score: {self.score}'


class Cube(tk.Frame):
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 26
    _WIDTH = 2
    _HEIGHT = 1
    _MAIN_COLOR = 'white'
    _CHOSEN_COLOR = 'red2'

    def __init__(self, parent, controller, letter, pos_x, pos_y):
        """
        Initializing Cube.
        :param parent: frame container (parent widget)
        :param controller: the widget controller
        :param letter: the letter for the cube
        :param pos_x: the x position in the board
        :param pos_y: the y position in the board
        """
        # initializing inherited Frame class
        tk.Frame.__init__(self, parent)
        self.configure(borderwidth=2, padx=4, pady=4)
        self.controller = controller
        self.letter = letter
        self.entered = False
        self.position = (pos_x, pos_y)

        self.content = tk.Label(self, padx=2, pady=2, cursor='hand1',
                                text=self.letter,
                                font=(self._FONT, self._FONT_SIZE),


                                bg=self._MAIN_COLOR, relief="groove",
                                borderwidth=6)
        self.content.grid()

        self.content.bind("<B1-Motion>", self.generate_events)
        self.content.bind("<Button-1>", self.mouse_enter_or_click)
        self.content.bind("<<B1-Enter>>", self.mouse_enter_or_click)
        self.content.bind("<<B1-Leave>>", self.on_mouse_leave)

    def mouse_enter_or_click(self, event):
        """
        A method triggered when a cube is clicked or the mouse have entered
        a cube after another cube is pressed.
        The method check if the cube haven't already entered and if the cube is
        a valid option for the last cube to create a word. If so the cube color
        is changed and her letter adds to the current word' her controller
        (board) is holding.
        :param event: bind event (not used)
        """
        if not self.entered and self.controller.valid_next_cube(self):
            self.content.configure(bg=self._CHOSEN_COLOR)
            self.controller.add_letter_to_current_word(self.letter)
            self.controller.add_position_to_positions_path(self.position)
            self.entered = True
            self.controller.set_last_cube_visited(self)

    def on_mouse_leave(self, event):
        """
        A method triggered when a the mouse leaves the cube.
        :param event: bind event (not used)
        """
        # todo: remove method
        pass

    def generate_events(self, event):
        """
        Generates 2 new event sequences:
        1. <<B1-Enter>> : a cube is entered while (!) another cube is pressed.
        2. <<B1-Leave>> : a cube is left while (!) another cube is pressed.
        :param event: bind event
        """
        # widget is the widget which is at the mouse coordinates
        widget = self.winfo_containing(event.x_root, event.y_root)
        # checks if widget is the same widget
        if self.content != widget:
            if self.content:
                self.content.event_generate("<<B1-Leave>>")
            current_widget = widget
            current_widget.event_generate("<<B1-Enter>>")

    def get_position(self):
        """
        Returns the cube positions in board.
        :return: cube position as Tuple
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
        :return:
        """
        self.content.configure(bg=self._MAIN_COLOR)


class Board(tk.Frame):
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 30
    _SIZE = (6, 5)

    def __init__(self, parent, controller):
        """
        Initializing Board.
        :param parent: frame container (parent widget)
        :param controller: the widget controller
        """
        # initializing inherited Frame class
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.configure(padx=10, pady=10)
        self.word_display = tk.Label(self, text='',
                                      font=(self._FONT, self._FONT_SIZE))
        self.word_display.grid()
        self.container = tk.Frame(self)
        self.container.grid()
        self.cubes = []
        self._init_cubes()
        self.current_word = ''
        self.current_visited_positions = []
        self.last_cube_visited = None

    def _init_cubes(self):
        """
        Initializing the board cubes.
        """
        letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDSEJFHSJKDFHD'
        for pos_x in range(self._SIZE[0]):
            row = []
            for pos_y in range(self._SIZE[1]):
                cube = Cube(self.container, self, letters[0:3], pos_x, pos_y)
                cube.grid(row=pos_x, column=pos_y, sticky="nsew")
                row.append(cube)
                letters = letters[2:]
            self.cubes.append(row)

    def reset_used_cube(self):
        """
        Reset all cubes in board, meaning reverting them back how they was when
        first Initialized.
        :return:
        """
        for i in range(len(self.cubes)):
            for j in range(len(self.cubes[i])):
                self.cubes[i][j].set_main_color()
                self.cubes[i][j].entered = False

    def add_letter_to_current_word(self, letter):
        """
        Adds given letter to word
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


    def get_word(self):
        """
        Returns the word
        :return: string word
        """
        return self.current_word

    def reset(self):
        """
        Reverts the board back to when first Initialized, but without changing
        the cubes.
        """
        self.current_word = ''
        self.last_cube_visited = None
        self.word_display.configure(text=self.current_word)

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
            return cube.get_position() in\
                   self.get_all_possible_neighbours_position(
                       self.last_cube_visited)

    def get_all_possible_neighbours_position(self, cube):
        """
        Returns a list with all the valid given cube neighbours position.
        :param cube: a Cube object
        :return: list of all valid positions
        """
        cube_pos = cube.get_position()
        possible_neighbours_position = [(cube_pos[0]-1, cube_pos[1]-1),
                                        (cube_pos[0]-1, cube_pos[1]),
                                        (cube_pos[0]-1, cube_pos[1]+1),
                                        (cube_pos[0], cube_pos[1]-1),
                                        (cube_pos[0], cube_pos[1]+1),
                                        (cube_pos[0]+1, cube_pos[1]-1),
                                        (cube_pos[0]+1, cube_pos[1]),
                                        (cube_pos[0]+1, cube_pos[1]+1)]
        return [pos for pos in possible_neighbours_position if 0 <=
                pos[0] <= 3 and 0 <= pos[1] <= 3]


class WordDisplay(tk.Frame):
    _FONT = 'Shree Devanagari 714'
    _FONT_SIZE = 20

    def __init__(self, parent):
        """
        Initializing Timer frame.
        :param parent: frame container (parent widget)
        """
        # initializing inherited Frame class
        tk.Frame.__init__(self, parent)

        self.score = 0

        self._word_display = tk.Label(self, text='test',
                                      font=(self._FONT, self._FONT_SIZE))

        self._word_display.grid()

