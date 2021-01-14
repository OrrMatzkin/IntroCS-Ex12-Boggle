#################################################################
# FILE : instructions_frame.py
# WRITER 1 : Avihu Almog , avihuxp, 315709980
# WRITER 2 : Orr Matzkin , orr.matzkin , 314082884
# EXERCISE : intro2cs Ex12 2020
# DESCRIPTION: The instructions screen frame
# STUDENTS WE DISCUSSED THE EXERCISE WITH: N/A
# WEB PAGES WE USED: https://docs.python.org/3.3/library/tkinter.html#images
#################################################################

import tkinter as tk


class InstructionsFrame(tk.Frame):
    """
    the Class for the instruction page of the game
    """
    _PNG_PATH = "assets/instructions.png"
    _FONT = 'Shree Devanagari 714'

    def __init__(self, parent, controller):
        """
        Initiates the instructions page of the game, which includes an image of
        the instructions a return button and a play button.
        :param parent: the root of the game
        :param controller: the Game class
        """
        tk.Frame.__init__(self, parent)
        self.controller = controller

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
        loads the instructions image from file.
        :return: the instructions image as a Label
        """
        render = tk.PhotoImage(file=image_path)
        instructions_img = tk.Label(self, image=render)
        instructions_img.image = render
        return instructions_img

    def place_objects(self):
        """
        packs ith image and the button in place
        """
        self.instructions_img.pack()
        self.back_button.pack(side='left', fill='x', expand='yes')
        self.play_button.pack(side='right', fill='x', expand='yes')
