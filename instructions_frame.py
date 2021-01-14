#################################################################
# FILE : instructions_frame.py
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs2 ex12 2020
# DESCRIPTION: the main program for the boggle program
# STUDENTS WE DISCUSSED THE EXERCISE WITH:
# WEB PAGES WE USED:
#################################################################

import tkinter as tk


PNG_REQUIRED_SIZE = (750, 470)


class InstructionsFrame(tk.Frame):
    """
    the Class for the instruction page of the game
    """
    _PNG_PATH = "assets/instructions.png"
    _FONT = 'Shree Devanagari 714'

    def __init__(self, parent, controller):
        """
        initiates the instructions page of the game, which includes an image of
        the instructions and a return button.
        :param parent: the root of the game
        :param controller: the Game class
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.instructions_img = self.load_instructions_png()

        self.back_button = tk.Button(self, text="Back", font=(self._FONT, 18),
                                command=lambda: controller.set_frame(
                                    "welcome_frame"))
        self.play_button = tk.Button(self, text="Play", font=(self._FONT, 18),
                                     command=lambda: controller.set_frame(
                                         "play_frame"))
        self.place_objects()

    def load_instructions_png(self, image_path=_PNG_PATH):
        """
        loads the instructions image from file
        :return: the instructions image as a Label
        """
        # load = Image.open(image_path)
        # resized = load.resize(PNG_REQUIRED_SIZE, Image.ANTIALIAS)
        # render = ImageTk.PhotoImage(resized)
        # instructions_img = tk.Label(self, image=render)
        # instructions_img.image = render
        # load = Image.open(self._HUJI_LOGO_PATH)
        # render = ImageTk.PhotoImage(load)
        render = tk.PhotoImage(file=image_path)
        instructions_img = tk.Label(self, image=render)
        instructions_img.image = render
        return instructions_img

    def place_objects(self):
        """
        packs ith image and the button in place
        """
        self.instructions_img.pack()
        self.instructions_img.place()
        self.back_button.pack(side='left', fill='x', expand='yes')
        # self.back_button.place(relwidth=1, rely=0.95)
        self.play_button.pack(side='right', fill='x', expand='yes')
        # self.play_button.place(relwidth=1, rely=0.95)
